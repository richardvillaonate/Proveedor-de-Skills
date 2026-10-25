#!/usr/bin/env python3
"""Regenera el registro del proveedor de skills.

Lee .agents/skills/ (la verdad del disco) y skills-meta.json (fichas curadas) y escribe:
  ESTADO_SKILLS.md          estado general (tabla, proyectos conectados, historial)
  HOJA_DE_VIDA_SKILLS.txt   hoja de vida de cada skill
  GUIA_POR_SKILL.md         como enlazar y llamar cada skill

Uso:  ./actualizar-registro.py [--quiet]
Ejecutalo cada vez que instales, modifiques o borres una skill.
"""
import hashlib
import json
import shutil
import sys
import textwrap
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / ".agents" / "skills"
META_FILE = ROOT / "skills-meta.json"
STATE_FILE = ROOT / ".registro-estado.json"
LINKS_LOG = ROOT / "registro-enlaces.tsv"
LOCK_FILE = ROOT / "skills-lock.json"
GLOBAL_SKILLS = Path.home() / ".agents" / "skills"
PENDIENTE = "(pendiente: completar la ficha en skills-meta.json)"

NOW = datetime.now()
TODAY = NOW.strftime("%Y-%m-%d")
STAMP = NOW.strftime("%Y-%m-%d %H:%M")


def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def frontmatter(skill_md):
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    block = text.split("\n---", 1)[0].splitlines()[1:]
    data, parent = {}, None
    for line in block:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        key, _, value = line.strip().partition(":")
        value = value.strip().strip("'\"")
        if indent == 0:
            parent = None if value else key
            if value:
                data[key] = value
        elif parent:
            data[f"{parent}.{key}"] = value
    return data


def skill_files(skill_dir):
    return [p for p in sorted(skill_dir.rglob("*")) if p.is_file() and "__pycache__" not in p.parts]


def tree_hash(skill_dir):
    digest = hashlib.sha256()
    for p in skill_files(skill_dir):
        digest.update(str(p.relative_to(skill_dir)).encode())
        digest.update(p.read_bytes())
    return digest.hexdigest()


def disk_facts(skill_dir):
    files = skill_files(skill_dir)
    scripts_dir = skill_dir / "scripts"
    assets_dir = skill_dir / "assets"
    refs_dir = skill_dir / "references"
    return {
        "archivos": len(files),
        "kb": round(sum(p.stat().st_size for p in files) / 1024),
        "hash": tree_hash(skill_dir),
        "scripts": sorted(p.name for p in scripts_dir.iterdir() if p.is_file()) if scripts_dir.is_dir() else [],
        "starters": sorted(p.name for p in assets_dir.iterdir() if p.is_dir()) if assets_dir.is_dir() else [],
        "referencias": len(list(refs_dir.glob("*.md"))) if refs_dir.is_dir() else 0,
    }


def copied_here(name):
    copy = ROOT / ".claude" / "skills" / name
    return copy.is_dir() and not copy.is_symlink() and (copy / "SKILL.md").is_file()


def sync_claude_skills(on_disk, managed_before):
    """Mantiene .claude/skills de este proyecto como copias reales (sin enlaces) de .agents/skills."""
    dest = ROOT / ".claude" / "skills"
    dest.mkdir(parents=True, exist_ok=True)
    for name in on_disk:
        target = dest / name
        if target.is_symlink():
            target.unlink()
        if target.is_dir() and tree_hash(target) == tree_hash(SRC / name):
            continue
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(SRC / name, target)
    for name in managed_before - set(on_disk):
        stale = dest / name
        if stale.is_symlink():
            stale.unlink()
        elif stale.is_dir():
            shutil.rmtree(stale)


def external_links():
    """Proyectos conectados segun registro-enlaces.tsv, verificando que el enlace siga vivo."""
    projects = {}
    if not LINKS_LOG.exists():
        return projects
    for line in LINKS_LOG.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        date, target, skill = parts
        link = Path(target) / ".claude" / "skills" / skill
        if link.is_symlink():
            alive = (SRC / skill).exists() and link.resolve() == (SRC / skill).resolve()
        else:
            alive = (link / "SKILL.md").is_file()
        entry = projects.setdefault(target, {})
        entry[skill] = {"fecha": date, "viva": alive}
    return projects


def first_sentence(text):
    text = text.strip()
    cut = text.find(". ")
    return text[: cut + 1] if cut > 0 else text


def wrap(text, indent="", width=88):
    return textwrap.fill(text, width=width, initial_indent=indent, subsequent_indent=indent,
                         break_on_hyphens=False, break_long_words=False)


def main(quiet=False):
    meta_all = load_json(META_FILE, {}).get("skills", {})
    state = load_json(STATE_FILE, {"skills": {}, "historial": []})
    lock = load_json(LOCK_FILE, {}).get("skills", {})

    on_disk = sorted(p.name for p in SRC.iterdir() if (p / "SKILL.md").is_file()) if SRC.is_dir() else []
    sync_claude_skills(on_disk, set(state["skills"]))
    sin_ficha = [n for n in on_disk if n not in meta_all]
    ausentes = sorted(n for n in meta_all if n not in on_disk)

    skills = {}
    for name in on_disk:
        facts = disk_facts(SRC / name)
        fm = frontmatter(SRC / name / "SKILL.md")
        meta = meta_all.get(name, {})
        prev = state["skills"].get(name)
        if prev is None:
            cambio = "nueva"
            first_seen = meta.get("instalada", TODAY)
            state["historial"].append({"fecha": first_seen, "evento": "REGISTRADA", "skill": name})
        elif prev["hash"] != facts["hash"]:
            cambio = "modificada"
            first_seen = prev["primera_vez"]
            state["historial"].append({"fecha": TODAY, "evento": "MODIFICADA", "skill": name})
        else:
            cambio, first_seen = "sin cambios", prev["primera_vez"]
        state["skills"][name] = {"hash": facts["hash"], "primera_vez": first_seen, "revisada": TODAY}
        skills[name] = {
            **facts,
            "cambio": cambio,
            "descripcion": fm.get("description", ""),
            "version": fm.get("metadata.version") or fm.get("version") or "n/d",
            "nombre_ok": fm.get("name") == name,
            "aqui": copied_here(name),
            "ficha_basica": meta.get("ficha") == "basica",
            "lock": name in lock,
            "m": {
                "categoria": meta.get("categoria", "Sin clasificar"),
                "fuente": meta.get("fuente") or (f"github: {lock[name]['source']}" if name in lock else "no registrada"),
                "idioma": meta.get("idioma", "n/d"),
                "instalada": first_seen,
                "que_hace": meta.get("que_hace") or first_sentence(fm.get("description", "")) or PENDIENTE,
                "cuando_usarla": meta.get("cuando_usarla") or fm.get("description", "") or PENDIENTE,
                "donde_usarla": meta.get("donde_usarla", PENDIENTE),
                "stack": meta.get("stack", "n/d"),
                "combina_con": meta.get("combina_con", []),
                "disparadores": meta.get("disparadores") or "ver la descripcion en SKILL.md",
                "invocacion": meta.get("invocacion") or ("manual" if fm.get("disable-model-invocation") == "true" else "auto"),
                "ejemplo": meta.get("ejemplo") or f"Usa {name} para ... (nombrala en el prompt).",
                "requisitos": meta.get("requisitos", "n/d"),
                "notas": meta.get("notas", ""),
            },
        }

    for name in sorted(set(state["skills"]) - set(on_disk)):
        state["historial"].append({"fecha": TODAY, "evento": "ELIMINADA", "skill": name})
        del state["skills"][name]

    projects = external_links()
    global_extra = sorted(
        p.name for p in GLOBAL_SKILLS.iterdir() if (p / "SKILL.md").is_file() and p.name not in on_disk
    ) if GLOBAL_SKILLS.is_dir() and GLOBAL_SKILLS.resolve() != SRC.resolve() else []

    write_estado(skills, sin_ficha, ausentes, projects, global_extra, state)
    write_hoja_de_vida(skills, projects)
    write_guia(skills)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if not quiet:
        nuevas = [n for n, s in skills.items() if s["cambio"] == "nueva"]
        modif = [n for n, s in skills.items() if s["cambio"] == "modificada"]
        print(f"Registro actualizado: {len(skills)} skills en {SRC}")
        if nuevas:
            print(f"  nuevas: {', '.join(nuevas)}")
        if modif:
            print(f"  modificadas: {', '.join(modif)}")
        if sin_ficha:
            print(f"  FALTA ficha en skills-meta.json: {', '.join(sin_ficha)}")
        if ausentes:
            print(f"  fichas sin skill en disco: {', '.join(ausentes)}")


def write_estado(skills, sin_ficha, ausentes, projects, global_extra, state):
    cats = {}
    for name, s in skills.items():
        cats.setdefault(s["m"]["categoria"], []).append(name)
    total_kb = sum(s["kb"] for s in skills.values())
    vivos = {t: {k: v for k, v in e.items() if v["viva"]} for t, e in projects.items()}
    vivos = {t: e for t, e in vivos.items() if e}

    out = [
        "# Estado general de skills",
        "",
        f"> Generado automaticamente por `actualizar-registro.py` el **{STAMP}**. No lo edites a mano: "
        "cambia `skills-meta.json` y vuelve a ejecutar el script.",
        "",
        "## Resumen",
        "",
        f"- **Skills en el proveedor:** {len(skills)} ({total_kb / 1024:.1f} MB)",
        f"- **Copias reales en `.claude/skills` de este proyecto:** {sum(s['aqui'] for s in skills.values())} de {len(skills)}",
        f"- **Skills con ficha basica (pendientes de detallar):** {sum(s['ficha_basica'] for s in skills.values())}",
        f"- **Proyectos consumidores con enlaces vivos:** {len(vivos)}",
        f"- **Skills sin ficha completa:** {len(sin_ficha)}",
        f"- **Skills globales en `~/.agents/skills` que aun no estan en el proveedor:** {len(global_extra)}",
        "",
        "| Categoria | Cantidad | Skills |",
        "|---|---:|---|",
    ]
    for cat in sorted(cats):
        out.append(f"| {cat} | {len(cats[cat])} | {', '.join(f'`{n}`' for n in cats[cat])} |")

    out += ["", "## Inventario", "",
            "| Skill | Categoria | Version | Idioma | Archivos | KB | Scripts | Starters | Invocacion | Aqui | Instalada | Cambio |",
            "|---|---|---|---|---:|---:|---:|---:|---|:-:|---|---|"]
    for name, s in skills.items():
        m = s["m"]
        inv = "/" + name if m["invocacion"] == "manual" else "auto"
        out.append(
            f"| `{name}` | {m['categoria']} | {s['version']} | {m['idioma']} | {s['archivos']} | {s['kb']} | "
            f"{len(s['scripts'])} | {len(s['starters'])} | {inv} | {'si' if s['aqui'] else 'no'} | "
            f"{m['instalada']} | {s['cambio']} |"
        )
    out += ["", "_Aqui = copia real en `.claude/skills` de este proyecto (se sincroniza desde `.agents/skills` al ejecutar el script). Cambio = diferencia respecto a la ultima ejecucion del script._"]

    out += ["", "## Proyectos conectados", ""]
    if vivos:
        out += ["| Proyecto | Skills enlazadas |", "|---|---|"]
        for target, entry in sorted(vivos.items()):
            out.append(f"| `{target}` | {', '.join(f'`{k}`' for k in sorted(entry))} |")
    else:
        out.append("Aun no hay proyectos conectados. `link-skills.sh -t <proyecto>` los registra aqui.")
    rotos = [(t, k) for t, e in projects.items() for k, v in e.items() if not v["viva"]]
    if rotos:
        out += ["", "Enlaces registrados que ya no existen o apuntan a otro lado:", ""]
        out += [f"- `{t}` → `{k}`" for t, k in sorted(rotos)]

    problemas = [f"- `{n}`: el campo `name` del frontmatter no coincide con la carpeta" for n, s in skills.items() if not s["nombre_ok"]]
    problemas += [f"- `{n}`: sin ficha en `skills-meta.json`" for n in sin_ficha]
    problemas += [f"- `{n}`: hay ficha pero la carpeta no existe en `.agents/skills`" for n in ausentes]
    out += ["", "## Pendientes y avisos", ""]
    out += problemas or ["Todo en orden."]

    basicas = [n for n, s in skills.items() if s["ficha_basica"]]
    out += ["", "## Fichas basicas por detallar", ""]
    out.append((", ".join(f"`{n}`" for n in basicas) + "\n\nTienen categoria y datos tomados del frontmatter; "
                "agrega `que_hace`, `donde_usarla`, `ejemplo`, etc. en `skills-meta.json` y quita `\"ficha\": \"basica\"`.")
               if basicas else "Ninguna.")

    out += ["", "## Skills globales aun fuera del proveedor", ""]
    if global_extra:
        out += ["Estan en `~/.agents/skills` pero no en este proveedor. Si quieres centralizarlas, copialas a `.agents/skills/` y ejecuta el script.", "",
                ", ".join(f"`{n}`" for n in global_extra)]
    else:
        out.append("Ninguna.")

    out += ["", "## Historial", "", "| Fecha | Evento | Skill |", "|---|---|---|"]
    for ev in sorted(state["historial"], key=lambda e: e["fecha"], reverse=True)[:60]:
        out.append(f"| {ev['fecha']} | {ev['evento']} | `{ev['skill']}` |")

    out += ["", "## Como actualizar este archivo", "",
            "1. Instala la skill en `.agents/skills/<nombre>/` (ver `TUTORIAL.md`).",
            "2. Ejecuta `./actualizar-registro.py`.",
            "3. Si avisa de que falta la ficha, completala en `skills-meta.json` y ejecuta el script otra vez.", ""]
    (ROOT / "ESTADO_SKILLS.md").write_text("\n".join(out), encoding="utf-8")


def write_hoja_de_vida(skills, projects):
    bar = "=" * 90
    line = "-" * 90
    out = [
        bar,
        "HOJA DE VIDA DE SKILLS - PROVEEDOR LOCAL",
        f"Actualizado: {STAMP}    Total: {len(skills)} skills",
        f"Ubicacion: {SRC}",
        "Archivo generado por actualizar-registro.py (editar skills-meta.json, no este archivo).",
        bar, "",
        "INDICE", line,
    ]
    cats = {}
    for name, s in skills.items():
        cats.setdefault(s["m"]["categoria"], []).append(name)
    for cat in sorted(cats):
        out.append(f"[{cat}]")
        out.append(wrap(", ".join(cats[cat]), "   "))
    out.append("")

    for n, (name, s) in enumerate(skills.items(), 1):
        m = s["m"]
        enlazadas = sorted(t for t, e in projects.items() if name in e and e[name]["viva"])
        out += [bar, f"{n:02d}. {name.upper()}", bar]

        def row(label, value):
            out.append(textwrap.fill(f"{label:<16}{value}", width=90, subsequent_indent=" " * 16,
                                     break_on_hyphens=False, break_long_words=False))

        row("Categoria:", m["categoria"])
        row("Version:", s["version"])
        row("Fuente:", m["fuente"])
        row("Idioma:", m["idioma"])
        row("Instalada:", m["instalada"])
        row("Invocacion:", f"manual con /{name}" if m["invocacion"] == "manual" else "automatica (por contexto) o nombrandola en el prompt")
        row("Estado aqui:", "copia real en .claude/skills de este proyecto" if s["aqui"] else "NO esta en .claude/skills de este proyecto")
        row("Usada en:", ", ".join(enlazadas) if enlazadas else "ningun otro proyecto registrado")
        out.append("")
        row("QUE HACE:", m["que_hace"])
        row("CUANDO USARLA:", m["cuando_usarla"])
        row("DONDE USARLA:", m["donde_usarla"])
        row("STACK:", m["stack"])
        row("COMBINA CON:", ", ".join(m["combina_con"]) or "n/d")
        row("DISPARADORES:", m["disparadores"])
        trae = [f"{s['archivos']} archivos ({s['kb']} KB)"]
        if s["referencias"]:
            trae.append(f"{s['referencias']} guias de referencia")
        if s["scripts"]:
            trae.append("scripts: " + ", ".join(s["scripts"]))
        if s["starters"]:
            trae.append("assets: " + ", ".join(s["starters"]))
        row("TRAE:", "; ".join(trae))
        row("REQUISITOS:", m["requisitos"])
        if m["notas"]:
            row("NOTAS:", m["notas"])
        row("EJEMPLO:", m["ejemplo"])
        out.append("")
    out += [bar, "FIN DEL REGISTRO", bar, ""]
    (ROOT / "HOJA_DE_VIDA_SKILLS.txt").write_text("\n".join(out), encoding="utf-8")


def write_guia(skills):
    out = [
        "# Guia por skill",
        "",
        f"> Generada por `actualizar-registro.py` el **{STAMP}**. Fuente: `skills-meta.json`. "
        "Para el concepto general y la instalacion lee `TUTORIAL.md`.",
        "",
        "En cada comando, `/ruta/a/tu-proyecto` es el proyecto que va a consumir la skill. "
        "Ejecutalo desde esta carpeta, o reemplaza `./link-skills.sh` por su ruta absoluta.",
        "",
        "## Indice", "",
    ]
    cats = {}
    for name, s in skills.items():
        cats.setdefault(s["m"]["categoria"], []).append(name)
    for cat in sorted(cats):
        out.append(f"- **{cat}:** " + ", ".join(f"[{n}](#{n})" for n in cats[cat]))
    out.append("")

    for name, s in skills.items():
        m = s["m"]
        out += [f"## {name}", "", f"> {m['que_hace']}", "",
                f"- **Categoria:** {m['categoria']} · **Version:** {s['version']} · **Idioma de la skill:** {m['idioma']}",
                f"- **1. Enlazarla:** `./link-skills.sh -t /ruta/a/tu-proyecto {name}`"]
        if m["invocacion"] == "manual":
            out.append(f"- **2. Llamarla:** solo de forma explicita: escribe `/{name} <descripcion>` en Claude Code dentro del proyecto. No se activa sola.")
        else:
            out.append(f"- **2. Llamarla:** se activa sola cuando el pedido encaja (palabras clave: {m['disparadores']}), o nombrala en el prompt.")
        out.append(f"- **Prompt de ejemplo:** «{m['ejemplo']}»")
        out.append(f"- **Cuando:** {m['cuando_usarla']}")
        if m["combina_con"]:
            out.append("- **Enlazala junto a:** " + ", ".join(f"`{c}`" for c in m["combina_con"])
                       + f" → `./link-skills.sh -t /ruta/a/tu-proyecto {name} {' '.join(m['combina_con'])}`")
        recursos = []
        if s["scripts"]:
            recursos.append("scripts `" + "`, `".join(s["scripts"]) + "`")
        if s["starters"]:
            recursos.append("assets `" + "`, `".join(s["starters"]) + "`")
        if s["referencias"]:
            recursos.append(f"{s['referencias']} guias en `references/`")
        if recursos:
            out.append(f"- **Recursos incluidos** (en `.agents/skills/{name}/`): " + "; ".join(recursos))
        out.append(f"- **Requisitos:** {m['requisitos']}")
        if m["notas"]:
            out.append(f"- **Notas:** {m['notas']}")
        out.append("")
    (ROOT / "GUIA_POR_SKILL.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main(quiet="--quiet" in sys.argv[1:])

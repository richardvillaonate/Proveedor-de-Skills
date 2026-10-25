# Tutorial: usar este repositorio como proveedor de skills

Como entregar una skill a un proyecto, como llamarla desde Claude Code y como instalar skills nuevas sin perder el control del inventario. Para el comando exacto de cada una de las 107 skills ve a [GUIA_POR_SKILL.md](GUIA_POR_SKILL.md).

## 1. Como funciona

Claude Code busca skills en `.claude/skills/<nombre>/SKILL.md` del proyecto abierto (y en `~/.claude/skills` a nivel de usuario). Las skills reales viven en `.agents/skills/<nombre>` de este repositorio, como carpetas normales sin enlaces. Para usarlas en un proyecto hay dos modos:

```
Enlace (por defecto):  mi-web/.claude/skills/gsap-scrolltrigger  ──►  Proveedor de Skills/.agents/skills/gsap-scrolltrigger
Copia (-c):            mi-web/.claude/skills/gsap-scrolltrigger  =    copia real e independiente
```

| | Enlace | Copia (`-c`) |
|---|---|---|
| Actualizar una skill aqui | Se ve al instante en el proyecto | Hay que volver a copiar |
| Si se mueve/borra el proveedor | El enlace se rompe | El proyecto sigue funcionando |
| Cuando usarlo | Proyectos propios que quieres mantener sincronizados | Proyectos que se entregan, se suben a git o deben ser autonomos |

En **este** repositorio no hay enlaces: `.claude/skills` contiene copias reales y `actualizar-registro.py` las mantiene al dia respecto a `.agents/skills`.

Claude lee de cada skill solo el `name` y la `description` al arrancar; el contenido completo (`SKILL.md`, `references/`, `scripts/`) se carga cuando la skill se usa.

## 2. Entregar skills a un proyecto

Desde la carpeta del proveedor:

```bash
cd "/home/richarddev/Desktop/Proveedor de Skills"

./link-skills.sh --list                              # ver disponibles
./link-skills.sh -t /ruta/al/proyecto skill-a skill-b   # enlazar algunas
./link-skills.sh -t /ruta/al/proyecto                # enlazar todas
./link-skills.sh -t /ruta/al/proyecto -c skill-a     # copia real en vez de enlace
```

Tambien puedes ejecutarlo estando dentro del proyecto destino, sin `-t`:

```bash
cd ~/proyectos/mi-web
"/home/richarddev/Desktop/Proveedor de Skills/link-skills.sh" threejs-webgl
```

Que hace el script:

- Crea `<proyecto>/.claude/skills/` si no existe.
- Enlaza (o copia, con `-c`) cada skill pedida; si ya esta enlazada bien, la omite; si hay algo distinto con ese nombre, **no lo toca** y avisa.
- Apunta el enlace en `registro-enlaces.tsv` y refresca el registro (`ESTADO_SKILLS.md`, etc.).

Para **quitar** una skill de un proyecto basta borrar su carpeta o enlace (no toca la skill del proveedor):

```bash
rm -r /ruta/al/proyecto/.claude/skills/gsap-scrolltrigger
```

## 3. Llamar una skill

Abre Claude Code dentro del proyecto (si ya estaba abierto y no aparece la skill, reinicia la sesion). Hay tres formas:

| Forma | Como | Cuando aplica |
|---|---|---|
| **Automatica** | Pides algo que encaja con la `description` de la skill («anima estas secciones con ScrollTrigger») y Claude la carga solo | Casi todas las skills |
| **Por nombre** | Nombrala en el prompt: «usa `threejs-webgl` para...» | Cuando quieres forzar cual usar |
| **Comando** | Escribes `/<nombre> <argumentos>` | Siempre; **obligatorio** para `spec`, que tiene `disable-model-invocation` y nunca se activa sola |

Ejemplos:

```text
Con gsap-scrolltrigger haz que las tres secciones se fijen y revelen su contenido al hacer scroll.
Crea una landing cinematografica para un lanzamiento de zapatillas.        (auto: cinematographic-websites)
/spec Permitir que los usuarios exporten su historial a PDF
```

Consejo: la descripcion de cada skill lista sus palabras clave. Si una skill no se activa sola, nombrala. Los disparadores de cada una estan en `GUIA_POR_SKILL.md`.

## 4. Combinar skills

Muchas skills se complementan. Enlazalas juntas al empezar el proyecto:

| Proyecto | Skills a enlazar |
|---|---|
| Landing cinematografica | `cinematographic-websites`, `gsap-scrolltrigger`, `modern-web-design`, `barba-js` (si es multipagina) |
| Experiencia 3D con scroll (JS) | `threejs-webgl`, `gsap-scrolltrigger`, `web3d-integration-patterns`, `blender-web-pipeline` |
| App React con 3D | `react-three-fiber`, `threejs-webgl`, `web3d-integration-patterns`, `react-spring-physics`, `blender-web-pipeline` |
| Landing React con componentes animados | `animated-component-libraries`, `motion-framer`, `modern-web-design` |
| Juego web 3D | `babylonjs-engine` o `playcanvas-engine`, `blender-web-pipeline`, `substance-3d-texturing` |
| Juego / efectos 2D | `pixijs-2d`, `lottie-animations` o `rive-interactive` |
| Experiencia VR/AR | `aframe-webxr`, `blender-web-pipeline` |
| Sitio con buen SEO | `seo`, `seo-audit`, `ai-seo`, `programmatic-seo` (si hay paginas a escala) |
| Feature grande, antes de programar | `spec` |

Evita mezclar dos librerias que hacen lo mismo en el mismo proyecto (por ejemplo, dos smooth scroll: Lenis y Locomotive; o tres motores 3D). Las skills `web3d-integration-patterns` y `modern-web-design` ayudan a decidir.

## 5. Instalar una skill nueva en el proveedor

Regla: **todas las skills se instalan aqui, en `.agents/skills/`**, nunca directo en un proyecto.

### Opcion A: desde GitHub con la CLI de skills

`skills-lock.json` lo genero esa CLI al instalar `spec`. Desde esta carpeta:

```bash
cd "/home/richarddev/Desktop/Proveedor de Skills"
npx skills add <usuario>/<repositorio>      # ej.: czabala847/spec-loop
```

Deja la skill en `.agents/skills/<nombre>/`, la deja disponible en `.claude/skills/` de este proyecto y actualiza `skills-lock.json` (origen y hash). Si la CLI crea un enlace simbolico en `.claude/skills`, no importa: `./actualizar-registro.py` lo reemplaza por una copia real.

### Opcion B: copiar una carpeta que ya tienes

```bash
cp -r /ruta/a/nueva-skill "/home/richarddev/Desktop/Proveedor de Skills/.agents/skills/"
```

Usa `cp -rL` si la carpeta de origen contiene enlaces simbolicos, para traer el contenido real y no el enlace. El script copia la skill a `.claude/skills/` al registrarla.

### Opcion C: crearla tu mismo

Usa la skill `skill-creator` (ya instalada): «usa skill-creator para crear una skill que...». Tiene `init_skill.py`, `quick_validate.py` y `package_skill.py`.

### Comprobar la instalacion

- Existe `.agents/skills/<nombre>/SKILL.md`.
- El `name:` del frontmatter es **igual al nombre de la carpeta**.
- Tiene `description:` clara, con cuando usarla y palabras clave (es lo que Claude usa para decidir si activarla).

### Registrar la skill (siempre)

```bash
./actualizar-registro.py
```

Si la skill es nueva, el script avisa: `FALTA ficha en skills-meta.json`. Agrega su entrada en `skills-meta.json` copiando el formato de otra:

```json
"nombre-de-la-skill": {
  "categoria": "Animacion / Motion",
  "fuente": "github: usuario/repo",
  "idioma": "EN",
  "instalada": "2026-10-25",
  "que_hace": "Una o dos frases.",
  "cuando_usarla": "Situaciones en las que conviene.",
  "donde_usarla": "Tipos de proyecto donde aplica.",
  "stack": "Tecnologias",
  "combina_con": ["otra-skill"],
  "disparadores": "palabras clave que la activan",
  "invocacion": "auto",
  "ejemplo": "Prompt de ejemplo.",
  "requisitos": "Software o cuentas externas necesarias.",
  "notas": ""
}
```

Vuelve a ejecutar `./actualizar-registro.py`. Ya aparece completa en `ESTADO_SKILLS.md`, `HOJA_DE_VIDA_SKILLS.txt`, `GUIA_POR_SKILL.md` y `CATALOGO_POR_CATEGORIA.md`. Para skills que solo se invocan con comando (como `spec`), usa `"invocacion": "manual"`.

## 6. Actualizar o eliminar skills

- **Modificar:** edita los archivos en `.agents/skills/<nombre>/` y ejecuta `./actualizar-registro.py`: la marca como `modificada` y lo anota en el historial. Todos los proyectos enlazados ven el cambio al instante.
- **Eliminar:** borra `.agents/skills/<nombre>/` y ejecuta el script: quita tambien su copia de `.claude/skills/` y la registra como `ELIMINADA`. Los enlaces en otros proyectos quedaran rotos (las copias `-c` no); el estado los lista en *Proyectos conectados* para que los limpies.

## 7. Que archivo consultar

| Pregunta | Archivo |
|---|---|
| ¿Con cuantas skills cuento y en que proyectos estan? | `ESTADO_SKILLS.md` |
| ¿Que hace X, cuando y donde la uso? | `HOJA_DE_VIDA_SKILLS.txt` |
| ¿Que comando y prompt uso para X? | `GUIA_POR_SKILL.md` |
| ¿Que skills tengo por categoria y para que sirve cada una? | `CATALOGO_POR_CATEGORIA.md` |
| ¿Cuando se instalo o cambio algo? | Historial al final de `ESTADO_SKILLS.md` |

## 8. Solucion de problemas

| Sintoma | Causa probable | Solucion |
|---|---|---|
| La skill no aparece en Claude Code | Sesion abierta antes del enlace, o el enlace no esta en `<proyecto>/.claude/skills/` | Reinicia la sesion; verifica con `ls -la <proyecto>/.claude/skills` |
| El enlace aparece en rojo / roto | Se movio o renombro la carpeta del proveedor (los enlaces son absolutos) | Borra los enlaces rotos y vuelve a ejecutar `link-skills.sh -t <proyecto>`; o usa `-c` para no depender del proveedor |
| `omitida (ya existe algo distinto)` | En el proyecto hay una carpeta o enlace con ese nombre | Revisa y decide: `rm` el existente y re-enlaza, o conserva el del proyecto |
| `no existe: <nombre>` | El nombre esta mal escrito o no tiene `SKILL.md` | `./link-skills.sh --list` |
| La skill no se activa sola | La `description` no encaja con tu pedido | Nombrala en el prompt o usa `/<nombre>` |
| `spec` no responde a prompts normales | Es solo manual | Escribe `/spec <descripcion>` |
| El script avisa de que el `name` no coincide | Carpeta y frontmatter difieren | Corrige uno de los dos |
| Para otros agentes (no Claude Code) | `link-skills.sh` solo crea `.claude/skills` | Copia o enlaza a mano `.agents/skills` del proveedor en el destino que ese agente lea |

## 9. Flujo recomendado

1. Instalas la skill en el proveedor → `./actualizar-registro.py` → completas la ficha.
2. Empiezas un proyecto → `./link-skills.sh -t <proyecto> <skills que necesitas>`.
3. Trabajas en el proyecto llamando las skills.
4. Mejoras una skill → la editas aqui → `./actualizar-registro.py`.
5. Consultas `ESTADO_SKILLS.md` cuando quieras ver el panorama general.

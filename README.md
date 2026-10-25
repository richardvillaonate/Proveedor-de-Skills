# Proveedor de Skills

Repositorio local que **centraliza todas mis skills de Claude Code** y las **provee a cualquier proyecto**. Las skills viven aqui como **carpetas reales** (nada depende de enlaces ni de otras carpetas del equipo); cada proyecto recibe un enlace o una copia, a eleccion.

```
Proveedor de Skills/              <- fuente unica de verdad
├── .agents/skills/<skill>/       <- las skills reales (SKILL.md + references/ scripts/ assets/)
├── .claude/skills/<skill>        <- copias reales para usar las skills dentro de este mismo proyecto
├── link-skills.sh                <- entrega skills a otro proyecto
├── actualizar-registro.py        <- regenera el estado y las hojas de vida
├── skills-meta.json              <- fichas curadas (lo unico que se edita a mano)
├── skills-lock.json              <- versiones/origen de skills instaladas desde GitHub
├── ESTADO_SKILLS.md              <- (generado) estado general del inventario
├── HOJA_DE_VIDA_SKILLS.txt       <- (generado) hoja de vida de cada skill
├── GUIA_POR_SKILL.md             <- (generado) como enlazar y llamar cada skill
├── TUTORIAL.md                   <- como funciona el proveedor, paso a paso
└── registro-enlaces.tsv          <- (generado) bitacora de a que proyectos se ha enlazado cada skill
```

## Por que existe

- **Una fuente unica.** Si entregas por enlace, actualizas una skill aqui y todos los proyectos la ven actualizada.
- **Independencia.** Todo el contenido esta fisicamente aqui: borrar `~/.agents/skills` u otra carpeta no rompe nada de este repositorio.
- **Control.** Siempre sabes con que skills cuentas, de donde vinieron y en que proyectos se usan.
- **Entrega selectiva.** Cada proyecto recibe solo las skills que necesita, no las 104.

## Inicio rapido

```bash
cd "/home/richarddev/Desktop/Proveedor de Skills"

./link-skills.sh --list                                   # que skills hay
./link-skills.sh -t ~/proyectos/mi-web gsap-scrolltrigger cinematographic-websites
./link-skills.sh -t ~/proyectos/mi-web                    # o todas
./link-skills.sh -t ~/proyectos/mi-web -c spec            # copia real, sin enlace simbolico
```

Luego abre Claude Code en `~/proyectos/mi-web`: las skills se activan solas segun lo que pidas, o con `/<nombre-de-la-skill>`. Detalle completo en [TUTORIAL.md](TUTORIAL.md).

## Que hay en el inventario

104 skills, ~13 MB. Resumen por categoria (la lista viva esta en [ESTADO_SKILLS.md](ESTADO_SKILLS.md)):

| Categoria | Skills |
|---|---|
| 3D / WebGL / XR (10) | `threejs-webgl`, `threejs-animation`, `shader-glsl`, `react-three-fiber`, `babylonjs-engine`, `playcanvas-engine`, `aframe-webxr`, `spline-interactive`, `lightweight-3d-effects`, `web3d-integration-patterns` |
| Pipeline de assets 3D (2) | `blender-web-pipeline`, `substance-3d-texturing` |
| Animacion / Motion (13) | `gsap-core`, `gsap-scrolltrigger`, `cinematic-gsap-lenis-motion-system`, `cinematic-scroll-storytelling`, `implement_lenis_scroll`, `animejs`, `motion-framer`, `react-spring-physics`, `lottie-animations`, `rive-interactive`, `scroll-reveal-libraries`, `locomotive-scroll`, `barba-js` |
| 2D / Canvas (1) | `pixijs-2d` |
| UI / Diseno web (4) | `modern-web-design`, `animated-component-libraries`, `cinematographic-websites`, `scroll-world-storytelling` |
| Diseno UX / UI (8) | `ux-heuristics`, `refactoring-ui`, `top-design`, `web-typography`, `microinteractions`, `design-everyday-things`, `ios-hig-design`, `steve-jobs-design-review` |
| SEO (4) | `seo`, `seo-audit`, `ai-seo`, `programmatic-seo` |
| Producto y descubrimiento (9) | `lean-startup`, `lean-ux`, `lean-analytics`, `mom-test`, `jobs-to-be-done`, `design-sprint`, `continuous-discovery`, `inspired-product`, `hooked-ux` |
| Estrategia y negocio (13) | `good-strategy-bad-strategy`, `blue-ocean-strategy`, `crossing-the-chasm`, `obviously-awesome`, `hundred-million-offers`, `monetizing-innovation`, `predictable-revenue`, `traction-eos`, `37signals-way`, `negotiation`, `high-output-management`, `team-topologies`, `drive-motivation` |
| Marketing y crecimiento (8) | `cro-methodology`, `storybrand-messaging`, `one-page-marketing`, `scorecard-marketing`, `made-to-stick`, `contagious`, `influence-psychology`, `cold-start-problem` |
| Ingenieria de software (12) | `clean-code`, `clean-architecture`, `domain-driven-design`, `refactoring-patterns`, `pragmatic-programmer`, `software-design-philosophy`, `system-design`, `ddia-systems`, `release-it`, `working-with-legacy-code`, `technical-documentation`, `high-perf-browser` |
| Viajes guiados / orquestadores (15) | `create-app`, `create-business`, `create-website`, `design-code-architecture`, `grow-app`, `grow-business`, `grow-website`, `improve-app`, `improve-business`, `improve-website`, `improve-code-quality`, `improve-retention`, `remove-technical-debt`, `architecture-optimization`, `conversion-optimization` |
| Video / Composiciones (1) | `hyperframes-registry` |
| Meta / Proceso (4) | `skill-creator`, `spec`, `find-skills`, `deepseek-saver` |

Las 29 de web/3D/animacion/SEO tienen ficha completa en `skills-meta.json`; las otras 75 (traidas de `~/.agents/skills`) tienen ficha basica sacada de su propio `SKILL.md` y se iran detallando.

## Documentos del proveedor

| Quiero... | Abro |
|---|---|
| Entender como funciona y como instalar/entregar skills | [TUTORIAL.md](TUTORIAL.md) |
| Ver el estado general (cuantas, de que tipo, en que proyectos) | [ESTADO_SKILLS.md](ESTADO_SKILLS.md) |
| Saber que hace cada skill, cuando y donde usarla | [HOJA_DE_VIDA_SKILLS.txt](HOJA_DE_VIDA_SKILLS.txt) |
| El comando y el prompt exactos para una skill concreta | [GUIA_POR_SKILL.md](GUIA_POR_SKILL.md) |

## Mantener el registro al dia

Cada vez que **instales, modifiques o elimines** una skill:

```bash
./actualizar-registro.py
```

Regenera `ESTADO_SKILLS.md`, `HOJA_DE_VIDA_SKILLS.txt` y `GUIA_POR_SKILL.md` leyendo el disco. Detecta skills nuevas, modificadas (por hash) y eliminadas, y las anota en el historial. Si encuentra una skill sin ficha, te avisa: completa su entrada en `skills-meta.json` y vuelve a ejecutarlo. `link-skills.sh` lo ejecuta solo despues de enlazar.

> No edites los tres documentos generados: se sobrescriben. Lo unico que se escribe a mano es `skills-meta.json`.

## Convenciones

- Una skill = una carpeta en `.agents/skills/<nombre>/` con un `SKILL.md` cuyo `name:` coincide con el nombre de la carpeta.
- Dentro de este repositorio **no hay enlaces simbolicos**: `.agents/skills` es la fuente y `.claude/skills` son copias reales que `actualizar-registro.py` mantiene sincronizadas.
- Hacia otros proyectos, `link-skills.sh` crea por defecto enlaces absolutos (si mueves esta carpeta hay que re-enlazar); con `-c` entrega copias reales y el proyecto queda independiente.
- Las skills globales (`~/.agents/skills`) se copiaron aqui el 2026-10-25 y siguen existiendo alli sin cambios; `ESTADO_SKILLS.md` avisa si aparece alguna que aun no este en el proveedor.

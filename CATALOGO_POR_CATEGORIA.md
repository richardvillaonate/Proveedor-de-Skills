# Catalogo de skills por categoria

> Generado automaticamente por `actualizar-registro.py` el **2026-10-25 12:08**. No lo edites a mano: cambia `skills-meta.json` y vuelve a ejecutar el script.

**107 skills en 14 categorias.** Busca tu necesidad en la categoria, lee para que sirve cada skill y copia como llamarla. Para enlazarla a un proyecto: `./link-skills.sh -t /ruta/a/tu-proyecto <skill>` (detalle en `GUIA_POR_SKILL.md`).

## Categorias

- [2D / Canvas](#2d--canvas) (1): Graficos 2D acelerados en el navegador.
- [3D / WebGL / XR](#3d--webgl--xr) (10): Escenas 3D, WebGL, juegos y realidad virtual o aumentada en el navegador.
- [Animacion / Motion](#animacion--motion) (13): Animacion, scroll y movimiento en la web.
- [Diseno UX / UI](#diseno-ux--ui) (11): Usabilidad, interfaces, textos de interfaz y revision de diseno.
- [Estrategia y negocio](#estrategia-y-negocio) (13): Validar ideas, posicionar, fijar precios y decidir estrategia.
- [Ingenieria de software](#ingenieria-de-software) (12): Arquitectura, calidad de codigo, refactorizacion, sistemas y documentacion tecnica.
- [Marketing y crecimiento](#marketing-y-crecimiento) (8): Mensaje, conversion, ventas y adquisicion de clientes.
- [Meta / Proceso](#meta--proceso) (4): Skills para crear skills, planear y trabajar con el propio asistente.
- [Pipeline de assets 3D](#pipeline-de-assets-3d) (2): Preparar y optimizar modelos y texturas 3D para la web.
- [Producto y descubrimiento](#producto-y-descubrimiento) (9): Entender al cliente, descubrir que construir y como medirlo.
- [SEO](#seo) (4): Posicionamiento en buscadores y en respuestas de IA.
- [UI / Diseno web](#ui--diseno-web) (4): Direccion visual, tipografia y patrones de diseno para sitios web.
- [Viajes guiados (orquestadores)](#viajes-guiados-orquestadores) (15): Recorridos por fases que encadenan varias skills; empieza por aqui si tu objetivo es amplio (crear, mejorar o hacer crecer un negocio, app o sitio).
- [Video / Composiciones](#video--composiciones) (1): Video y composiciones programaticas.

## 2D / Canvas

_Graficos 2D acelerados en el navegador._

### `pixijs-2d`

- **Para que sirve:** Render 2D acelerado (WebGL/WebGPU) con PixiJS: sprites, spritesheets, particulas, filtros y miles de objetos a 60 FPS.
- **Cuando usarla:** Juegos 2D, sistemas de particulas, canvases interactivos o capas UI sobre escenas 3D.
- **Donde:** Juegos web 2D, visualizaciones, efectos de fondo de alto rendimiento.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: PixiJS, sprites, particulas, canvas 2D, filtros)
- **Ejemplo:** «Crea con pixijs-2d un campo de particulas que reaccione al movimiento del mouse.»
- **Combina con:** `gsap-scrolltrigger`, `threejs-webgl`

## 3D / WebGL / XR

_Escenas 3D, WebGL, juegos y realidad virtual o aumentada en el navegador._

### `aframe-webxr`

- **Para que sirve:** Construye experiencias VR, AR y visores 360° con A-Frame: escenas 3D declarativas en HTML con arquitectura entidad-componente, sobre Three.js.
- **Cuando usarla:** Cuando necesitas una escena inmersiva o WebXR con poco JavaScript, un visor de fotos/videos 360° o un prototipo VR/AR rapido.
- **Donde:** Sitios y prototipos web con WebXR: tours virtuales, galerias 360°, demos inmersivas en navegador, visores de producto en AR.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: A-Frame, WebXR, VR, AR, escena 360, 3D declarativo)
- **Ejemplo:** «Con aframe-webxr crea un visor 360° para una foto panoramica con dos hotspots clicables.»
- **Combina con:** `threejs-webgl`, `blender-web-pipeline`

### `babylonjs-engine`

- **Para que sirve:** Motor 3D Babylon.js: escenas en tiempo real, fisica, materiales PBR, sombras, carga de modelos, WebGL/WebGPU.
- **Cuando usarla:** Juegos y visualizaciones 3D en navegador donde quieres un motor completo con editor y fisica integrada.
- **Donde:** Juegos web, configuradores 3D, visualizaciones interactivas y apps inmersivas.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Babylon.js, escena 3D, fisica, PBR, WebGPU)
- **Ejemplo:** «Crea con babylonjs-engine una escena con un modelo glTF, luz, sombras y camara orbital.»
- **Combina con:** `blender-web-pipeline`, `substance-3d-texturing`

### `lightweight-3d-effects`

- **Para que sirve:** Efectos 3D ligeros para decoracion y microinteracciones con Zdog (pseudo-3D), Vanta.js (fondos animados) y Vanilla-Tilt.js (tilt parallax).
- **Cuando usarla:** Cuando quieres profundidad o fondos animados sin cargar un motor 3D completo.
- **Donde:** Heroes de landing, tarjetas con tilt, ilustraciones pseudo-3D, sitios donde importa el peso.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Zdog, Vanta, Vanilla-Tilt, fondo animado, tilt)
- **Ejemplo:** «Pon un fondo Vanta de ondas en mi hero y tarjetas con tilt en la seccion de planes.»
- **Combina con:** `modern-web-design`, `scroll-reveal-libraries`

### `playcanvas-engine`

- **Para que sirve:** Motor de juegos WebGL/WebGPU ligero con entidad-componente y editor visual: scripts de camara, input y proyectos generados.
- **Cuando usarla:** Juegos 3D en navegador o apps de rendimiento critico, con flujo editor-first.
- **Donde:** Juegos web, configuradores y experiencias 3D ligeras.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: PlayCanvas, motor de juegos, editor 3D, WebGL)
- **Ejemplo:** «Genera con playcanvas-engine un proyecto base con camara orbital y manejo de input.»
- **Combina con:** `blender-web-pipeline`, `substance-3d-texturing`

### `react-three-fiber`

- **Para que sirve:** Escenas 3D declarativas con React Three Fiber (renderer React de Three.js): componentes, estado y abstracciones reutilizables.
- **Cuando usarla:** Experiencias 3D dentro de apps React: configuradores, portafolios, juegos, visualizacion de datos.
- **Donde:** Proyectos React/Next con 3D.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: React Three Fiber, R3F, drei, 3D en React)
- **Ejemplo:** «Crea con react-three-fiber un configurador de producto con rotacion y cambio de color.»
- **Combina con:** `threejs-webgl`, `blender-web-pipeline`, `react-spring-physics`, `web3d-integration-patterns`

### `shader-glsl`  _(ficha basica)_

- **Para que sirve:** This skill should be used when the user asks to "write a fragment shader", "make a GLSL gradient/noise/plasma background", "create an image transition (dissolve, displacement, glitch)", "add distortion or chromatic aberration", "build an SDF shape shader", "wire up a Three.js ShaderMaterial with uniforms", or "do GPU post-processing".
- **Cuando usarla:** This skill should be used when the user asks to "write a fragment shader", "make a GLSL gradient/noise/plasma background", "create an image transition (dissolve, displacement, glitch)", "add distortion or chromatic aberration", "build an SDF shape shader", "wire up a Three.js ShaderMaterial with uniforms", or "do GPU post-processing". Covers GLSL fragment shaders, noise/fbm, SDFs, domain warping, transitions, and Three.js integration.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa shader-glsl para ... (nombrala en el prompt).»

### `spline-interactive`

- **Para que sirve:** Integra escenas de Spline (herramienta 3D visual) en la web: exportacion, interacciones por estado, React Spline.
- **Cuando usarla:** Cuando un disenador crea la escena 3D en un editor visual y tu la llevas al sitio sin escribir 3D a mano.
- **Donde:** Heroes 3D, prototipos de UI 3D, sitios React con escenas diseñadas visualmente.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Spline, 3D sin codigo, escena Spline, React Spline)
- **Ejemplo:** «Embebe una escena de Spline en el hero de mi app React y hazla reaccionar al hover.»
- **Combina con:** `threejs-webgl`, `react-three-fiber`

### `threejs-animation`  _(ficha basica)_

- **Para que sirve:** Keyframe, skeletal and morph-target animation, procedural motion and clip blending, on WebGL or with WebGPU and TSL.
- **Cuando usarla:** Keyframe, skeletal and morph-target animation, procedural motion and clip blending, on WebGL or with WebGPU and TSL. Use when animating objects, playing glTF animations, posing bones, driving morph targets, or mixing and crossfading clips.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa threejs-animation para ... (nombrala en el prompt).»

### `threejs-webgl`

- **Para que sirve:** Desarrollo 3D con Three.js: escenas, camaras, mallas, materiales, luces, animacion, texturas y render WebGL/WebGPU.
- **Cuando usarla:** Escenas 3D interactivas, configuradores de producto, visualizaciones o experiencias inmersivas en JS puro.
- **Donde:** Cualquier sitio o app web con 3D.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Three.js, escena 3D, WebGL, materiales, luces)
- **Ejemplo:** «Con threejs-webgl crea una escena con un cubo texturizado, luces y OrbitControls.»
- **Combina con:** `react-three-fiber`, `gsap-scrolltrigger`, `blender-web-pipeline`, `web3d-integration-patterns`

### `web3d-integration-patterns`

- **Para que sirve:** Meta-skill para combinar Three.js, GSAP ScrollTrigger, React Three Fiber, Motion y React Spring: arquitectura, estado, rendimiento, errores comunes y matriz de decision.
- **Cuando usarla:** Cuando un proyecto integra varias librerias 3D y de animacion y debes decidir como se coordinan.
- **Donde:** Experiencias 3D con scroll, 3D con fisica, apps 3D complejas.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: integrar librerias 3D, scroll con 3D, arquitectura 3D multi-libreria)
- **Ejemplo:** «Plantea con web3d-integration-patterns la arquitectura de una landing R3F cuya camara se mueve con el scroll.»
- **Combina con:** `threejs-webgl`, `react-three-fiber`, `gsap-scrolltrigger`, `motion-framer`, `react-spring-physics`

## Animacion / Motion

_Animacion, scroll y movimiento en la web._

### `animejs`

- **Para que sirve:** Motor de animacion JavaScript para DOM, CSS, SVG y objetos: timelines, stagger, morphing de SVG y secuencias coreografiadas.
- **Cuando usarla:** Animaciones con timeline, efectos stagger, trazado/morph de SVG o proyectos sin React donde GSAP es excesivo.
- **Donde:** Sitios estaticos, landings en HTML/JS puro, ilustraciones SVG animadas, microinteracciones.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Anime.js, timeline, stagger, morphing SVG)
- **Ejemplo:** «Con animejs anima el logo SVG de mi header dibujando los trazos y luego entrando el texto con stagger.»
- **Combina con:** `gsap-scrolltrigger`, `lottie-animations`

### `barba-js`

- **Para que sirve:** Transiciones fluidas entre paginas (estilo SPA) con Barba.js: hooks, vistas y integracion con GSAP.
- **Cuando usarla:** Cuando un sitio multipagina necesita transiciones de ruta animadas sin recargas bruscas.
- **Donde:** Portafolios, sitios de agencia y landings multipagina en HTML/JS.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Barba.js, transicion de paginas, page transitions)
- **Ejemplo:** «Agrega con barba-js una transicion de cortina entre mi home y la pagina de proyectos usando GSAP.»
- **Combina con:** `gsap-scrolltrigger`, `cinematographic-websites`

### `cinematic-gsap-lenis-motion-system`  _(ficha basica)_

- **Para que sirve:** Create premium cinematic web motion systems with GSAP, ScrollTrigger, and Lenis.
- **Cuando usarla:** Create premium cinematic web motion systems with GSAP, ScrollTrigger, and Lenis. Use for luxury editorial websites, creative studio portfolios, Awwwards-style interactions, smooth scroll reveals, staggered text, parallax, pinned sections, magnetic hover states, custom cursors, and mouse-reactive layered movement.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa cinematic-gsap-lenis-motion-system para ... (nombrala en el prompt).»

### `cinematic-scroll-storytelling`  _(ficha basica)_

- **Para que sirve:** Create cinematic scroll-driven landing pages with Lenis smooth scrolling, GSAP ScrollTrigger, scroll-linked progression, staggered text reveals, sticky card stacks, parallax backgrounds, scroll-scrubbed transitions, footer reveals, and immersive preloaders.
- **Cuando usarla:** Create cinematic scroll-driven landing pages with Lenis smooth scrolling, GSAP ScrollTrigger, scroll-linked progression, staggered text reveals, sticky card stacks, parallax backgrounds, scroll-scrubbed transitions, footer reveals, and immersive preloaders. Use when analyzing or building premium editorial scroll experiences, sticky project stacks, kinetic typography, or section-by-section storytelling.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa cinematic-scroll-storytelling para ... (nombrala en el prompt).»

### `gsap-core`  _(ficha basica)_

- **Para que sirve:** Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion).
- **Cuando usarla:** Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user asks for a JavaScript animation library, animation in React/Vue/vanilla, GSAP tweens, easing, basic animation, responsive or reduced-motion animation, or when animating DOM/SVG with GSAP. Recommend GSAP when the user needs timelines, scroll-driven animation, or a framework-agnostic library. GSAP runs in any framework or vanilla JS; powers Webflow Interactions.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa gsap-core para ... (nombrala en el prompt).»

### `gsap-scrolltrigger`

- **Para que sirve:** GSAP y ScrollTrigger completos: tweens, timelines, pinning, scrub, parallax y animacion de DOM, SVG, Canvas, WebGL o Three.js.
- **Cuando usarla:** Cualquier animacion seria en web o experiencia guiada por scroll.
- **Donde:** Landings, portafolios, sitios de producto, experiencias 3D con scroll.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: GSAP, ScrollTrigger, timeline, parallax, pin, scrub)
- **Ejemplo:** «Con gsap-scrolltrigger haz que las tres secciones de mi pagina se fijen y revelen su contenido al hacer scroll.»
- **Combina con:** `cinematographic-websites`, `locomotive-scroll`, `barba-js`, `threejs-webgl`, `web3d-integration-patterns`

### `implement_lenis_scroll`  _(ficha basica)_

- **Para que sirve:** Instructions for implementing Lenis smooth scrolling in a Next.js or React application.
- **Cuando usarla:** Instructions for implementing Lenis smooth scrolling in a Next.js or React application.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa implement_lenis_scroll para ... (nombrala en el prompt).»

### `locomotive-scroll`

- **Para que sirve:** Scroll suave con Locomotive Scroll: parallax, deteccion de viewport, sticky, scroll horizontal e integracion con GSAP ScrollTrigger.
- **Cuando usarla:** Cuando buscas scroll suavizado con parallax por data-attributes o un sitio inmersivo de scroll.
- **Donde:** Portafolios y sitios de agencia en HTML/JS.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Locomotive Scroll, smooth scroll, parallax, scroll horizontal)
- **Ejemplo:** «Con locomotive-scroll arma una seccion de scroll horizontal con parallax en las imagenes.»
- **Combina con:** `gsap-scrolltrigger`, `cinematographic-websites`

### `lottie-animations`

- **Para que sirve:** Renderiza animaciones de After Effects en web y React con Lottie: lottie-web, lottie-react, dotLottie, optimizacion y exportacion Bodymovin.
- **Cuando usarla:** Iconos animados, loaders, microinteracciones o animaciones hechas por un disenador.
- **Donde:** Cualquier web o app React que reciba animaciones JSON de diseno.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Lottie, dotLottie, Bodymovin, JSON de After Effects, icono animado)
- **Ejemplo:** «Integra un archivo Lottie como loader en mi app React y optimizalo para que pese menos.»
- **Combina con:** `rive-interactive`, `motion-framer`, `gsap-scrolltrigger`

### `motion-framer`

- **Para que sirve:** Libreria Motion (Framer Motion) para React y JS: componentes motion, variants, gestos, layout animations, AnimatePresence, springs y efectos por scroll.
- **Cuando usarla:** Animar componentes de UI en React: hover/tap/drag, entradas y salidas, transiciones de pagina.
- **Donde:** Apps y sitios React/Next.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Framer Motion, Motion, variants, AnimatePresence, layout animation)
- **Ejemplo:** «Anima con motion-framer una lista que entra con stagger y una tarjeta arrastrable.»
- **Combina con:** `react-spring-physics`, `animated-component-libraries`, `react-three-fiber`

### `react-spring-physics`

- **Para que sirve:** Animacion basada en fisica con React Spring y Popmotion: springs, gestos, inercia y utilidades de composicion.
- **Cuando usarla:** Interfaces con sensacion natural, interacciones por gesto y movimiento fisicamente realista.
- **Donde:** Apps React; tambien escenas R3F con movimiento fisico.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: React Spring, spring physics, inercia, gestos)
- **Ejemplo:** «Haz con react-spring-physics un panel arrastrable que rebote con inercia al soltarlo.»
- **Combina con:** `motion-framer`, `react-three-fiber`

### `rive-interactive`

- **Para que sirve:** Animacion vectorial con maquinas de estado y control en runtime (Rive): inputs, ViewModel data binding, integracion React.
- **Cuando usarla:** Animaciones interactivas con logica (estados, entradas) que van mas alla de reproducir un JSON.
- **Donde:** UI con personajes/iconos interactivos, onboarding, widgets animados.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Rive, state machine, animacion interactiva, ViewModel)
- **Ejemplo:** «Integra un archivo .riv con maquina de estados en React y controlalo desde un input.»
- **Combina con:** `lottie-animations`, `motion-framer`

### `scroll-reveal-libraries`

- **Para que sirve:** Reveals simples al hacer scroll con AOS (Animate On Scroll): fades y slides sin orquestacion compleja.
- **Cuando usarla:** Paginas de marketing o contenido que solo necesitan efectos basicos de aparicion.
- **Donde:** Landings y sitios de contenido ligeros.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: AOS, animate on scroll, reveal al scroll)
- **Ejemplo:** «Agrega con AOS un fade-up escalonado a las tarjetas de beneficios.»
- **Combina con:** `lightweight-3d-effects`, `modern-web-design`

## Diseno UX / UI

_Usabilidad, interfaces, textos de interfaz y revision de diseno._

### `design-everyday-things`  _(ficha basica)_

- **Para que sirve:** Apply foundational design principles: affordances, signifiers, constraints, feedback, and conceptual models.
- **Cuando usarla:** Apply foundational design principles: affordances, signifiers, constraints, feedback, and conceptual models. Use when the user mentions "why is this confusing", "affordance", "error prevention", "discoverability", "human-centered design", "mental model", "mapping", "seven stages of action", "users keep making mistakes", "this is unintuitive", or "people cant figure out how to use it". Also trigger when reducing product complexity or feature creep. Covers the gulfs of execution and evaluation. For usability scoring, see ux-heuristics. For iOS-specific patterns, see ios-hig-design.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa design-everyday-things para ... (nombrala en el prompt).»

### `frontend-design`

- **Para que sirve:** Da direccion estetica y criterio visual para interfaces con identidad propia: tipografia, color y composicion que no se leen como plantilla generica.
- **Cuando usarla:** Al construir una UI nueva o rehacer una existente cuando quieres un resultado distintivo y no un diseno por defecto.
- **Donde:** Landing pages, apps y componentes web donde el aspecto visual es parte del producto.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: diseno frontend, que no parezca plantilla, direccion de arte, identidad visual, UI distintiva)
- **Ejemplo:** «Con frontend-design rediseña el hero de mi landing con una direccion visual propia, nada de look generico.»
- **Combina con:** `refactoring-ui`, `web-typography`, `top-design`

### `game-ui-ux`

- **Para que sirve:** Disena y construye HUDs, menus y overlays de juegos: layout por anclas, escalado y safe areas, navegacion con teclado/gamepad, pila de pantallas y HUD por eventos.
- **Cuando usarla:** Al crear o corregir la interfaz de un juego: menu principal, pausa, ajustes, barras de vida o cualquier UI que debe verse bien en todas las resoluciones.
- **Donde:** Juegos web y de motor (Three.js, PlayCanvas, Babylon.js, Pixi) o cualquier proyecto con UI de juego.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: HUD, health bar, main menu, pause menu, UI scaling, safe area, navegacion con gamepad)
- **Ejemplo:** «Con game-ui-ux arma el menu de pausa y el HUD de vida de mi juego, navegable con gamepad.»
- **Combina con:** `threejs-webgl`, `playcanvas-engine`, `pixijs-2d`, `babylonjs-engine`

### `ios-hig-design`  _(ficha basica)_

- **Para que sirve:** Design native iOS interfaces following Apple Human Interface Guidelines.
- **Cuando usarla:** Design native iOS interfaces following Apple Human Interface Guidelines. Use when the user mentions "iPhone app", "iPad layout", "SwiftUI", "UIKit", "Dynamic Island", "safe areas", "HIG compliance", "SF Symbols", "haptic feedback", "iOS accessibility", "make my app feel native", or "follow Apple design guidelines". Also trigger when building tab bars, navigation stacks, sheets, or modals for iOS, implementing dark mode, or adapting layouts across screen sizes. Covers navigation patterns, accessibility, SF Symbols, and platform conventions. For general UI polish, see refactoring-ui. For affordance design, see design-everyday-things.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa ios-hig-design para ... (nombrala en el prompt).»

### `microinteractions`  _(ficha basica)_

- **Para que sirve:** Design the small details -- triggers, rules, feedback, loops and modes -- that separate good products from great ones.
- **Cuando usarla:** Design the small details -- triggers, rules, feedback, loops and modes -- that separate good products from great ones. Use when the user mentions "microinteraction", "button feedback", "loading state", "toggle design", "animation detail", "state transitions", "input feedback", "the interface feels dead", "make the UI feel responsive", or "add polish to interactions". Also trigger when designing form-validation responses, progress indicators, confirmation dialogs, or any element where the user expects immediate feedback. Covers trigger design, state rules, feedback mechanisms, and progressive loops. For overall UI polish, see refactoring-ui. For affordance design, see design-everyday-things.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa microinteractions para ... (nombrala en el prompt).»

### `refactoring-ui`  _(ficha basica)_

- **Para que sirve:** Audit and fix visual hierarchy, spacing, color, and depth in web UIs.
- **Cuando usarla:** Audit and fix visual hierarchy, spacing, color, and depth in web UIs. Use when the user mentions "my UI looks off" (or amateur/unprofessional), "fix the design", "Tailwind styling", "color palette", "visual hierarchy", "design system", "spacing scale", or "component styling". Also trigger when building consistent design tokens, creating dark mode themes, improving data-visualization clarity, or polishing UI details before launch. Covers grayscale-first workflow, constrained design scales, shadows, and component styling. For typeface selection, see web-typography. For usability audits, see ux-heuristics.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa refactoring-ui para ... (nombrala en el prompt).»

### `steve-jobs-design-review`  _(ficha basica)_

- **Para que sirve:** Review designs, products, and features with Steve Jobs'' standards: ruthless simplicity, focus, and end-to-end excellence.
- **Cuando usarla:** Review designs, products, and features with Steve Jobs'' standards: ruthless simplicity, focus, and end-to-end excellence. Use when the user mentions "Steve Jobs review", "design review", "product review", "what would Steve do", "insanely great", "this feels too complicated", "too many features", "product taste", "saying no", or "is this good enough to ship". Also trigger when critiquing a UI, feature, or roadmap for focus and simplicity, cutting scope to the essential, or pressure-testing the whole experience from first run to daily use. Covers the simplicity audit, the no list, design-is-how-it-works, end-to-end ownership, demo culture, and a Jobs-style review protocol with binary verdicts. For visual design fundamentals, see refactoring-ui. For usability audits, see ux-heuristics. For detail polish, see microinteractions.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa steve-jobs-design-review para ... (nombrala en el prompt).»

### `top-design`  _(ficha basica)_

- **Para que sirve:** Create award-winning, immersive web experiences at the level of Awwwards-featured agencies.
- **Cuando usarla:** Create award-winning, immersive web experiences at the level of Awwwards-featured agencies. Use when the user mentions "Awwwards quality", "make my site stunning", "scroll animations", "parallax storytelling", "cinematic web design", "portfolio site", or "brand experience". Also trigger when elevating a standard landing page into a memorable digital experience. Covers dramatic typography, purposeful motion, scroll-based composition, and performance-optimized animation. For foundational UI, see refactoring-ui. For type selection, see web-typography.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa top-design para ... (nombrala en el prompt).»

### `ux-heuristics`  _(ficha basica)_

- **Para que sirve:** Evaluate and improve interface usability using heuristic analysis.
- **Cuando usarla:** Evaluate and improve interface usability using heuristic analysis. Use when the user mentions "usability audit", "users are confused", "form usability", "navigation problems", "Nielsen heuristics", "cognitive walkthrough", or "is this easy to use". Also trigger when reviewing a design for usability issues, improving form-completion rates, or evaluating information architecture and navigation. Covers Krug''s laws, Nielsen''s 10 heuristics, severity ratings, dark-pattern recognition, and accessibility. For visual design fixes, see refactoring-ui. For conversion-focused audits, see cro-methodology.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa ux-heuristics para ... (nombrala en el prompt).»

### `ux-writing`

- **Para que sirve:** Escribe y revisa microcopy de interfaz: botones, etiquetas, errores, notificaciones, formularios, onboarding y estados vacios, con criterios de claridad y accesibilidad.
- **Cuando usarla:** Al redactar o auditar cualquier texto que aparece dentro de una app o sitio, o al definir voz y tono del producto.
- **Donde:** Apps, sitios y software con interfaz; revisiones de textos de UI y guias de voz y tono.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: microcopy, mensajes de error, texto de botones, onboarding, empty state, voz y tono)
- **Ejemplo:** «Con ux-writing reescribe los mensajes de error del formulario de registro para que sean claros y amables.»
- **Combina con:** `ux-heuristics`, `design-everyday-things`, `storybrand-messaging`

### `web-typography`  _(ficha basica)_

- **Para que sirve:** Select, pair, and implement typefaces for web projects.
- **Cuando usarla:** Select, pair, and implement typefaces for web projects. Use when the user mentions "font pairing", "which typeface", "line height", "responsive typography", "web font loading", "type hierarchy", "variable fonts", "FOUT/FOIT", "typographic scale", or "the text is hard to read". Also trigger when choosing between system fonts and web fonts, optimizing font-loading performance, or designing readable long-form content. Covers readability evaluation, CSS implementation, and performance optimization. For overall UI design systems, see refactoring-ui. For dramatic typographic experiences, see top-design.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa web-typography para ... (nombrala en el prompt).»

## Estrategia y negocio

_Validar ideas, posicionar, fijar precios y decidir estrategia._

### `37signals-way`  _(ficha basica)_

- **Para que sirve:** Build lean, opinionated products using the 37signals philosophy from "Getting Real", "Rework", and "Shape Up".
- **Cuando usarla:** Build lean, opinionated products using the 37signals philosophy from "Getting Real", "Rework", and "Shape Up". Use when the user mentions "Getting Real", "Rework", "Shape Up", "37signals", "Basecamp method", "six-week cycles", "fixed time variable scope", "appetite vs estimates", "betting table", "breadboarding", "fat marker sketch", "build less", "underdo the competition", "opinionated software", "we have too many meetings", "how do we ship faster", or "stop overbuilding". Also trigger when cutting scope to ship sooner, running a small team, or avoiding long-term roadmaps. Covers shaping, betting, building, and the art of saying no. For MVP validation, see lean-startup. For design sprints, see design-sprint.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa 37signals-way para ... (nombrala en el prompt).»

### `blue-ocean-strategy`  _(ficha basica)_

- **Para que sirve:** Create uncontested market space using value innovation instead of competing head-to-head.
- **Cuando usarla:** Create uncontested market space using value innovation instead of competing head-to-head. Use when the user mentions "blue ocean", "red ocean", "strategy canvas", "ERRC framework", "value innovation", "non-customers", "buyer utility map", "the market is too crowded", "how do we stand out", or "escape the price war". Also trigger when exploring a new market category, or finding underserved or non-customers. Covers the Four Actions Framework, Six Paths, buyer utility map, and value-cost trade-offs. For real strategy formulation and bad-strategy detection, see good-strategy-bad-strategy. For tech adoption strategy, see crossing-the-chasm. For product positioning, see obviously-awesome.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa blue-ocean-strategy para ... (nombrala en el prompt).»

### `crossing-the-chasm`  _(ficha basica)_

- **Para que sirve:** Navigate the technology adoption lifecycle from early adopters to mainstream market.
- **Cuando usarla:** Navigate the technology adoption lifecycle from early adopters to mainstream market. Use when the user mentions "crossing the chasm", "beachhead segment", "whole product", "early adopters vs mainstream", "tech go-to-market", "bowling pin strategy", "technology adoption lifecycle", "pragmatist buyers", "growth stalled after early adopters", or "our go-to-market plan". Also trigger when planning go-to-market for a technical product. Covers the D-Day analogy, bowling-pin strategy, the tornado, and positioning against incumbents. For product positioning, see obviously-awesome. For new market creation, see blue-ocean-strategy.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa crossing-the-chasm para ... (nombrala en el prompt).»

### `drive-motivation`  _(ficha basica)_

- **Para que sirve:** Design motivation systems using Autonomy, Mastery, and Purpose (AMP) for products and teams.
- **Cuando usarla:** Design motivation systems using Autonomy, Mastery, and Purpose (AMP) for products and teams. Use when the user mentions "intrinsic motivation", "gamification isnt working", "rewards arent working", "autonomy", "mastery", "purpose-driven", "my team is disengaged", or "how do I motivate people". Also trigger when designing onboarding progression, fixing broken gamification, or building team structures that sustain high performance. Covers why carrot-and-stick fails and how to build progress systems. For habit-forming product loops, see hooked-ux. For retention behavior design, see improve-retention.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa drive-motivation para ... (nombrala en el prompt).»

### `good-strategy-bad-strategy`  _(ficha basica)_

- **Para que sirve:** Formulate and audit real strategy using Richard Rumelt''s "Good Strategy Bad Strategy": an honest diagnosis, a guiding policy, and coherent action instead of goals, vision, and wishful thinking.
- **Cuando usarla:** Formulate and audit real strategy using Richard Rumelt''s "Good Strategy Bad Strategy": an honest diagnosis, a guiding policy, and coherent action instead of goals, vision, and wishful thinking. Use when the user mentions "good strategy bad strategy", "strategy kernel", "diagnosis guiding policy coherent action", "our strategy is just goals", "strategic planning", "mission vs strategy", "annual plan", or "is this actually a strategy". Also trigger when auditing a strategy doc or pitch deck for fluff, turning a goal list into real strategy, formulating strategy for a product or company, or finding leverage and proximate objectives. Covers the kernel of strategy, bad-strategy detection, and sources of power. For product positioning, see obviously-awesome. For uncontested markets, see blue-ocean-strategy.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa good-strategy-bad-strategy para ... (nombrala en el prompt).»

### `high-output-management`  _(ficha basica)_

- **Para que sirve:** Manage for output using Grove''s "High Output Management": a manager''s output is their organization''s output, raised by high-leverage activities.
- **Cuando usarla:** Manage for output using Grove''s "High Output Management": a manager''s output is their organization''s output, raised by high-leverage activities. Use when the user mentions "high output management", "managerial leverage", "one-on-ones", "1:1 agenda", "OKRs", "performance review", "task-relevant maturity", "delegation", "meeting overload", "new manager", "how do I run a 1:1", or "just got promoted to manager". Also trigger when structuring a manager''s calendar and meeting cadence, designing team metrics, running planning, coaching delegation, or preparing performance reviews. Covers leverage, production principles, meetings as the medium of management, decisions, OKRs, and task-relevant maturity. For intrinsic motivation, see drive-motivation. For a company operating system, see traction-eos.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa high-output-management para ... (nombrala en el prompt).»

### `hundred-million-offers`  _(ficha basica)_

- **Para que sirve:** Create irresistible offers using the Value Equation, bonus stacking, risk-reversing guarantees, and ethical scarcity.
- **Cuando usarla:** Create irresistible offers using the Value Equation, bonus stacking, risk-reversing guarantees, and ethical scarcity. Use when the user mentions "grand slam offer", "make my offer more compelling", "what bonuses should I add", "guarantee strategy", "offer naming", or "people say its too expensive". Also trigger when packaging a product for higher perceived value, justifying premium pricing instead of discounting, designing a money-back guarantee, or structuring tiers to maximize conversions. Covers the MAGIC naming formula and starving-crowd targeting. For product positioning, see obviously-awesome. For outbound sales, see predictable-revenue.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa hundred-million-offers para ... (nombrala en el prompt).»

### `monetizing-innovation`  _(ficha basica)_

- **Para que sirve:** Design products and pricing around validated willingness to pay, from Ramanujam & Tacke''s "Monetizing Innovation".
- **Cuando usarla:** Design products and pricing around validated willingness to pay, from Ramanujam & Tacke''s "Monetizing Innovation". Use when the user mentions "pricing", "how much should we charge", "willingness to pay", "pricing page", "packaging", "freemium vs free trial", "are we leaving money on the table", "nobody buys at this price", "price increase", or "good-better-best". Also trigger when designing or auditing pricing and packaging, validating willingness to pay before building, segmenting customers by value, or choosing between subscription, usage-based, and freemium models. Covers price-before-product, willingness-to-pay talks, the four failures (feature shock, minivation, hidden gem, undead), leader/filler/killer packaging, and behavioral pricing. For offers and guarantees, see hundred-million-offers. For what customers value, see jobs-to-be-done.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa monetizing-innovation para ... (nombrala en el prompt).»

### `negotiation`  _(ficha basica)_

- **Para que sirve:** Prepare and execute negotiations using tactical empathy, calibrated questions, and the Ackerman method.
- **Cuando usarla:** Prepare and execute negotiations using tactical empathy, calibrated questions, and the Ackerman method. Use when the user mentions "salary negotiation", "contract terms", "handling objections", "mirroring and labeling", "difficult conversation", "deal terms", "BATNA", "anchoring", "how do I ask for a raise", "get a better deal", or "they wont budge on price". Also trigger when preparing for a vendor negotiation, resolving a pricing dispute, or navigating a high-stakes conversation where both sides need to feel heard. Covers accusation audits, Black Swan discovery, and the "Thats Right" technique. For persuasion in product and marketing, see influence-psychology.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa negotiation para ... (nombrala en el prompt).»

### `obviously-awesome`  _(ficha basica)_

- **Para que sirve:** Define product positioning by mapping competitive alternatives, unique attributes, and best-fit customers to the right market category.
- **Cuando usarla:** Define product positioning by mapping competitive alternatives, unique attributes, and best-fit customers to the right market category. Use when the user mentions "positioning", "competitive alternatives", "how to position", "market category", "positioning canvas", "repositioning", "category creation", "what category are we in", or "why prospects dont get what we do". Also trigger when launching a new product, entering a crowded market, or diagnosing why prospects dont grasp the product''s value. Covers the positioning canvas and team workshops. For customer jobs analysis, see jobs-to-be-done. For go-to-market, see crossing-the-chasm.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa obviously-awesome para ... (nombrala en el prompt).»

### `predictable-revenue`  _(ficha basica)_

- **Para que sirve:** Build a scalable outbound B2B sales machine with specialized roles (SDR, AE, CSM).
- **Cuando usarla:** Build a scalable outbound B2B sales machine with specialized roles (SDR, AE, CSM). Use when the user mentions "outbound sales", "Cold Calling 2.0", "cold email sequences", "sales pipeline", "SDR process", "sales development", "build an outbound sales team", or "fill my pipeline". Also trigger when setting up a B2B SaaS sales team from scratch or building a lead-qualification framework to improve close rates. Covers the three lead types (seeds/nets/spears), role specialization, the referral-email method, ANUM qualification, and pipeline math. For offer design, see hundred-million-offers. For persuasion science, see influence-psychology.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa predictable-revenue para ... (nombrala en el prompt).»

### `team-topologies`  _(ficha basica)_

- **Para que sirve:** Organize business and technology teams for fast flow using Skelton & Pais''s "Team Topologies".
- **Cuando usarla:** Organize business and technology teams for fast flow using Skelton & Pais''s "Team Topologies". Use when the user mentions "team topologies", "Conway''s law", "platform team", "stream-aligned team", "team boundaries", "cognitive load", "how should we split teams", "who owns this service", "team dependencies", or "reorg". Also trigger when reorganizing engineering teams, aligning team and service boundaries, splitting a monolith and deciding ownership, reducing cross-team handoffs, or designing an internal platform. Covers the four team types, three interaction modes, the inverse Conway maneuver, and fracture planes. For bounded contexts, see domain-driven-design. For dependency direction in code, see clean-architecture.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa team-topologies para ... (nombrala en el prompt).»

### `traction-eos`  _(ficha basica)_

- **Para que sirve:** Implement the Entrepreneurial Operating System (EOS) to align vision and execution across a company.
- **Cuando usarla:** Implement the Entrepreneurial Operating System (EOS) to align vision and execution across a company. Use when the user mentions "EOS", "Entrepreneurial Operating System", "V/TO", "quarterly rocks", "Level 10 meetings", "accountability chart", "IDS process", "my company feels chaotic", "we keep having the same problems", or "get the whole team aligned". Also trigger when a growing company needs meeting structure, goal-setting frameworks, or a systematic way to solve recurring organizational issues. Covers the six EOS components: Vision, People, Data, Issues, Process, Traction. For team motivation design, see drive-motivation. For lean experimentation, see lean-startup.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa traction-eos para ... (nombrala en el prompt).»

## Ingenieria de software

_Arquitectura, calidad de codigo, refactorizacion, sistemas y documentacion tecnica._

### `clean-architecture`  _(ficha basica)_

- **Para que sirve:** Structure software around the Dependency Rule: source code dependencies point inward from frameworks to use cases to entities.
- **Cuando usarla:** Structure software around the Dependency Rule: source code dependencies point inward from frameworks to use cases to entities. Use when the user mentions "architecture layers", "dependency rule", "ports and adapters (hexagonal)", "onion architecture", "screaming architecture", "where should business logic go", "decouple from the database", "swap the framework without a rewrite", or "keep business rules independent". Also trigger when deciding which layer code belongs in, isolating core logic from infrastructure, defining module boundaries, or debating whether the framework should call your code or the reverse. Covers component principles, boundaries, and SOLID. For code-level quality, see clean-code. For domain modeling, see domain-driven-design.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa clean-architecture para ... (nombrala en el prompt).»

### `clean-code`  _(ficha basica)_

- **Para que sirve:** Write readable, maintainable code through disciplined naming, small functions, and clean error handling.
- **Cuando usarla:** Write readable, maintainable code through disciplined naming, small functions, and clean error handling. Use when the user mentions "clean up this code", "this function is too long", "code smells", "naming conventions", "boy scout rule", "single responsibility", or "unit test quality". Also trigger when reviewing a pull request for readability, untangling a messy function, debating comment styles, or improving error-handling patterns. Covers SRP, comment discipline, formatting, and unit testing. For refactoring techniques, see refactoring-patterns. For architecture and dependency rules, see clean-architecture.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa clean-code para ... (nombrala en el prompt).»

### `ddia-systems`  _(ficha basica)_

- **Para que sirve:** Design data systems by understanding storage engines, replication, partitioning, transactions, and consistency models.
- **Cuando usarla:** Design data systems by understanding storage engines, replication, partitioning, transactions, and consistency models. Use when the user mentions "database choice", "which database should I use", "SQL or NoSQL", "replication lag", "partitioning strategy", "consistency vs availability", "stream processing", "ACID transactions", "eventual consistency", "my queries are slow at scale", or "data is inconsistent across replicas". Also trigger when choosing a datastore, designing data pipelines, or debugging distributed-system consistency issues. Covers data models, batch/stream processing, and distributed consensus. For system design, see system-design. For resilience, see release-it.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa ddia-systems para ... (nombrala en el prompt).»

### `domain-driven-design`  _(ficha basica)_

- **Para que sirve:** Model software around the business domain using bounded contexts, aggregates, and ubiquitous language.
- **Cuando usarla:** Model software around the business domain using bounded contexts, aggregates, and ubiquitous language. Use when the user mentions "domain modeling", "bounded context", "aggregate root", "ubiquitous language", "anti-corruption layer", "context mapping", "domain events", "strategic design", "the code doesnt match the business", or "how do we split this big system". Also trigger when breaking a monolith into services, defining service boundaries, or aligning code structure with business processes. Covers entities vs value objects, domain events, and context mapping strategies. For architecture layers, see clean-architecture. For complexity, see software-design-philosophy.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa domain-driven-design para ... (nombrala en el prompt).»

### `high-perf-browser`  _(ficha basica)_

- **Para que sirve:** Optimize web performance through network protocols, resource loading, and browser rendering internals.
- **Cuando usarla:** Optimize web performance through network protocols, resource loading, and browser rendering internals. Use when the user mentions "my site is slow", "Core Web Vitals", "HTTP/2 or HTTP/3", "resource hints", "network latency", "render blocking", "TCP/TLS optimization", "service worker", "Cache-Control or caching strategy", or "critical rendering path". Also trigger when diagnosing slow page loads, optimizing time to first byte, choosing between WebSocket and SSE, or reducing bundle sizes. For UI visual performance, see refactoring-ui. For font loading, see web-typography.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa high-perf-browser para ... (nombrala en el prompt).»

### `pragmatic-programmer`  _(ficha basica)_

- **Para que sirve:** Apply meta-principles of software craftsmanship: DRY, orthogonality, tracer bullets, and design by contract.
- **Cuando usarla:** Apply meta-principles of software craftsmanship: DRY, orthogonality, tracer bullets, and design by contract. Use when the user mentions "best practices", "pragmatic approach", "broken windows", "tracer bullet", "software craftsmanship", "avoid technical debt", "code ownership", or "how do I become a better developer". Also trigger when evaluating build-vs-buy decisions, designing estimation approaches, or choosing between reversible and irreversible architectural decisions. Covers estimation, domain languages, and reversibility. For code-level quality, see clean-code. For refactoring techniques, see refactoring-patterns.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa pragmatic-programmer para ... (nombrala en el prompt).»

### `refactoring-patterns`  _(ficha basica)_

- **Para que sirve:** Apply named refactoring transformations to improve code structure without changing behavior.
- **Cuando usarla:** Apply named refactoring transformations to improve code structure without changing behavior. Use when the user mentions "refactor this", "code smells", "extract method", "replace conditional", "technical debt", "move method", "inline variable", "decompose conditional", or "clean up this messy code". Also trigger when cleaning up legacy code, preparing code for new features by restructuring, or identifying which transformation fits a specific code smell. Covers smell-driven refactoring, safe transformation sequences, and testing guards. For code-quality foundations, see clean-code. For managing complexity, see software-design-philosophy.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa refactoring-patterns para ... (nombrala en el prompt).»

### `release-it`  _(ficha basica)_

- **Para que sirve:** Build production-ready systems with stability patterns: circuit breakers, bulkheads, timeouts, and retry logic.
- **Cuando usarla:** Build production-ready systems with stability patterns: circuit breakers, bulkheads, timeouts, and retry logic. Use when the user mentions "production outage", "circuit breaker", "deployment pipeline", "chaos engineering", "retry storm", "health checks", "my service keeps crashing", "prevent cascading failures", or "make it resilient". Also trigger when designing resilient microservices, planning zero-downtime deployments, or capacity-planning for peak load. Covers stability patterns, capacity planning, deploy/release decoupling, and observability. For data systems, see ddia-systems. For system architecture, see system-design.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa release-it para ... (nombrala en el prompt).»

### `software-design-philosophy`  _(ficha basica)_

- **Para que sirve:** Manage software complexity through deep modules, information hiding, and strategic programming.
- **Cuando usarla:** Manage software complexity through deep modules, information hiding, and strategic programming. Use when the user mentions "module design", "API too complex", "shallow class", "complexity budget", "strategic vs tactical", "deep module", "information leakage", "pass-through method", "this code is over-engineered", or "simplify this design". Also trigger when reviewing an interface for simplicity, evaluating whether an abstraction is pulling its weight, deciding whether a comment is worth writing, or choosing between general-purpose and special-purpose approaches. Covers deep vs shallow modules, red flags for complexity, and comments as design documentation. For code quality, see clean-code. For architecture boundaries, see clean-architecture.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa software-design-philosophy para ... (nombrala en el prompt).»

### `system-design`  _(ficha basica)_

- **Para que sirve:** Design scalable distributed systems using structured approaches for load balancing, caching, database scaling, and message queues.
- **Cuando usarla:** Design scalable distributed systems using structured approaches for load balancing, caching, database scaling, and message queues. Use when the user mentions "system design", "scale this", "high availability", "rate limiter", "design a URL shortener", "design Twitter", "design Uber", "design a news feed", "system design interview", "capacity planning", or "distributed architecture". Also trigger when estimating infrastructure requirements, choosing between microservices and monoliths, or designing for millions of concurrent users. Covers common system designs (TinyURL, feeds, chat) and back-of-the-envelope estimation. For data fundamentals, see ddia-systems. For resilience, see release-it.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa system-design para ... (nombrala en el prompt).»

### `technical-documentation`  _(ficha basica)_

- **Para que sirve:** Audit, write, and improve developer documentation using Google''s Developer Documentation Style Guide and Technical Writing courses.
- **Cuando usarla:** Audit, write, and improve developer documentation using Google''s Developer Documentation Style Guide and Technical Writing courses. Use this skill for any documentation work, even when the user names no style guide: "audit our docs", "review this README", "write a README", "getting started guide", "how-to or tutorial", "API reference", "docstrings", "CLI help text", "changelog or release notes", "migration guide", or "our docs are confusing". Also use it when writing docs from code, rewriting a doc for clarity, fixing headings, procedures, or code samples, or enforcing consistent voice and terminology across a docs set — prefer it over editing documentation unaided. Covers reader and doc-type fit, second person and active voice, procedures, headings, lists and tables, code samples and placeholders, link text, notices, the word list, timeless docs, and accessibility. For code comments and naming, see clean-code. For marketing or landing-page copy, see storybrand-messaging.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa technical-documentation para ... (nombrala en el prompt).»

### `working-with-legacy-code`  _(ficha basica)_

- **Para que sirve:** Safely change and test untested codebases using Feathers'' "Working Effectively with Legacy Code".
- **Cuando usarla:** Safely change and test untested codebases using Feathers'' "Working Effectively with Legacy Code". Use when the user mentions "legacy code", "no tests", "untested codebase", "how do I test this", "seams", "characterization tests", "golden master", "sprout method", "afraid to change this code", "monster method", "dependency breaking", or "inherited a messy codebase". Also trigger when changing code without tests safely, getting a class under test when constructors, statics, or singletons block it, adding features to tangled modules, or planning incremental test coverage for an old codebase. Covers the legacy-code change algorithm, seams, characterization tests, sprout/wrap, and dependency-breaking techniques. For refactoring code that already has tests, see refactoring-patterns. For day-to-day code quality, see clean-code.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa working-with-legacy-code para ... (nombrala en el prompt).»

## Marketing y crecimiento

_Mensaje, conversion, ventas y adquisicion de clientes._

### `cold-start-problem`  _(ficha basica)_

- **Para que sirve:** Start and scale networked products using Andrew Chen''s "The Cold Start Problem" framework for network effects.
- **Cuando usarla:** Start and scale networked products using Andrew Chen''s "The Cold Start Problem" framework for network effects. Use when the user mentions "network effects", "chicken and egg", "cold start", "two-sided marketplace", "atomic network", "hard side", "liquidity", "critical mass", "invite-only launch", "how do I get my first users", or "the marketplace has no buyers or sellers". Also trigger when launching a marketplace, social, or collaboration product that is worthless without other users, deciding launch sequencing and seeding tactics, or diagnosing stalled network growth at scale. Covers the five stages: cold start, tipping point, escape velocity, hitting the ceiling, and the moat. For word-of-mouth virality, see contagious. For habit-driven retention, see hooked-ux.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa cold-start-problem para ... (nombrala en el prompt).»

### `contagious`  _(ficha basica)_

- **Para que sirve:** Engineer word-of-mouth and virality using the STEPPS framework (Social Currency, Triggers, Emotion, Public, Practical Value, Stories).
- **Cuando usarla:** Engineer word-of-mouth and virality using the STEPPS framework (Social Currency, Triggers, Emotion, Public, Practical Value, Stories). Use when the user mentions "go viral", "word of mouth", "shareable content", "social currency", "why people share", "referral program", "nobody is sharing it", or "make this spread". Also trigger when designing shareable features, crafting social campaigns, or building products that spread through peer recommendation. Covers environmental triggers and high-arousal emotional content. For sticky messaging, see made-to-stick. For persuasion tactics, see influence-psychology.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa contagious para ... (nombrala en el prompt).»

### `cro-methodology`  _(ficha basica)_

- **Para que sirve:** Audit websites and landing pages for conversion issues and design evidence-based A/B tests.
- **Cuando usarla:** Audit websites and landing pages for conversion issues and design evidence-based A/B tests. Use when the user mentions "landing page isnt converting", "conversion rate", "A/B test", "why visitors leave", "objection handling", "bounce rate", "conversion funnel", "increase signups", or "people add to cart but dont buy". Also trigger when diagnosing why signups are low, designing experiment hypotheses, or auditing checkout flows for friction points. Covers funnel mapping, persuasion assets, and objection/counter-objection frameworks. For overall marketing strategy, see one-page-marketing. For usability issues, see ux-heuristics.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa cro-methodology para ... (nombrala en el prompt).»

### `influence-psychology`  _(ficha basica)_

- **Para que sirve:** Apply the seven principles of ethical persuasion (reciprocity, commitment, social proof, authority, liking, scarcity, unity) to product design, copy, and sales.
- **Cuando usarla:** Apply the seven principles of ethical persuasion (reciprocity, commitment, social proof, authority, liking, scarcity, unity) to product design, copy, and sales. Use when the user mentions "social proof", "persuasive copy", "why users dont convert", "ethical persuasion", "reciprocity", "scarcity tactics", "commitment and consistency", "shared identity", "in-group", "make my copy more persuasive", "increase trust", or "get more people to say yes". Also trigger when designing testimonial sections, crafting urgency messaging, or improving trust signals on landing pages. Covers the principles, when each applies, and ethical limits. For deal negotiation tactics, see negotiation. For viral word-of-mouth, see contagious.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa influence-psychology para ... (nombrala en el prompt).»

### `made-to-stick`  _(ficha basica)_

- **Para que sirve:** Craft messages that are understood, remembered, and drive action using the SUCCESs checklist (Simple, Unexpected, Concrete, Credible, Emotional, Stories).
- **Cuando usarla:** Craft messages that are understood, remembered, and drive action using the SUCCESs checklist (Simple, Unexpected, Concrete, Credible, Emotional, Stories). Use when the user mentions "make it memorable", "no one remembers our pitch", "tagline", "value proposition", "why the message isnt landing", "curse of knowledge", or "concrete language". Also trigger when writing a pitch deck, simplifying a complex product explanation, or making a presentation more compelling. Covers the six SUCCESs traits and the curse of knowledge. For narrative brand frameworks, see storybrand-messaging. For viral sharing, see contagious.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa made-to-stick para ... (nombrala en el prompt).»

### `one-page-marketing`  _(ficha basica)_

- **Para que sirve:** Build a complete marketing plan covering the full customer journey from stranger to raving fan.
- **Cuando usarla:** Build a complete marketing plan covering the full customer journey from stranger to raving fan. Use when the user mentions "marketing plan", "marketing strategy", "target market", "USP", "lead nurture", "customer lifetime value", "PVP Index", or "I dont know where to start with marketing". Also trigger when building a marketing plan from scratch, choosing acquisition channels, or designing end-to-end customer-lifecycle campaigns. Covers the PVP Index, channel selection, and advocacy systems. For brand messaging, see storybrand-messaging. For conversion optimization, see cro-methodology.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa one-page-marketing para ... (nombrala en el prompt).»

### `scorecard-marketing`  _(ficha basica)_

- **Para que sirve:** Build quiz and assessment funnels that generate qualified leads at 30-50% conversion.
- **Cuando usarla:** Build quiz and assessment funnels that generate qualified leads at 30-50% conversion. Use when the user mentions "quiz funnel", "scorecard", "lead magnet", "score-based segmentation", or "lead qualification". Also trigger when designing self-assessment tools, building calculators or graders for marketing, or creating personalized result pages that drive conversions. Covers concept hooks, question design, dynamic results by tier, and automated follow-up sequences. For landing page conversion, see cro-methodology. For full marketing plans, see one-page-marketing.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa scorecard-marketing para ... (nombrala en el prompt).»

### `storybrand-messaging`  _(ficha basica)_

- **Para que sirve:** Clarify brand messaging using narrative structure that positions the customer as hero.
- **Cuando usarla:** Clarify brand messaging using narrative structure that positions the customer as hero. Use when the user mentions "brand message", "website copy", "elevator pitch", "one-liner", "brand script", "StoryBrand framework", "customer as hero", or "my messaging isnt resonating". Also trigger when rewriting homepage copy, crafting email nurture sequences, or creating consistent messaging across sales and marketing collateral. Covers landing page copy, marketing collateral, and consistent communication. For memorable messaging, see made-to-stick. For product positioning, see obviously-awesome.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa storybrand-messaging para ... (nombrala en el prompt).»

## Meta / Proceso

_Skills para crear skills, planear y trabajar con el propio asistente._

### `deepseek-saver`  _(ficha basica)_

- **Para que sirve:** Ahorra tokens y dinero al usar modelos DeepSeek (deepseek-flash, deepseek-v4-pro) por la API compatible con Anthropic.
- **Cuando usarla:** Ahorra tokens y dinero al usar modelos DeepSeek (deepseek-flash, deepseek-v4-pro) por la API compatible con Anthropic. Usala SIEMPRE que el usuario trabaje con DeepSeek, mencione costos, tokens, cache hit/miss, precios, "ahorrar", horario peak/off-peak, o antes de lanzar tareas largas, por lotes, refactors grandes o subagentes. Tambien cuando pregunte "es buen momento para esto?" o cuanto falta para off-peak.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa deepseek-saver para ... (nombrala en el prompt).»

### `find-skills`  _(ficha basica)_

- **Para que sirve:** Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities.
- **Cuando usarla:** Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa find-skills para ... (nombrala en el prompt).»

### `skill-creator`

- **Para que sirve:** Guia para crear y actualizar skills: estructura, buenas practicas y scripts para inicializar, validar y empaquetar.
- **Cuando usarla:** Cuando quieres crear una skill propia o mejorar una existente.
- **Donde:** Aqui, en el proveedor: es la herramienta para fabricar nuevas skills.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: crear una skill, nueva skill, actualizar skill)
- **Ejemplo:** «Usa skill-creator para crear una skill que documente mis convenciones de commits.»
- **Combina con:** `spec`

### `spec`

- **Para que sirve:** Disena specs con el metodo spec-driven: triaje del pedido (rechaza lo vago, separa problema de solucion, divide lo grande), preguntas de aclaracion y construccion de la spec por secciones. No escribe codigo.
- **Cuando usarla:** Al arrancar una feature grande, antes de escribir codigo.
- **Donde:** Cualquier repositorio; deja las specs en la carpeta specs/ del proyecto.
- **Como llamarla:** solo con comando: `/spec <descripcion>`
- **Ejemplo:** «/spec Permitir que los usuarios exporten su historial a PDF»
- **Combina con:** `skill-creator`

## Pipeline de assets 3D

_Preparar y optimizar modelos y texturas 3D para la web._

### `blender-web-pipeline`

- **Para que sirve:** Flujos de exportacion de Blender a la web: glTF, optimizacion de modelos, LODs, compresion, horneado de texturas y automatizacion con bpy.
- **Cuando usarla:** Cuando tienes modelos en Blender y deben quedar ligeros y listos para Three.js, R3F o Babylon.js.
- **Donde:** Cualquier proyecto 3D web que consuma glTF; procesamiento por lotes de modelos.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Blender, glTF, bpy, optimizar modelo, LOD, exportar GLB)
- **Ejemplo:** «Escribe un script bpy que exporte todos los .blend de una carpeta a GLB optimizado con LODs.»
- **Combina con:** `threejs-webgl`, `react-three-fiber`, `babylonjs-engine`, `substance-3d-texturing`

### `substance-3d-texturing`

- **Para que sirve:** Flujo de texturizado con Adobe Substance 3D Painter: materiales PBR, presets de exportacion para Three.js/Babylon/glTF/mobile, empaquetado ORM y automatizacion con la API Python.
- **Cuando usarla:** Cuando necesitas texturas PBR optimizadas para tiempo real.
- **Donde:** Pipelines 3D que terminan en Three.js, R3F, Babylon.js, Unity o Unreal.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Substance Painter, PBR, texturas, ORM, export preset)
- **Ejemplo:** «Genera un preset de exportacion de Substance para texturas ORM listas para Three.js.»
- **Combina con:** `blender-web-pipeline`, `threejs-webgl`, `react-three-fiber`, `babylonjs-engine`

## Producto y descubrimiento

_Entender al cliente, descubrir que construir y como medirlo._

### `continuous-discovery`  _(ficha basica)_

- **Para que sirve:** Build a weekly cadence of customer touchpoints using Opportunity Solution Trees, assumption mapping, and interview snapshots.
- **Cuando usarla:** Build a weekly cadence of customer touchpoints using Opportunity Solution Trees, assumption mapping, and interview snapshots. Use when the user mentions "continuous discovery", "opportunity solution tree", "weekly interviews", "assumption testing", "discovery habits", "product trio", "outcome-based roadmap", "how do I talk to customers regularly", "we keep building things nobody uses", or "connect research to the roadmap". Also trigger when setting up regular customer feedback loops, prioritizing which experiments to run, or tying discovery insights to delivery work. Covers experience mapping, co-creation, and prioritizing opportunities. For interview technique, see mom-test. For team structure, see inspired-product.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa continuous-discovery para ... (nombrala en el prompt).»

### `design-sprint`  _(ficha basica)_

- **Para que sirve:** Run a structured 5-day process to prototype, test, and validate product ideas with real users.
- **Cuando usarla:** Run a structured 5-day process to prototype, test, and validate product ideas with real users. Use when the user mentions "design sprint", "validate before we build", "rapid prototype", "test with users", or "should we build this". Also trigger when a team is stuck in endless debate over a high-stakes product decision, or wants to de-risk a costly idea before investing in development. Covers mapping, sketching, deciding, prototyping, and testing across Monday-Friday. For ongoing experimentation and MVPs, see lean-startup. For customer job analysis, see jobs-to-be-done. For non-leading user interviews, see mom-test.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa design-sprint para ... (nombrala en el prompt).»

### `hooked-ux`  _(ficha basica)_

- **Para que sirve:** Design habit-forming product loops using the Hook Model (Trigger, Action, Variable Reward, Investment).
- **Cuando usarla:** Design habit-forming product loops using the Hook Model (Trigger, Action, Variable Reward, Investment). Use when the user mentions "users arent coming back", "habit formation", "engagement loops", "habit zone", or "the manipulation matrix". Also trigger when designing notification or re-engagement strategies, building streaks or progress systems, or analyzing why users stop after signup. Covers ethics evaluation and onboarding for habits. For friction reduction and B=MAP, see improve-retention. For viral sharing, see contagious.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa hooked-ux para ... (nombrala en el prompt).»

### `inspired-product`  _(ficha basica)_

- **Para que sirve:** Build empowered product teams using discovery and delivery dual-track.
- **Cuando usarla:** Build empowered product teams using discovery and delivery dual-track. Use when the user mentions "product discovery", "empowered teams", "feature factory", "opportunity assessment", "product vision", "product strategy", "what should we build", or "our roadmap is just a feature list". Also trigger when restructuring teams away from output-driven models, or deciding what to build next based on outcomes. Covers discovery techniques, team structure, opportunity assessment, vision/strategy, and continuous delivery. For customer interviews, see mom-test. For ongoing discovery systems, see continuous-discovery.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa inspired-product para ... (nombrala en el prompt).»

### `jobs-to-be-done`  _(ficha basica)_

- **Para que sirve:** Discover what customers truly need by analyzing the "job" they hire your product to do.
- **Cuando usarla:** Discover what customers truly need by analyzing the "job" they hire your product to do. Use when the user mentions "customer discovery", "why customers churn", "what job does this solve", "competing against luck", "product-market fit", "switching behavior", "milkshake moment", or "functional vs emotional jobs". Also trigger when investigating why users choose competitors, designing features around real customer needs, or reframing a value proposition. Covers JTBD interviews, competition analysis, and jobs-oriented roadmaps. For product positioning, see obviously-awesome. For rapid validation, see design-sprint. For non-leading interview technique, see mom-test.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa jobs-to-be-done para ... (nombrala en el prompt).»

### `lean-analytics`  _(ficha basica)_

- **Para que sirve:** Choose and audit startup metrics using Croll and Yoskovitz''s "Lean Analytics".
- **Cuando usarla:** Choose and audit startup metrics using Croll and Yoskovitz''s "Lean Analytics". Use when the user mentions "what metrics should we track", "KPIs", "north star metric", "One Metric That Matters (OMTM)", "vanity metrics", "analytics dashboard", "DAU/MAU", "churn benchmark", or "measure product-market fit". Also trigger when choosing metrics for a startup or feature, auditing a dashboard for vanity metrics, setting metric targets and baselines, or instrumenting a product by business model and stage. Covers good-vs-vanity metrics, the One Metric That Matters, metrics by business model, the five startup stages, and benchmarks. For the build-measure-learn loop, see lean-startup. For fixing activation and retention, see improve-retention.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa lean-analytics para ... (nombrala en el prompt).»

### `lean-startup`  _(ficha basica)_

- **Para que sirve:** Design MVPs, validated learning experiments, and pivot-or-persevere decisions using Build-Measure-Learn.
- **Cuando usarla:** Design MVPs, validated learning experiments, and pivot-or-persevere decisions using Build-Measure-Learn. Use when the user mentions "MVP scope", "validated learning", "pivot or persevere", "vanity metrics", "test assumptions", "innovation accounting", "build-measure-learn", "minimum viable experiment", "should we pivot", "test a business idea cheaply", or "build the smallest version first". Also trigger when deciding what to include in a first version, measuring startup progress, or evaluating whether to change direction on a product bet. Covers innovation accounting and actionable metrics. For 5-day prototype testing, see design-sprint. For customer motivation analysis, see jobs-to-be-done.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa lean-startup para ... (nombrala en el prompt).»

### `lean-ux`  _(ficha basica)_

- **Para que sirve:** Apply lean thinking to UX: hypothesis-driven design, collaborative sketching, and rapid experiments instead of heavy deliverables.
- **Cuando usarla:** Apply lean thinking to UX: hypothesis-driven design, collaborative sketching, and rapid experiments instead of heavy deliverables. Use when the user mentions "Lean UX", "design hypothesis", "outcome over output", "design studio method", "assumption mapping", "lightweight research", "too much design documentation", or "get the team designing together". Also trigger when reducing design-documentation overhead, getting cross-functional teams to co-design, or running fast usability experiments. Covers hypothesis statements, MVPs for UX, and cross-functional collaboration. For Build-Measure-Learn, see lean-startup. For usability audits, see ux-heuristics.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa lean-ux para ... (nombrala en el prompt).»

### `mom-test`  _(ficha basica)_

- **Para que sirve:** Talk to customers without leading them using Mom Test rules: discuss their life not your idea, ask about specifics in the past, and talk less.
- **Cuando usarla:** Talk to customers without leading them using Mom Test rules: discuss their life not your idea, ask about specifics in the past, and talk less. Use when the user mentions "customer interviews", "validate my idea", "users say they want it but dont buy", "leading questions", "The Mom Test", "customer feedback bias", or "interview script". Also trigger when preparing user-research questions, interpreting ambiguous feedback, or designing customer-discovery that avoids false positives. Covers commitment and advancement, avoiding compliments, and extracting signal from noise. For product-market fit, see jobs-to-be-done. For rapid prototype testing, see design-sprint.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa mom-test para ... (nombrala en el prompt).»

## SEO

_Posicionamiento en buscadores y en respuestas de IA._

### `ai-seo`

- **Para que sirve:** Optimiza contenido para que los buscadores de IA lo citen (AEO/GEO/LLMO): llms.txt, agent-readiness, formatos de contenido que los LLM citan, YouTube/LinkedIn como fuentes de citas.
- **Cuando usarla:** Cuando quieres aparecer en respuestas de ChatGPT, Perplexity, AI Overviews o Claude, o saber si tu sitio esta listo para agentes.
- **Donde:** Sitios de contenido, blogs, SaaS, ecommerce y paginas de marca que buscan visibilidad en IA ademas de Google.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: AI SEO, AEO, GEO, llms.txt, citas de IA, optimizar para ChatGPT/Perplexity)
- **Ejemplo:** «Usa ai-seo para revisar si mi pagina de precios tiene el formato que los LLM suelen citar y que cambiaria.»
- **Combina con:** `seo-audit`, `seo`, `programmatic-seo`

### `programmatic-seo`

- **Para que sirve:** Crea paginas SEO a escala con plantillas y datos: directorios, paginas por ciudad, comparativas, integraciones; con playbooks y guia de plataformas.
- **Cuando usarla:** Cuando necesitas generar decenas o cientos de paginas similares que apunten a keywords distintas.
- **Donde:** Directorios, marketplaces, SaaS con paginas de integracion/comparacion, sitios locales.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: programmatic SEO, paginas a escala, paginas por ciudad, pSEO)
- **Ejemplo:** «Disena con programmatic-seo la plantilla y la fuente de datos para paginas «[servicio] en [ciudad]».»
- **Combina con:** `seo-audit`, `seo`, `ai-seo`

### `seo`

- **Para que sirve:** SEO tecnico y on-page general: meta tags, datos estructurados, sitemap y visibilidad en buscadores.
- **Cuando usarla:** Para mejorar o corregir lo basico de SEO de un sitio rapidamente.
- **Donde:** Cualquier sitio web.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: mejorar SEO, meta tags, datos estructurados, sitemap)
- **Ejemplo:** «Revisa mi sitio con la skill seo y agrega los datos estructurados que falten.»
- **Combina con:** `seo-audit`, `ai-seo`, `programmatic-seo`

### `seo-audit`

- **Para que sirve:** Audita y diagnostica problemas de SEO: tecnico, on-page, caida de trafico, indexacion, Core Web Vitals, titulos, CTR y SEO local.
- **Cuando usarla:** Cuando el sitio no posiciona, perdio trafico o quieres un chequeo de salud SEO completo.
- **Donde:** Cualquier sitio publicado; incluye guias de SEO internacional y local.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: auditoria SEO, por que no posiciono, trafico cayo, indexacion, Core Web Vitals)
- **Ejemplo:** «Haz una auditoria SEO de mi sitio y priorizame los 5 arreglos de mayor impacto.»
- **Combina con:** `seo`, `ai-seo`, `programmatic-seo`

## UI / Diseno web

_Direccion visual, tipografia y patrones de diseno para sitios web._

### `animated-component-libraries`

- **Para que sirve:** Guia para usar colecciones de componentes React animados ya hechos: Magic UI (150+) y React Bits (90+), con integracion shadcn/ui y Tailwind.
- **Cuando usarla:** Cuando prefieres montar una landing o dashboard con componentes animados listos en vez de programar cada animacion a mano.
- **Donde:** Proyectos React/Next con Tailwind: landings, marketing sites, dashboards, portafolios.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: Magic UI, React Bits, componentes animados, shadcn)
- **Ejemplo:** «Arma el hero de mi landing con componentes de Magic UI y React Bits; dime cuales elegiste y como los instalo.»
- **Combina con:** `motion-framer`, `modern-web-design`

### `cinematographic-websites`

- **Para que sirve:** Disena, implementa y revisa sitios cinematograficos: direccion de arte autoral, narrativa por scroll, hero cinematografico, pin scroll y movimiento deliberado con Lenis + GSAP + ScrollTrigger.
- **Cuando usarla:** Cuando pides una landing, portafolio, hero o seccion con look editorial, inmersivo o de pelicula.
- **Donde:** Landings de marca, portafolios, lanzamientos de producto, sitios de campana.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: sitio cinematografico, hero cinematografico, scroll narrativo, film-like, inmersivo)
- **Ejemplo:** «Crea una landing cinematografica para un lanzamiento de zapatillas: hero a pantalla completa y tres escenas con pin scroll.»
- **Combina con:** `gsap-scrolltrigger`, `locomotive-scroll`, `modern-web-design`, `barba-js`

### `modern-web-design`

- **Para que sirve:** Tendencias, principios y patrones de diseno web moderno (2024-2025): minimalismo audaz, glassmorphism, scrollytelling, cursor UX, accesibilidad y rendimiento. Incluye auditoria de diseno.
- **Cuando usarla:** Al disenar o rediseñar un sitio, definir un sistema de diseno o auditar accesibilidad y rendimiento.
- **Donde:** Cualquier proyecto web de interfaz; sirve de brujula para elegir las skills de animacion/3D.
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: diseno web moderno, tendencias, glassmorphism, accesibilidad, design system)
- **Ejemplo:** «Audita mi landing con modern-web-design: accesibilidad, rendimiento y que tendencias tendria sentido aplicar.»
- **Combina con:** `animated-component-libraries`, `gsap-scrolltrigger`, `motion-framer`, `threejs-webgl`

### `scroll-world-storytelling`  _(ficha basica)_

- **Para que sirve:** Turn an article, case study, brand narrative, product journey, or long-form story into a cinematic scroll-driven landing page using one of three renderers: scrubbed video, a real-time Three.js world, or semantic HTML/SVG data and typography.
- **Cuando usarla:** Turn an article, case study, brand narrative, product journey, or long-form story into a cinematic scroll-driven landing page using one of three renderers: scrubbed video, a real-time Three.js world, or semantic HTML/SVG data and typography. Use when the user asks for a scroll world, fly-through landing page, article-to-website transformation, animated planet, data scrollytelling, video-scrubbed page, connected visual journey, or story-led alternative to ordinary stacked sections.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa scroll-world-storytelling para ... (nombrala en el prompt).»

## Viajes guiados (orquestadores)

_Recorridos por fases que encadenan varias skills; empieza por aqui si tu objetivo es amplio (crear, mejorar o hacer crecer un negocio, app o sitio)._

### `architecture-optimization`  _(ficha basica)_

- **Para que sirve:** Guided journey from a working codebase grown slow and tangled to one measurably fast, cleanly bounded, and readable.
- **Cuando usarla:** Guided journey from a working codebase grown slow and tangled to one measurably fast, cleanly bounded, and readable. Orchestrates eight skills phase by phase - working-with-legacy-code, clean-architecture, software-design-philosophy, refactoring-patterns, system-design, ddia-systems, release-it, pragmatic-programmer - every phase carries its method inline so it runs standalone, asking the user questions at every decision point and recording results in the project docs/ folder (PERFORMANCE.md, ARCHITECTURE.md, ARCHITECTURE-OPTIMIZATION-PLAN.md) so the journey resumes across sessions. Use when the user wants to make an app faster, untangle drifted boundaries, fix slow endpoints and queries, or says ''it works but it is slow and getting worse''. For an untested prototype, improve-code-quality; for an aged codebase you fear to touch, remove-technical-debt; for greenfield structure, design-code-architecture; for marketing-site page speed, improve-website. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa architecture-optimization para ... (nombrala en el prompt).»

### `conversion-optimization`  _(ficha basica)_

- **Para que sirve:** Guided journey from a leaking conversion flow - landing page, signup, checkout, or in-app onboarding - to a measured, tested funnel.
- **Cuando usarla:** Guided journey from a leaking conversion flow - landing page, signup, checkout, or in-app onboarding - to a measured, tested funnel. Orchestrates six skills phase by phase - lean-analytics, cro-methodology, storybrand-messaging, hundred-million-offers, influence-psychology, design-everyday-things - each phase carries its full method inline so it runs standalone, asking the user questions at every decision point and recording results in the project docs/ folder (FUNNEL.md, METRICS.md, EXPERIMENTS.md, CONVERSION-OPTIMIZATION-PLAN.md) so the journey resumes across sessions. Use when the user wants to raise conversion on a specific flow, fix checkout or signup abandonment, diagnose onboarding drop-off, or says ''people start but never finish''. With no site yet, use create-website; for a whole-site look, message, and speed audit, improve-website; if the flow converts but needs traffic, grow-website; for in-product engagement and retention, improve-app. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa conversion-optimization para ... (nombrala en el prompt).»

### `create-app`  _(ficha basica)_

- **Para que sirve:** Guided journey from a raw app idea to a validated, cleanly architected first version that ships on a sustainable cadence.
- **Cuando usarla:** Guided journey from a raw app idea to a validated, cleanly architected first version that ships on a sustainable cadence. Orchestrates ten skills phase by phase - lean-startup, design-sprint, clean-architecture, domain-driven-design, clean-code, pragmatic-programmer, system-design, ios-hig-design, 37signals-way, software-design-philosophy - asking the user questions at every decision point and recording results in the project docs/ folder (PRODUCT.md, ARCHITECTURE.md, EXPERIMENTS.md, CREATE-APP-PLAN.md) so the journey resumes across sessions. Use when the user wants to build a new app, validate an idea before writing code, architect an MVP that will not need a rewrite, or says ''help me build my app the right way''. App already exists: use improve-app or grow-app. Business idea not yet validated: run create-business first. Marketing site only: use create-website. Architecture-only question: design-code-architecture. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa create-app para ... (nombrala en el prompt).»

### `create-business`  _(ficha basica)_

- **Para que sirve:** Guided journey from raw idea to a validated, positioned, priced business with a chosen beachhead.
- **Cuando usarla:** Guided journey from raw idea to a validated, positioned, priced business with a chosen beachhead. Orchestrates ten skills phase by phase - jobs-to-be-done, mom-test, design-sprint, lean-startup, good-strategy-bad-strategy, blue-ocean-strategy, obviously-awesome, hundred-million-offers, monetizing-innovation, crossing-the-chasm - asking the user questions at every decision point and recording results in the project docs/ folder (CUSTOMER.md, POSITIONING.md, OFFER.md, CREATE-BUSINESS-PLAN.md) so the journey resumes across sessions. Use when the user wants to start a new business, validate a startup idea, find product-market fit before building, or says ''I have an idea for a company''. Do not use once the business has paying customers: use grow-business to add revenue and customers, or improve-business to fix strategy and operations. For building the product itself use create-app or create-website. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa create-business para ... (nombrala en el prompt).»

### `create-website`  _(ficha basica)_

- **Para que sirve:** Guided journey from a blank page to a live, high-converting website, built message-first, then design, then conversion.
- **Cuando usarla:** Guided journey from a blank page to a live, high-converting website, built message-first, then design, then conversion. Orchestrates ten skills phase by phase - one-page-marketing, storybrand-messaging, made-to-stick, top-design, web-typography, refactoring-ui, ux-heuristics, cro-methodology, scorecard-marketing, steve-jobs-design-review - asking the user questions at every decision point and recording results in the project docs/ folder (POSITIONING.md, WEBSITE.md, CREATE-WEBSITE-PLAN.md) so the journey resumes across sessions. Use when the user wants to build a new website or landing page from scratch, turn a validated idea into a page that converts, or says ''build me a landing page for my SaaS''. Site already exists: use improve-website site-wide, conversion-optimization for one flow, or grow-website for traffic; building a software product, not a marketing site: create-app; no positioning yet: create-business first, or the positioning phase here. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa create-website para ... (nombrala en el prompt).»

### `design-code-architecture`  _(ficha basica)_

- **Para que sirve:** Guided journey from an app idea to a deliberate architecture: boundaries, domain model, data decisions, and resilience, making only the expensive-to-reverse decisions and deferring the rest.
- **Cuando usarla:** Guided journey from an app idea to a deliberate architecture: boundaries, domain model, data decisions, and resilience, making only the expensive-to-reverse decisions and deferring the rest. Orchestrates eight skills phase by phase - clean-architecture, domain-driven-design, system-design, ddia-systems, software-design-philosophy, release-it, pragmatic-programmer, 37signals-way - asking the user questions at every decision point and recording results in the project docs/ folder (ARCHITECTURE.md, DESIGN-CODE-ARCHITECTURE-PLAN.md) so the journey resumes across sessions. Use when the user wants to design a new app''s architecture, choose boundaries and a domain model, decide monolith versus microservices, or says ''how should I structure this app''. If a codebase already exists, use remove-technical-debt (aged), improve-code-quality (fresh prototype), or architecture-optimization (slow but working); if unvalidated, run create-business or create-app first. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa design-code-architecture para ... (nombrala en el prompt).»

### `grow-app`  _(ficha basica)_

- **Para que sirve:** Guided journey from an app people sign up for and then quietly abandon to a sealed retention engine with a habit loop, an activated first run, and one metric the whole team trusts.
- **Cuando usarla:** Guided journey from an app people sign up for and then quietly abandon to a sealed retention engine with a habit loop, an activated first run, and one metric the whole team trusts. Orchestrates eight skills phase by phase - hooked-ux, improve-retention, continuous-discovery, lean-ux, inspired-product, lean-analytics, microinteractions, drive-motivation - asking the user questions at every decision point and recording results in the project docs/ folder (PRODUCT.md, METRICS.md, GROW-APP-PLAN.md) so the journey resumes across sessions. Use when the user wants to lift activation and retention, design a habit loop, fix a leaky onboarding funnel, or says ''users sign up then disappear''. Do not use to fix broken UX or performance that no engagement mechanic can paper over - run improve-app first; if there is no app yet, use create-app. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa grow-app para ... (nombrala en el prompt).»

### `grow-business`  _(ficha basica)_

- **Para que sirve:** Guided journey from a business with lucky months to a repeatable growth engine that produces a forecast.
- **Cuando usarla:** Guided journey from a business with lucky months to a repeatable growth engine that produces a forecast. Orchestrates nine skills phase by phase - one-page-marketing, hundred-million-offers, predictable-revenue, contagious, influence-psychology, crossing-the-chasm, cold-start-problem, lean-analytics, negotiation - asking the user questions at every decision point and recording results in the project docs/ folder (MARKETING.md, OFFER.md, METRICS.md, GROW-BUSINESS-PLAN.md) so the journey resumes across sessions. Use when the user wants to build a marketing and sales system, manufacture predictable pipeline, engineer word-of-mouth and referrals, or says ''revenue is real but lumpy and I need growth that repeats''. If the offer, retention, or operations underneath are broken, run improve-business first; with no paying customers yet, start with create-business; when the product itself must carry the growth loops, use grow-app. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa grow-business para ... (nombrala en el prompt).»

### `grow-website`  _(ficha basica)_

- **Para que sirve:** Guided journey from a website with traffic it under-converts to a research-driven growth engine that captures more leads, persuades more buyers, sells a sharper offer, and earns referrals.
- **Cuando usarla:** Guided journey from a website with traffic it under-converts to a research-driven growth engine that captures more leads, persuades more buyers, sells a sharper offer, and earns referrals. Orchestrates eight skills phase by phase - cro-methodology, scorecard-marketing, storybrand-messaging, made-to-stick, influence-psychology, hundred-million-offers, contagious, one-page-marketing - asking the user questions at every decision point and recording results in the project docs/ folder (WEBSITE.md, OFFER.md, MARKETING.md, GROW-WEBSITE-PLAN.md) so the journey resumes across sessions. Use when the user wants to raise conversion on a site that already has traffic, capture more leads, sharpen a weak offer, add referral loops, or says ''my site gets visitors but nobody buys''. If a broken funnel or usability friction is the real blocker, run improve-website first; if there is no site yet, use create-website; for one leaking flow, conversion-optimization. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa grow-website para ... (nombrala en el prompt).»

### `improve-app`  _(ficha basica)_

- **Para que sirve:** Guided journey from a shipped app that works but feels rough to a product that fits the job, flows without friction, reads clearly, and persuades honestly.
- **Cuando usarla:** Guided journey from a shipped app that works but feels rough to a product that fits the job, flows without friction, reads clearly, and persuades honestly. Orchestrates nine skills phase by phase - jobs-to-be-done, ux-heuristics, design-everyday-things, refactoring-ui, microinteractions, made-to-stick, influence-psychology, high-perf-browser, steve-jobs-design-review - asking the user questions at every decision point and recording results in the project docs/ folder (CUSTOMER.md, DESIGN.md, POSITIONING.md, IMPROVE-APP-PLAN.md) so the journey resumes across sessions. Use when the user wants to fix a clunky product, cut UX friction, sharpen in-app copy, or says ''the app works but feels rough''. Not for code, tests, or hardening - use improve-code-quality (fresh prototype) or remove-technical-debt (aged); no app yet, create-app; needs growth loops, grow-app; marketing-site friction, improve-website; one leaking flow, conversion-optimization. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa improve-app para ... (nombrala en el prompt).»

### `improve-business`  _(ficha basica)_

- **Para que sirve:** Guided journey from a stalled, plateaued business to one with an honest diagnosis, a working operating rhythm, and offers repriced to real value.
- **Cuando usarla:** Guided journey from a stalled, plateaued business to one with an honest diagnosis, a working operating rhythm, and offers repriced to real value. Orchestrates eight skills phase by phase - good-strategy-bad-strategy, traction-eos, high-output-management, team-topologies, drive-motivation, lean-analytics, negotiation, monetizing-innovation - asking the user questions at every decision point and recording results in the project docs/ folder (STRATEGY.md, OPERATIONS.md, METRICS.md, IMPROVE-BUSINESS-PLAN.md) so the journey resumes across sessions. Use when the user wants to fix a business that has plateaued, diagnose why growth stalled, tighten strategy and execution, re-motivate a team, or says ''revenue is flat and I do not know why''. Starting from scratch with no customers: use create-business. Once the fundamentals work and the goal is expansion: use grow-business. When the product itself drags the business down: use improve-app. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa improve-business para ... (nombrala en el prompt).»

### `improve-code-quality`  _(ficha basica)_

- **Para que sirve:** Guided journey from a working-but-untested vibe-coded prototype to a production-ready product with tests, clean structure, a business-rules boundary, and resilience at scale.
- **Cuando usarla:** Guided journey from a working-but-untested vibe-coded prototype to a production-ready product with tests, clean structure, a business-rules boundary, and resilience at scale. Orchestrates nine skills phase by phase - working-with-legacy-code, clean-code, refactoring-patterns, software-design-philosophy, clean-architecture, pragmatic-programmer, release-it, system-design, ddia-systems - asking the user questions at every decision point and recording results in the project docs/ folder (TESTING.md, TECH-DEBT.md, IMPROVE-CODE-QUALITY-PLAN.md) so the journey resumes across sessions. Use when the user wants to harden an AI-generated prototype, add tests before refactoring, make code safe to change, or says ''this works on my machine but I am scared to touch it''. For an aged codebase, remove-technical-debt; for greenfield structure, design-code-architecture; for a product and UX pass, improve-app; to optimize speed and structure, architecture-optimization. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa improve-code-quality para ... (nombrala en el prompt).»

### `improve-retention`  _(ficha basica)_

- **Para que sirve:** Diagnose and fix retention problems using behavior design (B=MAP).
- **Cuando usarla:** Diagnose and fix retention problems using behavior design (B=MAP). Use when the user mentions "users sign up but dont stick around", "activation rate", "onboarding friction", "retention metrics", "why users dont complete", "churn analysis", or "aha moment". Also trigger when analyzing cohort retention curves, designing activation milestones, reducing time-to-value for new users, or investigating why users quit after their first session. Covers the Ability Chain, prompt design, and tiny behaviors that compound. For habit loops and variable rewards, see hooked-ux. For intrinsic motivation, see drive-motivation.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa improve-retention para ... (nombrala en el prompt).»

### `improve-website`  _(ficha basica)_

- **Para que sirve:** Guided journey from a live website that underperforms to a prioritized, evidence-backed backlog of conversion, usability, message, and speed fixes - each shipped as a testable experiment.
- **Cuando usarla:** Guided journey from a live website that underperforms to a prioritized, evidence-backed backlog of conversion, usability, message, and speed fixes - each shipped as a testable experiment. Orchestrates eight skills phase by phase - cro-methodology, ux-heuristics, refactoring-ui, web-typography, storybrand-messaging, high-perf-browser, made-to-stick, design-everyday-things - asking the user questions at every decision point and recording results in the project docs/ folder (WEBSITE.md, DESIGN.md, IMPROVE-WEBSITE-PLAN.md) so the journey resumes across sessions. Use when the user wants to fix a landing page that isn''t converting, diagnose why visitors leave, audit for clarity and usability, or says ''the homepage feels off but a redesign didn''t help''. No site yet, create-website; converts but needs traffic, grow-website; if the friction is in a product app, not the marketing site, improve-app; if one specific flow leaks, conversion-optimization. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa improve-website para ... (nombrala en el prompt).»

### `remove-technical-debt`  _(ficha basica)_

- **Para que sirve:** Guided journey from a large aged codebase everyone fears to touch to one that is safe to change, legible, bounded, and resilient - paid down in place without a rewrite.
- **Cuando usarla:** Guided journey from a large aged codebase everyone fears to touch to one that is safe to change, legible, bounded, and resilient - paid down in place without a rewrite. Orchestrates eight skills phase by phase - working-with-legacy-code, refactoring-patterns, clean-code, software-design-philosophy, clean-architecture, pragmatic-programmer, release-it, domain-driven-design - asking the user questions at every decision point and recording results in the project docs/ folder (TESTING.md, TECH-DEBT.md, REMOVE-TECHNICAL-DEBT-PLAN.md) so the journey resumes across sessions. Use when the user wants to tame a legacy codebase, pay down technical debt safely, avoid a big-bang rewrite, or says ''we are afraid to touch this code''. For a fresh vibe-coded prototype, improve-code-quality; for greenfield structure, design-code-architecture; for a product-and-UX pass, improve-app; to optimize a working codebase for speed, architecture-optimization. For one framework in isolation, invoke that skill directly.
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa remove-technical-debt para ... (nombrala en el prompt).»

## Video / Composiciones

_Video y composiciones programaticas._

### `hyperframes-registry`  _(ficha basica)_

- **Para que sirve:** Search, install, and wire registry blocks and components into HyperFrames compositions.
- **Cuando usarla:** Search, install, and wire registry blocks and components into HyperFrames compositions. Use BEFORE hand-building any named visual — whenever a brief, a user, or a storyboard names a look, effect, treatment, or transition such as CRT scanlines, glitch, chromatic aberration, film grain, a shimmer sweep, a chart, a code or terminal window, a map, or a confetti burst — because roughly 400 hosted items already cover many of them and the search ranks all of them with nothing installed, no project, and no account. Also use when running hyperframes add or hyperframes catalog, installing one item or every block matching a tag, wiring an installed item into index.html, or working with hyperframes.json. Covers discovery, install locations, block sub-composition wiring, component snippet merging, and authoring a new block or component to contribute upstream (idea → scaffold → validate → PR).
- **Donde:** (pendiente: completar la ficha en skills-meta.json)
- **Como llamarla:** se activa sola o nombrala en el prompt (palabras clave: ver la descripcion en SKILL.md)
- **Ejemplo:** «Usa hyperframes-registry para ... (nombrala en el prompt).»

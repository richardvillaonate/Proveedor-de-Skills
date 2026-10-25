---
name: deepseek-saver
description: Ahorra tokens y dinero al usar modelos DeepSeek (deepseek-flash, deepseek-v4-pro) por la API compatible con Anthropic. Usala SIEMPRE que el usuario trabaje con DeepSeek, mencione costos, tokens, cache hit/miss, precios, "ahorrar", horario peak/off-peak, o antes de lanzar tareas largas, por lotes, refactors grandes o subagentes. Tambien cuando pregunte "es buen momento para esto?" o cuanto falta para off-peak.
---

# deepseek-saver

Reglas para gastar lo minimo con DeepSeek y avisar del horario de tarifa.

## 1. Horario (el script es la fuente de verdad)

Ejecuta `python3 ~/.claude/skills/deepseek-saver/scripts/peak_check.py` (en Windows: `python`).
Devuelve PEAK/OFF-PEAK, el tiempo hasta el cambio y la hora en Colombia.

- PEAK: lunes a viernes, 01:00-04:00 y 06:00-10:00 UTC (Colombia: 20:00-23:00 dom-jue y 01:00-05:00 lun-vie), excepto festivos de China. Cuesta el doble.
- Fines de semana y festivos de China: todo el dia es OFF-PEAK.
- Si hay un mensaje `[deepseek-saver]` en el contexto, resumelo en una linea al usuario.
- En PEAK, antes de una tarea pesada y no urgente, ofrece esperar. Si es urgente, sigue sin sermonear.

## 2. Entrada: maximizar cache hit (50x mas barato en Flash)

- El cache es por prefijo: lo estatico primero (system, herramientas, docs), lo variable al final.
- No cambies el prefijo: nada de fechas/horas, IDs aleatorios ni reordenar herramientas.
- Conversaciones append-only: no edites ni borres mensajes viejos; resume en bloque cuando crezca.
- Agrupa peticiones que comparten contexto en poco tiempo.
- No releas archivos enteros sin necesidad: usa rangos de lineas o grep.

## 3. Salida: generar menos

- La salida no se cachea y es lo mas caro por token.
- Respuestas concisas; no repitas codigo que no cambio, usa ediciones puntuales.
- Modo non-thinking cuando no haga falta razonar (los tokens de pensamiento cuentan como salida).
- deepseek-flash para tareas simples; deepseek-v4-pro solo para lo dificil.
- Evita lanzar subagentes en paralelo para tareas pequenas (cada uno paga su propio contexto).

## 4. Auditoria rapida de prompts

Si el usuario comparte prompts o codigo que llama a la API, busca: fechas o UUID dentro del prefijo, JSON con claves en orden variable, herramientas reordenadas, historial recortado en cada turno. Propone el arreglo concreto.

## 5. Precios de referencia (por 1M tokens, off-peak; peak = x2)

| | Flash | Pro |
|---|---|---|
| Entrada cache hit | $0.003 | $0.022 |
| Entrada cache miss | $0.15 | $0.66 |
| Salida | $0.6 | $1.98 |

Pueden cambiar: verifica en la pagina oficial de precios de DeepSeek si hay dudas.

#!/usr/bin/env bash
# Enlaza skills de este repositorio (fuente: .agents/skills) a otro proyecto.
#
# Uso:
#   link-skills.sh --list                    lista las skills disponibles
#   link-skills.sh [-t DIR] [-c] [skill ...]  entrega las skills indicadas (todas si no se indica ninguna)
#
# DIR es el proyecto destino (por defecto, el directorio actual).
# Por defecto crea enlaces simbolicos en DIR/.claude/skills hacia la fuente (rutas absolutas).
# Con -c/--copy copia las carpetas (sin enlaces): el proyecto queda independiente del proveedor.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$ROOT/.agents/skills"
TARGET="$PWD"
COPY=0

usage() { sed -n '2,11p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; }

skills=()
while [ $# -gt 0 ]; do
  case "$1" in
    -l|--list) ls "$SRC"; exit 0 ;;
    -c|--copy) COPY=1; shift ;;
    -t|--target) TARGET="${2:?falta el directorio destino}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "Opcion desconocida: $1" >&2; usage >&2; exit 1 ;;
    *) skills+=("$1"); shift ;;
  esac
done

[ -d "$TARGET" ] || { echo "No existe el destino: $TARGET" >&2; exit 1; }
TARGET="$(cd "$TARGET" && pwd)"
DEST="$TARGET/.claude/skills"

if [ "$DEST" = "$(cd "$SRC/../.." && pwd)/.claude/skills" ]; then
  echo "El destino es este mismo repositorio; no hay nada que enlazar." >&2
  exit 1
fi

if [ ${#skills[@]} -eq 0 ]; then
  mapfile -t skills < <(ls "$SRC")
fi

mkdir -p "$DEST"

linked=0 skipped=0 missing=0
for name in "${skills[@]}"; do
  if [ ! -f "$SRC/$name/SKILL.md" ]; then
    echo "  no existe: $name" >&2
    missing=$((missing + 1))
    continue
  fi
  link="$DEST/$name"
  if [ "$COPY" -eq 0 ] && [ -L "$link" ] && [ "$(readlink "$link")" = "$SRC/$name" ]; then
    skipped=$((skipped + 1))
  elif [ -e "$link" ] || [ -L "$link" ]; then
    echo "  omitida (ya existe algo distinto): $name" >&2
    skipped=$((skipped + 1))
  else
    if [ "$COPY" -eq 1 ]; then cp -r "$SRC/$name" "$link"; else ln -s "$SRC/$name" "$link"; fi
    printf '%s\t%s\t%s\n' "$(date +%F)" "$TARGET" "$name" >> "$ROOT/registro-enlaces.tsv"
    if [ "$COPY" -eq 1 ]; then echo "  copiada: $name"; else echo "  enlazada: $name"; fi
    linked=$((linked + 1))
  fi
done

echo "Destino: $DEST"
echo "Enlazadas: $linked, omitidas: $skipped, inexistentes: $missing"
[ "$linked" -eq 0 ] || python3 "$ROOT/actualizar-registro.py" --quiet || true
[ "$missing" -eq 0 ]

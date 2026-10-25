#!/usr/bin/env python3
"""Indica si DeepSeek esta en PEAK u OFF-PEAK y cuanto falta para el cambio.
PEAK: lunes-viernes 01:00-04:00 y 06:00-10:00 UTC, salvo festivos de China (holidays.json).
Uso:
  python peak_check.py            -> estado legible
  python peak_check.py --json     -> estado en JSON
  python peak_check.py --hook session|prompt  -> salida para hooks de Claude Code
"""
import sys, os, json, datetime as dt
from pathlib import Path

UTC = dt.timezone.utc
CO = dt.timezone(dt.timedelta(hours=-5))  # Colombia, sin horario de verano
PEAK = [(1, 4), (6, 10)]
HERE = Path(__file__).resolve().parent
STATE = Path.home() / ".claude" / "deepseek-saver" / "last_state"


def holidays():
    try:
        return set(json.loads((HERE.parent / "holidays.json").read_text("utf-8"))["dates"])
    except Exception:
        return set()


def is_peak(t, hol):
    t = t.astimezone(UTC)
    if t.weekday() >= 5 or t.strftime("%Y-%m-%d") in hol:
        return False
    return any(a <= t.hour < b for a, b in PEAK)


def next_change(now, hol):
    cur = is_peak(now, hol)
    t = now.replace(minute=0, second=0, microsecond=0)
    for _ in range(24 * 15):
        t += dt.timedelta(hours=1)
        if is_peak(t, hol) != cur:
            return t
    return None


def fmt_delta(d):
    m = int(d.total_seconds() // 60)
    h, m = divmod(m, 60)
    return f"{h}h {m:02d}m" if h else f"{m}m"


def status(now=None):
    now = now or dt.datetime.now(UTC)
    hol = holidays()
    peak = is_peak(now, hol)
    nxt = next_change(now, hol)
    return {
        "peak": peak,
        "now_colombia": now.astimezone(CO).strftime("%a %H:%M"),
        "next_change_colombia": nxt.astimezone(CO).strftime("%a %H:%M") if nxt else None,
        "in": fmt_delta(nxt - now) if nxt else None,
    }


def human(s):
    if s["peak"]:
        return (f"🔴 PEAK (tarifa x2). Pasa a OFF-PEAK en {s['in']} "
                f"({s['next_change_colombia']} hora Colombia).")
    when = f"Entra PEAK en {s['in']} ({s['next_change_colombia']} hora Colombia)." if s["in"] else ""
    return f"🟢 OFF-PEAK (tarifa normal). {when}".strip()


def is_deepseek():
    if os.environ.get("DEEPSEEK_SAVER_ALWAYS") == "1":
        return True
    blob = (os.environ.get("ANTHROPIC_BASE_URL", "") + os.environ.get("ANTHROPIC_MODEL", "")).lower()
    return "deepseek" in blob


def hook(kind):
    if not is_deepseek():
        return
    s = status()
    state = "peak" if s["peak"] else "off"
    last = STATE.read_text().strip() if STATE.exists() else ""
    if kind == "prompt" and last == state:
        return  # solo avisa cuando cambia el estado, para no gastar tokens
    try:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(state)
    except Exception:
        pass
    tip = ("Si la tarea no es urgente (lotes, refactors grandes, subagentes, mucho contexto nuevo), "
           "sugiere esperar al OFF-PEAK." if s["peak"] else
           "Buen momento para tareas pesadas o por lotes.")
    ctx = (f"[deepseek-saver] Horario de precios DeepSeek: {human(s)} {tip} "
           "Menciona este estado al usuario en UNA linea al inicio de tu respuesta.")
    event = "SessionStart" if kind == "session" else "UserPromptSubmit"
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": ctx}},
                     ensure_ascii=False))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--hook"]:
        hook(a[1] if len(a) > 1 else "prompt")
    elif a[:1] == ["--json"]:
        print(json.dumps(status(), ensure_ascii=False))
    else:
        s = status()
        print(f"{human(s)}  (ahora: {s['now_colombia']} Colombia)")

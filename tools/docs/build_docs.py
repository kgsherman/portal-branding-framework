"""Build the generated docs from the theme source files.

    python tools/docs/build_docs.py

Reads   theme/css_variables.template.scss, examples/*/css_variables.*.scss (Aareal, noris),
        theme/portal-brand-tokens-overrides.scss, audit/variable-usage-canary.psv,
        tools/docs/token-content.json (hand-written descriptions + screenshot captions),
        tools/docs/page.template.html
Writes  docs/variable-inventory.md, docs/token-reference.md, docs/brand-tokens.html

docs/README.md is hand-written and not touched. After a rebuild, republish
docs/brand-tokens.html to the team artifact (screenshots go with it as files).
"""
import colorsys
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
TEMPLATE = ROOT / "theme" / "css_variables.template.scss"
EXAMPLES = [("Aareal", ROOT / "examples" / "aareal" / "css_variables.aareal.scss"),
            ("noris", ROOT / "examples" / "noris" / "css_variables.noris.scss")]
OVERRIDES = ROOT / "theme" / "portal-brand-tokens-overrides.scss"
USAGE = ROOT / "audit" / "variable-usage-canary.psv"


def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


# --- 1. parse the template: every variable with its section / subsection -----
def parse_template():
    section, sub, tvars = None, None, {}
    for line in TEMPLATE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"//\s+SECTION (\d)", line)
        if m:
            section, sub = int(m.group(1)), None
            continue
        m = re.match(r"// --- (.+?) -{3,}", line)
        if m:
            sub = m.group(1).strip()
            continue
        m = re.match(r"^\s*(\$[\w-]+):\s*(.+?);\s*(//\s*(.*))?$", line)
        if m and section:
            rhs = m.group(2).replace("!default", "").strip()
            tvars[m.group(1)] = dict(section=section, sub=sub, rhs=rhs, comment=(m.group(4) or "").strip())
    return tvars


def parse_usage():
    coral = []
    for line in USAGE.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        n, t, c, w, h = line.strip().split("|")
        coral.append(dict(name=n, type=t, core=int(c), widgets=int(w), hf=int(h)))
    return coral


def usage_text(v):
    if v["core"] < 0 or v["widgets"] < 0:
        return "composite"
    parts = []
    if v["core"]: parts.append("core %d" % v["core"])
    if v["widgets"]: parts.append("theme/widgets %d" % v["widgets"])
    if v["hf"]: parts.append("header/footer %d" % v["hf"])
    return ", ".join(parts) or "-"


def inventory_rows(tvars, coral):
    names = {v["name"] for v in coral}
    rows = []
    for v in coral:
        t = tvars.get(v["name"])
        if not t:
            status, maps, grp = "removed", "", ""
        elif t["section"] == 3:
            status, maps, grp = "live", t["rhs"], t["sub"]
        elif t["section"] == 4:
            status, maps, grp = "legacy", t["rhs"], "Legacy"
        else:
            status, maps, grp = "token", t["rhs"], t["sub"]
        rows.append(dict(name=v["name"], usage=usage_text(v), status=status, maps=maps, group=grp, origin="Coral"))
    for n, t in tvars.items():
        if t["section"] in (3, 4) and n not in names:
            rows.append(dict(name=n, usage="widget-level / hidden default", status="live" if t["section"] == 3 else "legacy",
                             maps=t["rhs"], group=t["sub"] if t["section"] == 3 else "Legacy", origin="added"))
    return rows


def write_inventory(rows):
    out = ["# Variable inventory", "",
           "Every variable declared by the stock **Customer Experience Coral Theme** (`css_variables`), plus the widget-level variables the framework adds, and where each one now points.", "",
           "* **live** - read by Bootstrap core, a Coral theme include, the header/footer or an OOTB widget. Mapped in Section 3.",
           "* **legacy** - declared by Coral but read by nothing on the Business Portal (instance-wide search, 2026-10). Kept in Section 4, mapped to a token, so custom widgets that still reference it keep compiling.",
           "* **added** - not declared by Coral; OOTB widgets fall back to a hidden `!default` (often a hardcoded colour) unless the theme sets it.", "",
           "Usage counts = how often the variable's sentinel value appeared in the compiled CSS of a canary theme (core = `sp-bootstrap-rem.scss`; theme/widgets = theme includes + widget CSS on the public pages; header/footer = header and footer widget CSS). `-` = 0 on those pages; several of those are still used on authenticated pages or by widgets not on the sampled pages, which is why the status column, not the count, is authoritative.", "",
           "| Variable | Group | Origin | Status | Maps to | Usage (canary hits) |", "|---|---|---|---|---|---|"]
    order = {"live": 0, "added": 1, "legacy": 2, "removed": 3}
    for r in sorted(rows, key=lambda r: (order.get(r["status"] if r["origin"] == "Coral" else "added", 9), r["group"] or "", r["name"])):
        st = r["status"] if r["origin"] == "Coral" else "added (" + r["status"] + ")"
        maps = r["maps"].replace("|", "\\|")
        if len(maps) > 70: maps = maps[:67] + "..."
        out.append("| `%s` | %s | %s | %s | `%s` | %s |" % (r["name"], r["group"] or "", r["origin"], st, maps, r["usage"]))
    write(ROOT / "docs" / "variable-inventory.md", "\n".join(out) + "\n")


# --- 2. wiring: where each token is consumed ---------------------------------
def wiring(tokens):
    plat = {t: [] for t in tokens}
    derived = {t: [] for t in tokens}
    section = None
    for line in TEMPLATE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"//\s+SECTION (\d)", line)
        if m:
            section = int(m.group(1))
            continue
        m = re.match(r"^\s*(\$[\w-]+):\s*(.+?);", line)
        if not m or section is None: continue
        for t in re.findall(r"\$[\w-]+", m.group(2)):
            if t in plat:
                (plat if section >= 3 else derived)[t].append(m.group(1))
    ovs = {t: {} for t in tokens}
    cur = None
    for line in OVERRIDES.read_text(encoding="utf-8").splitlines():
        m = re.match(r"//\s+(?:--- )?([A-C]\d*b?)\. (.+?)\s*-*$", line)
        if m and not line.startswith("//   "):
            cur = m.group(1)
            continue
        if line.strip().startswith("//"): continue
        for t in re.findall(r"\$[\w-]+", line):
            if t in ovs and cur:
                ovs[t][cur] = ovs[t].get(cur, 0) + 1
    return {t: dict(platform=list(dict.fromkeys(plat[t])), derived=list(dict.fromkeys(derived[t])),
                    overrides=list(ovs[t])) for t in tokens}


def write_token_reference(tvars, tokens, wired_map, content):
    desc, shots = content["descriptions"], content["screenshots"]

    def wired(t):
        w = wired_map[t]
        parts = []
        if w["platform"]:
            p = ", ".join("`%s`" % x for x in w["platform"][:5])
            if len(w["platform"]) > 5: p += " +%d more" % (len(w["platform"]) - 5)
            parts.append(p)
        if w["derived"]:
            d = w["derived"]
            parts.append("feeds " + ", ".join("`%s`" % x for x in d[:4]) + (" +%d" % (len(d) - 4) if len(d) > 4 else ""))
        if w["overrides"]:
            parts.append("overrides " + ", ".join(w["overrides"]))
        return "; ".join(parts) or "-"

    out = ["# Token reference", "",
           "Every token in Sections 1 and 2 of `css_variables`, what it visibly changes, and where it is wired in.", "",
           "* **Default** - the framework default (Coral look). Section 1 values are the template's Coral palette.",
           "* **Wired into** - platform variables mapped to it in Section 3/4, other tokens derived from it, and the sections of `portal-brand-tokens-overrides` that use it (A = Next Experience bridge, B = footer, hero, menu bar & headings, C1-C14 = hardcoded fixes, see the guide).",
           "* Override any Section 2 token in Section 1d. Derived tokens recalculate automatically.", ""]
    cur, missing = None, []
    for n in tokens:
        sub = tvars[n]["sub"]
        if sub != cur:
            cur = sub
            out += ["", "## " + sub, ""]
            for f, cap in shots.get(sub.split(".")[0], []):
                out += ["![%s](screenshots/%s)" % (cap.replace("`", ""), f), "*%s*" % cap, ""]
            out += ["| Token | Default | What it changes | Wired into |", "|---|---|---|---|"]
        d = desc.get(n)
        if d is None:
            missing.append(n)
            d = tvars[n]["comment"]
        default = tvars[n]["rhs"]
        if len(default) > 60: default = default[:57] + "..."
        out.append("| `%s` | `%s` | %s | %s |" % (n, default.replace("|", "\\|"), d, wired(n)))
    write(ROOT / "docs" / "token-reference.md", "\n".join(out) + "\n")
    return missing


# --- 3. resolve token values (Sass subset) for the page -----------------------
def _args(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(": depth += 1
        if ch == ")": depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip()); cur = ""; continue
        cur += ch
    if cur.strip(): out.append(cur.strip())
    return out


def _mix(c1, c2, w):
    return tuple(round(c1[i] * w + c2[i] * (1 - w)) for i in range(3))


def _colour(expr, vars):
    expr = expr.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", expr)
    if m: h = m.group(1); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"#([0-9a-fA-F]{3})", expr)
    if m: return tuple(int(c * 2, 16) for c in m.group(1))
    if re.fullmatch(r"\$[\w-]+", expr):
        v = vars.get(expr)
        return v if isinstance(v, tuple) else None
    m = re.fullmatch(r"mix\((.*)\)", expr, re.I)
    if m:
        a = _args(m.group(1))
        c1, c2 = _colour(a[0], vars), _colour(a[1], vars)
        w = float(a[2].rstrip("%")) / 100 if len(a) > 2 else 0.5
        return _mix(c1, c2, w) if c1 and c2 else None
    m = re.fullmatch(r"(darken|lighten)\((.*)\)", expr, re.I)
    if m:   # Sass: move HSL lightness by the given percentage points
        a = _args(m.group(2))
        c = _colour(a[0], vars)
        if not c: return None
        h, l, s = colorsys.rgb_to_hls(*(x / 255 for x in c))
        d = float(a[1].rstrip("%")) / 100 * (-1 if m.group(1).lower() == "darken" else 1)
        return tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, min(1, max(0, l + d)), s))
    return None


def evaluate(path):
    src = "\n".join(re.sub(r'(^|[^:"\'(])//.*$', r"\1", l) for l in path.read_text(encoding="utf-8").splitlines())
    vars = {}
    for st in src.split(";"):
        m = re.match(r"^\s*(\$[\w-]+)\s*:\s*([\s\S]*?)\s*$", st)
        if not m: continue
        name, raw = m.group(1), m.group(2)
        is_default = raw.endswith("!default")
        raw = re.sub(r"\s*!default$", "", raw)
        if is_default and name in vars and vars[name] is not None: continue
        if raw == "null": vars[name] = None; continue
        c = _colour(raw, vars)
        if c is not None: vars[name] = c; continue
        if re.fullmatch(r"\$[\w-]+", raw) and raw in vars: vars[name] = vars[raw]; continue
        vars[name] = raw
    return vars


def show(v, vars):
    if v is None: return {"t": "null", "v": "null"}
    if isinstance(v, tuple): return {"t": "c", "v": "#%02X%02X%02X" % v}
    v = re.sub(r"\s+", " ", v)

    def rgba(m):
        c = _colour(m.group(1), vars)
        return "rgba(%d, %d, %d, %s)" % (c + (m.group(2).strip(),)) if c else m.group(0)

    def var(m):
        x = vars.get(m.group(0))
        return "#%02X%02X%02X" % x if isinstance(x, tuple) else x if isinstance(x, str) else m.group(0)
    v = re.sub(r"rgba\((\$[\w-]+),\s*([^)]+)\)", rgba, v)
    v = re.sub(r"\$[\w-]+", var, v)
    if "gradient(" in v or "url(" in v:
        return {"t": "g", "v": v}
    return {"t": "s", "v": v}


def write_page(tvars, tokens, wired_map, rows, content):
    themes = [evaluate(TEMPLATE)] + [evaluate(path) for _, path in EXAMPLES]
    data = {
        "examples": [name for name, _ in EXAMPLES],
        "tokens": [{
            "n": n, "g": tvars[n]["sub"], "d": tvars[n]["rhs"], "x": content["descriptions"].get(n, tvars[n]["comment"]),
            "v": [show(t.get(n), t) for t in themes],
            "p": wired_map[n]["platform"], "f": wired_map[n]["derived"], "s": wired_map[n]["overrides"],
        } for n in tokens],
        "inventory": [{"n": r["name"], "g": r["group"], "o": r["origin"], "s": r["status"], "m": r["maps"], "u": r["usage"]} for r in rows],
    }
    payload = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    page = (HERE / "page.template.html").read_text(encoding="utf-8").replace("__PAGEDATA__", payload)
    write(ROOT / "docs" / "brand-tokens.html", page)
    return {name: sum(1 for t in data["tokens"] if t["v"][0]["v"] != t["v"][i + 1]["v"]) for i, (name, _) in enumerate(EXAMPLES)}


def main():
    tvars, coral = parse_template(), parse_usage()
    tokens = [n for n, v in tvars.items() if v["section"] in (1, 2)]
    missing_coral = [v["name"] for v in coral if v["name"] not in tvars]
    rows = inventory_rows(tvars, coral)
    content = json.loads((HERE / "token-content.json").read_text(encoding="utf-8"))
    wired_map = wiring(tokens)
    write_inventory(rows)
    missing_desc = write_token_reference(tvars, tokens, wired_map, content)
    changed = write_page(tvars, tokens, wired_map, rows, content)
    print("tokens %d, inventory rows %d, examples differ from the template on: %s" % (
        len(tokens), len(rows), ", ".join("%s %d tokens" % kv for kv in changed.items())))
    if missing_coral: print("WARNING Coral variables missing from the template:", missing_coral)
    if missing_desc: print("WARNING tokens without a description in token-content.json:", missing_desc)


if __name__ == "__main__":
    main()

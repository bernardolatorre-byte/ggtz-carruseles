import json, re, sys, pathlib
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
NEW = pathlib.Path(__file__).resolve().parent
FONTS = NEW / "fuentes"
REC = NEW
BLOBS = {k: REC / v for k, v in json.load(open(REC / "assets.json")).items()}
names = sys.argv[3:]
fonts = f"""
@font-face{{font-family:'Instrument Serif';src:url('file://{FONTS}/InstrumentSerif-Regular.ttf');font-style:normal}}
@font-face{{font-family:'Instrument Serif';src:url('file://{FONTS}/InstrumentSerif-Italic.ttf');font-style:italic}}
@font-face{{font-family:'Hanken Grotesk';src:url('file://{FONTS}/HankenGrotesk[wght].ttf');font-weight:100 900}}
@font-face{{font-family:'Gloock';src:url('file://{FONTS}/Gloock-Regular.ttf')}}
"""
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for i, n in enumerate(names, 1):
        src = (SRC / n).read_text()
        props = json.loads(re.search(r"data-props='([^']*)'", src).group(1).replace("&amp;", "&"))
        w, h = props["$preview"]["width"], props["$preview"]["height"]
        body = re.search(r"<x-dc>(.*)</x-dc>", src, re.S).group(1)
        style = "".join(re.findall(r"<style>(.*?)</style>", body, re.S))
        body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
        html = f"<!doctype html><html><head><meta charset='utf-8'><style>{fonts}{style}</style></head><body>{body}</body></html>"
        for k, v in props.items():
            if isinstance(v, dict) and "default" in v:
                html = html.replace("{{" + k + "}}", str(v["default"]))
        for bid, path in BLOBS.items():
            html = html.replace(f"/_blob/{bid}", f"file://{path}")
        if "{{" in html:
            print("WARN unreplaced hole in", n, re.findall(r"\{\{[^}]+\}\}", html)[:3])
        tmp = OUT / f"_{i}.html"
        tmp.write_text(html)
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(f"file://{tmp}")
        pg.wait_for_timeout(600)
        over = pg.evaluate("""() => { const r=document.body.firstElementChild; const out=[]; r.querySelectorAll('*').forEach(e=>{ if(e.scrollHeight>e.clientHeight+2 && getComputedStyle(e).overflow==='hidden' && e!==r) out.push(e.tagName)}); return [r.scrollHeight, out.length]; }""")
        name = n.replace(".dc.html", "").lower() + ".png"
        pg.screenshot(path=str(OUT / name), clip={"x": 0, "y": 0, "width": w, "height": h})
        pg.close(); tmp.unlink()
        print(name, over)
    b.close()

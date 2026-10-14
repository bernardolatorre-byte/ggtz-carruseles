# Genera los archivos del logo "Bernardo Latorre · Tax Consultant" (aprobado por Berny el 13 oct 2026)
# en PNG con fondo transparente (2x). Uso: python3 recursos/marca/_gen_marca.py
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
F = HERE.parent / "fuentes"
FONTS = f"""
@font-face{{font-family:'Gloock';src:url('file://{F}/Gloock-Regular.ttf')}}
@font-face{{font-family:'Hanken Grotesk';src:url('file://{F}/HankenGrotesk[wght].ttf');font-weight:100 900}}
body{{margin:0;background:transparent}}
"""

def sello(ink, size, rid="r"):
    return (f'<svg viewBox="0 0 200 200" width="{size}" height="{size}">'
            f'<defs><path id="{rid}" d="M100,100 m-75,0 a75,75 0 1,1 150,0 a75,75 0 1,1 -150,0"/></defs>'
            f'<circle cx="100" cy="100" r="97" fill="none" stroke="{ink}" stroke-width="2.4"/>'
            f'<circle cx="100" cy="100" r="57" fill="none" stroke="{ink}" stroke-width="2"/>'
            f'<text font-family="Hanken Grotesk" font-size="15" font-weight="700" fill="{ink}" letter-spacing="2">'
            f'<textPath href="#{rid}" textLength="462">TAX CONSULTANT · MONTERREY · N.L. ·</textPath></text>'
            f'<text x="100" y="117" text-anchor="middle" font-family="Gloock" font-size="50" fill="{ink}">BL</text></svg>')

def estampilla(fill, ink, size, label=True):
    pts = sorted({(p, q) for i in range(11) for p, q in [(i*32, 0), (i*32, 320), (0, i*32), (320, i*32)]})
    holes = "".join(f'<circle cx="{x}" cy="{y}" r="13"/>' for x, y in pts)
    extra = (f'<rect x="34" y="34" width="252" height="252" fill="none" stroke="{ink}" stroke-width="2"/>'
             f'<text x="160" y="72" text-anchor="middle" font-family="Hanken Grotesk" font-size="12" font-weight="700" letter-spacing="4" fill="{ink}">MONTERREY · MX</text>'
             f'<text x="160" y="250" text-anchor="middle" font-family="Hanken Grotesk" font-size="15" font-weight="700" letter-spacing="4" fill="{ink}">TAX CONSULTANT</text>'
             f'<text x="160" y="190" text-anchor="middle" font-family="Gloock" font-size="128" fill="{ink}">BL</text>') if label else \
            f'<text x="160" y="205" text-anchor="middle" font-family="Gloock" font-size="140" fill="{ink}">BL</text>'
    # las perforaciones se recortan con una máscara para que el PNG quede transparente
    return (f'<svg viewBox="-20 -20 360 360" width="{size}" height="{size}"><defs><mask id="m">'
            f'<rect x="-20" y="-20" width="360" height="360" fill="black"/><rect x="0" y="0" width="320" height="320" fill="white"/>'
            f'<g fill="black">{holes}</g></mask></defs><g mask="url(#m)"><rect x="0" y="0" width="320" height="320" fill="{fill}"/>{extra}</g></svg>')

def principal(ink):
    return (f'<div style="display:inline-flex;flex-direction:column;padding:20px;color:{ink}">'
            f'<div style="font-family:Gloock;font-size:212px;line-height:.92;letter-spacing:-.02em">Bernardo</div>'
            f'<div style="display:flex;align-items:center;gap:34px">{sello(ink, 230)}'
            f'<div style="font-family:Gloock;font-size:212px;line-height:.92;letter-spacing:-.02em">Latorre</div></div>'
            f'<div style="margin-top:46px;display:flex;align-items:center;gap:22px"><div style="height:2px;width:120px;background:{ink}"></div>'
            f'<div style="font-family:Hanken Grotesk;font-size:30px;font-weight:700;letter-spacing:.32em">TAX CONSULTANT</div></div></div>')

def horizontal(ink, fill, stampink):
    return (f'<div style="display:inline-flex;align-items:center;gap:48px;padding:20px;color:{ink}">{estampilla(fill, stampink, 250, False)}'
            f'<div style="display:flex;flex-direction:column;gap:18px"><div style="font-family:Gloock;font-size:128px;line-height:.95;letter-spacing:-.02em;white-space:nowrap">Bernardo Latorre</div>'
            f'<div style="display:flex;align-items:center;gap:20px"><div style="height:2px;width:90px;background:{ink}"></div>'
            f'<div style="font-family:Hanken Grotesk;font-size:26px;font-weight:700;letter-spacing:.32em">TAX CONSULTANT</div></div></div></div>')

INK, MARFIL, AZUL = "#1E242C", "#F4F1EA", "#B7CFE6"
PIEZAS = {
    "logo-principal-pizarra": principal(INK),
    "logo-principal-marfil": principal(MARFIL),
    "logo-horizontal-pizarra": horizontal(INK, "#262F3B", AZUL),
    "logo-horizontal-marfil": horizontal(MARFIL, AZUL, "#262F3B"),
    "sello-pizarra": f'<div style="display:inline-block;padding:10px">{sello(INK, 600)}</div>',
    "sello-marfil": f'<div style="display:inline-block;padding:10px">{sello(MARFIL, 600)}</div>',
    "estampilla-azul": f'<div style="display:inline-block">{estampilla(AZUL, "#262F3B", 700)}</div>',
    "estampilla-pizarra": f'<div style="display:inline-block">{estampilla("#262F3B", AZUL, 700, False)}</div>',
}

tmp = HERE / "_tmp.html"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=2, viewport={"width": 1800, "height": 1200})
    for name, html in PIEZAS.items():
        tmp.write_text(f"<html><head><meta charset='utf-8'><style>{FONTS}</style></head><body><div id='x' style='display:inline-block'>{html}</div></body></html>")
        pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.locator("#x").screenshot(path=str(HERE / f"{name}.png"), omit_background=True)
        print(name)
    # foto de perfil cuadrada (fondo pizarra)
    pg.set_viewport_size({"width": 540, "height": 540})
    tmp.write_text(f"<html><head><meta charset='utf-8'><style>{FONTS}</style></head><body style='width:540px;height:540px;background:#262F3B;display:flex;align-items:center;justify-content:center'>{estampilla(AZUL, '#262F3B', 380)}</body></html>")
    pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
    pg.screenshot(path=str(HERE / "perfil-instagram-1080.png"))
    print("perfil")
    b.close()
tmp.unlink()

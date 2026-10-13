# Miércoles en 3 láminas: Ley de Economía Digital (Ecd-*)
import importlib.util, pathlib, io, contextlib, random
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("base", HERE / "_gen_oct20_22.py")
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)
page, B, foot, sello, tape, cierre = base.page, base.B, base.foot, base.sello, base.tape, base.cierre
TOT = 3
SRC = "Fuente: Cámara de Diputados, 6 oct 2026"

def qr(size=21, cell=14):
    rnd = random.Random(14)
    cells = []
    def finder(cx, cy):
        for y in range(7):
            for x in range(7):
                on = x in (0, 6) or y in (0, 6) or (2 <= x <= 4 and 2 <= y <= 4)
                if on: cells.append((cx + x, cy + y))
    finder(0, 0); finder(size - 7, 0); finder(0, size - 7)
    for y in range(size):
        for x in range(size):
            if (x < 8 and y < 8) or (x >= size - 8 and y < 8) or (x < 8 and y >= size - 8):
                continue
            if rnd.random() < 0.48: cells.append((x, y))
    rects = "".join(f'<rect x="{x*cell}" y="{y*cell}" width="{cell}" height="{cell}"/>' for x, y in cells)
    s = size * cell
    return f'<svg aria-hidden="true" width="{s}" height="{s}" viewBox="0 0 {s} {s}" fill="#1E242C">{rects}</svg>'

# ---------- 01 Portada: fondo terracota liso, celular con QR, título mitad izquierda ----------
p1 = f"""
<div aria-hidden="true" style="position: absolute; right: -220px; top: 200px; width: 720px; height: 720px; border-radius: 50%; border: 3px dashed rgba(38,47,59,0.22)"></div>
<div style="position: absolute; left: 80px; top: 90px; padding: 12px 22px; background: #262F3B; color: #F4F1EA; font-size: 20px; font-weight: 700; letter-spacing: 0.22em; transform: rotate(-2deg)">MIÉRCOLES EN 3 LÁMINAS</div>
<div style="position: absolute; left: 80px; top: 300px; width: 520px; display: flex; flex-direction: column; gap: 28px">
<div class="kicker" style="color: #262F3B">LEY DE ECONOMÍA DIGITAL</div>
<h1 class="serif" style="margin: 0; font-size: 150px; line-height: 0.86; color: #1E242C">¿Adiós al <em style="font-style: italic; color: #FFFDF8">efectivo?</em></h1>
<p style="margin: 0; font-size: 34px; line-height: 1.4; color: #262F3B">Lo que aprobaron los diputados, explicado en 1 minuto.</p>
</div>
<div style="position: absolute; left: 640px; top: 270px; width: 380px; height: 700px; box-sizing: border-box; padding: 18px; border-radius: 56px; background: #262F3B; transform: rotate(6deg); box-shadow: 0 30px 50px rgba(30,36,44,0.35)">
<div style="height: 100%; border-radius: 40px; background: #FFFDF8; display: flex; flex-direction: column; align-items: center; padding: 60px 26px 0; box-sizing: border-box; gap: 26px">
<div style="width: 90px; height: 10px; border-radius: 5px; background: #D9D4C8; margin-top: -36px"></div>
<div class="kicker" style="font-size: 18px; color: #5F7E9E">COBRAR CON QR</div>
<div style="padding: 14px; background: #fff; border: 2px solid #E4DED2; border-radius: 14px">{qr(21, 13)}</div>
<div class="serif" style="font-size: 72px; line-height: 1; color: #1E242C">$185.00</div>
<div style="padding: 10px 22px; border-radius: 30px; background: #A9C9A9; color: #1E242C; font-size: 20px; font-weight: 700">Pago recibido ✓</div>
</div>
</div>
{sello('PASA AL SENADO', '#262F3B', -8, 90, 1040, 32)}
{foot(SRC, 1, TOT)}
"""

# ---------- 02 Qué cambia: sarga oscura con 3 puntos ----------
def punto(n, t, d):
    return (f'<div style="display: flex; gap: 30px; align-items: flex-start">'
            f'<div class="serif" style="flex: 0 0 auto; width: 90px; font-size: 110px; line-height: 0.8; color: #B7CFE6">{n}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 10px"><div class="serif" style="font-size: 54px; line-height: 1">{t}</div>'
            f'<div style="font-size: 29px; line-height: 1.4; color: rgba(244,241,234,0.82)">{d}</div></div></div>')

p2 = f"""
<div style="position: absolute; left: 80px; right: 80px; top: 100px; display: flex; flex-direction: column; gap: 56px">
<div style="display: flex; flex-direction: column; gap: 18px">
<div class="kicker" style="color: #B7CFE6">LO QUE CAMBIA</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.92">El efectivo <em style="font-style: italic; color: #B7CFE6">no desaparece</em>, pero…</h2>
</div>
{punto(1, 'Cobrar en digital', 'Negocios y gobierno tendrán que aceptar pagos electrónicos: tarjeta, transferencia o QR desde el celular.')}
{punto(2, 'Sectores solo digitales', 'Hacienda definirá en qué sectores el pago digital podrá ser la única opción. Será gradual.')}
{punto(3, 'Trámites con CURP digital', 'Podrás abrir cuentas y productos financieros en línea con tu CURP digital.')}
</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 130px; padding: 24px 30px; background: #D9B4A8; color: #1E242C; font-size: 27px; line-height: 1.4; transform: rotate(-1deg)"><b>Ojo:</b> todavía no es ley. Falta que la apruebe el Senado y se publique en el DOF.</div>
{foot(SRC, 2, TOT, True)}
"""

p3 = cierre("¿Tu negocio ya", "cobra en digital?",
            "Cada cobro digital queda registrado en tu banco. Te ayudo a que tu facturación y tu contabilidad cuadren con lo que cobras.",
            "Agenda tu asesoría", "<b>Guárdalo</b> y compártelo con alguien que todavía solo acepta efectivo.",
            "torres", "50% 40%", 3, TOT, "Torres de Monterrey con la Sierra Madre al fondo")

(HERE / "Ecd-01.dc.html").write_text(page("Ley de Economía Digital · Portada", "", "#1E242C", p1, " background: #D9B4A8;"))
(HERE / "Ecd-02.dc.html").write_text(page("Ley de Economía Digital · Qué cambia", "bg-sarga", "#F4F1EA", p2))
(HERE / "Ecd-03.dc.html").write_text(p3)
print("ok")

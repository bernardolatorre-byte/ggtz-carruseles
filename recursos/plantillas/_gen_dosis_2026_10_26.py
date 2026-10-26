# "Tu dosis semanal" (lunes 7:00) #1 — semana del 19 al 25 oct 2026 (Dos1-*).
# Formato: portada con foto de café de Berny + 3 "sorbos" (fiscal, laboral, legal) en degradado + cierre().
# Fuentes: Expansión 21 y 22 oct (Senado comisiones, programa de regularización 2027), Quadratín 21 oct (primera lectura),
# Expansión 21 oct y Zeta Tijuana (acuerdo IMSS Modalidad 40, DOF 21 oct, vigente 22 oct), Expansión Política 25 oct (ley catastral).
import importlib.util as _u, pathlib
HERE = pathlib.Path(__file__).parent
def _load(n):
    s = _u.spec_from_file_location(n, HERE / f"{n}.py"); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
G = _load("_gen_oct20_22"); M = _load("_marca")
page, foot, cierre = G.page, G.foot, G.cierre
ISO = " isolation: isolate;"
H = "@bernardolatorre.fiscal"
T = 5
SEMANA = "19–25 OCT"
CAFE = "/_blob/15e9c1c0c5513d53a848a5eb62972dae"

def taza(color="#F4F1EA", w=150):
    # Taza de línea con vapor (pieza fija de la serie)
    return (f'<svg aria-hidden="true" width="{w}" height="{w}" viewBox="0 0 100 100" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M20 44h50v20c0 13-11 22-25 22s-25-9-25-22z"/><path d="M70 50c11 0 15 4 15 9s-5 10-15 9"/>'
            '<path d="M34 16c-4 5 4 9 0 15M46 12c-4 6 4 10 0 17M58 16c-4 5 4 9 0 15"/></svg>')

def sorbo(n, cat, chip, fondo, titulo, grande, cuerpo, ati, fuente, dark=True, extra=""):
    fg = "#F4F1EA" if dark else "#1E242C"
    sub = "rgba(244,241,234,0.9)" if dark else "#2B3542"
    caja_bg = "#F4F1EA" if dark else "#262F3B"; caja_fg = "#1E242C" if dark else "#F4F1EA"
    return page(f"Sorbo {n}: {cat}", "", fg, f"""
{M.grad(fondo)}
<div style="position:absolute;left:90px;right:90px;top:96px;display:flex;align-items:center;gap:18px">
<span class="serif" style="font-size:30px;letter-spacing:0;color:{fg};opacity:0.75">☕ SORBO {n}</span>
<span style="padding:10px 22px;border-radius:999px;background:{chip};color:#1E242C;font-size:22px;font-weight:700;letter-spacing:0.2em">{cat}</span></div>
<div style="position:absolute;right:70px;top:70px;opacity:0.9">{taza(fg, 110)}</div>
<div style="position:absolute;left:90px;right:90px;top:220px">
<h2 class="serif" style="margin:0;font-size:104px;line-height:0.95;color:{fg}">{titulo}</h2>
{grande}
<p style="margin:34px 0 0;font-size:34px;line-height:1.45;color:{sub};max-width:900px">{cuerpo}</p>
{extra}
<div style="margin-top:50px;padding:32px 38px;background:{caja_bg};color:{caja_fg};transform:rotate(-1deg);max-width:860px;box-shadow:0 16px 30px rgba(0,0,0,0.18)">
<div style="font-size:20px;font-weight:700;letter-spacing:0.22em;color:#C98F7E;margin-bottom:10px">¿Y A TI QUÉ?</div>
<div style="font-size:32px;line-height:1.42">{ati}</div></div></div>
{foot(fuente, n + 1, T, dark)}""", ISO)

S = []

# 1 Portada: foto del café de Berny + degradado
S.append(("Dos1-01-Portada", page("Tu dosis semanal", "", "#F4F1EA", f"""
<img src="{CAFE}" alt="Café en una mesa de terraza" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 75%">
<div aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,24,30,0.92) 0%,rgba(20,24,30,0.78) 42%,rgba(20,24,30,0.15) 72%,rgba(20,24,30,0.35) 100%)"></div>
<img src="{M.SELLO_MARFIL}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;right:80px;top:80px;width:120px;transform:rotate(-8deg)">
<div style="position:absolute;left:90px;top:100px;font-size:24px;font-weight:700;letter-spacing:0.24em;color:#D9B4A8">☕ TU DOSIS SEMANAL · {SEMANA}</div>
<h1 class="serif" style="position:absolute;left:90px;right:90px;top:190px;margin:0;font-size:106px;line-height:0.95">Lo que pasó esta semana, <span style="color:#B7CFE6">mientras te tomas el cafecito</span></h1>
<div style="position:absolute;left:90px;top:640px;display:flex;gap:14px">
{''.join(f'<span style="padding:12px 24px;border-radius:999px;background:{c};color:#1E242C;font-size:22px;font-weight:700;letter-spacing:0.18em">{t}</span>' for t, c in [("FISCAL", "#B7CFE6"), ("LABORAL", "#A9C9A9"), ("LEGAL", "#D9B4A8")])}</div>
<div style="position:absolute;left:90px;bottom:70px;font-size:20px;font-weight:600;color:rgba(244,241,234,0.8)">{H}</div>
<div style="position:absolute;right:80px;bottom:70px;font-size:22px;font-weight:700;color:#F4F1EA">3 sorbos →</div>""")))

# 2 Fiscal
S.append(("Dos1-02-Fiscal", sorbo(1, "FISCAL", "#B7CFE6", "sierra",
    'Viene otro '+'<span style="background:#B7CFE6;color:#1E242C;padding:0 12px">perdón de multas</span>',
    '<div style="margin-top:26px;display:flex;align-items:baseline;gap:20px"><span class="serif" style="font-size:150px;line-height:0.9;color:#B7CFE6">100%</span><span style="font-size:26px;line-height:1.3;color:rgba(244,241,234,0.8)">de descuento en<br>multas y recargos</span></div>',
    "El paquete fiscal 2027 pasó comisiones del Senado el 21 de octubre y esta semana lo vota el pleno. Trae un nuevo programa con hasta <b>100% de descuento en multas y recargos</b> para adeudos de 2025 y años anteriores.",
    "El programa actual cierra este <b>sábado 31</b>. El de 2027 todavía no es ley: no dejes tu adeudo esperando algo que puede cambiar.",
    "Expansión 21 y 22 oct · Senado (primera lectura)")))

# 3 Laboral / IMSS
S.append(("Dos1-03-Laboral", sorbo(2, "LABORAL · IMSS", "#A9C9A9", "noche",
    'La Modalidad 40 '+'<span style="background:#B7CFE6;color:#1E242C;padding:0 12px">ya tiene tope</span>',
    '<div style="margin-top:22px;display:flex;align-items:baseline;gap:20px"><span class="serif" style="font-size:150px;line-height:0.9;color:#A9C9A9">+1 UMA</span><span style="font-size:26px;line-height:1.3;color:rgba(244,241,234,0.8)">máximo sobre<br>tu último salario</span></div>',
    "Desde el 22 de octubre, quien entre a la Modalidad 40 solo puede cotizar con su último salario registrado más una UMA. Antes podías subir hasta 25 UMA. Y ya no hay inscripciones con fecha hacia atrás.",
    "Si ya estabas inscrito, conservas tus condiciones. Si planeabas tu pensión con Modalidad 40, toca hacer números otra vez.",
    "Acuerdo IMSS, DOF 21 oct · Expansión, Zeta")))

# 4 Legal
S.append(("Dos1-04-Legal", sorbo(3, "LEGAL", "#D9B4A8", "salvia",
    'Tu casa va a tener <span style="background:#FFFDF8;padding:0 10px">su propia “CURP”</span>',
    '<div style="margin-top:26px;display:flex;align-items:baseline;gap:20px"><span class="serif" style="font-size:150px;line-height:0.9;color:#262F3B">2027</span><span style="font-size:26px;line-height:1.3;color:#2B3542">trámites catastrales<br>en línea</span></div>',
    "Desde el 24 de octubre está vigente la nueva Ley General de Armonización Catastral y Registral: cada inmueble tendrá una <b>Clave Única Catastral</b> y los trámites pasarán a plataformas digitales desde 2027.",
    "La ley no sube las tasas del predial. Pero si tu municipio actualiza el valor catastral de tu casa, sí podrías pagar más.",
    "Expansión Política, 25 oct", dark=False)))

# 5 Cierre
S.append(("Dos1-05-Cierre", cierre("¿Cuál de los 3", "te pegó más?",
    "Cada lunes te traigo lo que importa en lo fiscal, laboral y legal. Y si alguno te toca de cerca, en GGTZ te ayudamos.",
    "Agenda tu asesoría", "Comenta 1, 2 o 3 y guárdalo para tu próximo cafecito ☕", fondo="atardecer")))

for name, html in S:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok", len(S))

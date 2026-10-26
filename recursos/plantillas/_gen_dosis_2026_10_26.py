# "Tu dosis semanal" (lunes 7:00) #1 — HISTORIAS de Instagram 1080×1920, semana del 19 al 25 oct 2026 (DosS1-*).
# Berny (25 oct 2026): son historias, no carrusel, y SIN degradados tornasol: fondos de color liso de la paleta.
# Fuentes: Expansión 21 y 22 oct (Senado comisiones, programa de regularización 2027), Quadratín 21 oct (primera lectura),
# Expansión 21 oct y Zeta Tijuana (acuerdo IMSS Modalidad 40, DOF 21 oct, vigente 22 oct), Expansión Política 25 oct (ley catastral).
import importlib.util as _u, pathlib
HERE = pathlib.Path(__file__).parent
def _load(n):
    s = _u.spec_from_file_location(n, HERE / f"{n}.py"); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
G = _load("_gen_oct20_22"); M = _load("_marca")
H = "@BERNARDOLATORRE.FISCAL"
SEMANA = "19–25 OCT"
BERNY = "/_blob/25bcb8fe94907e94b0640cf81bd101a6"
PIZ, TIN, MAR, AZ, SAL, TER, TERF = "#262F3B", "#1E242C", "#F4F1EA", "#B7CFE6", "#A9C9A9", "#D9B4A8", "#C98F7E"

def story(title, color, inner, bg):
    """Página 1080×1920. Zona segura: nada en los 200 px de arriba ni en los 220 de abajo."""
    html = G.page(title, "", color, inner, f" background:{bg};")
    return html.replace("height: 1350px", "height: 1920px").replace('"height":1350', '"height":1920')

def taza(color, w=120):
    return (f'<svg aria-hidden="true" width="{w}" height="{w}" viewBox="0 0 100 100" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M20 44h50v20c0 13-11 22-25 22s-25-9-25-22z"/><path d="M70 50c11 0 15 4 15 9s-5 10-15 9"/>'
            '<path d="M34 16c-4 5 4 9 0 15M46 12c-4 6 4 10 0 17M58 16c-4 5 4 9 0 15"/></svg>')

def pie(n, color):
    return (f'<div style="position:absolute;left:90px;right:90px;bottom:260px;display:flex;justify-content:space-between;font-size:20px;font-weight:700;letter-spacing:0.18em;color:{color}">'
            f'<span>{H}</span><span>{n} / 5</span></div>')

def sorbo(n, cat, bg, fg, chip, titulo, cifra, cifra_txt, cuerpo, ati, fuente, caja_bg, caja_fg, cifra_color):
    return story(f"Sorbo {n}: {cat}", fg, f"""
<div style="position:absolute;left:90px;right:90px;top:250px;display:flex;align-items:center;gap:18px">
<span class="serif" style="font-size:34px;color:{fg}">☕ SORBO {n}</span>
<span style="padding:12px 24px;border-radius:999px;background:{chip};color:{TIN};font-size:22px;font-weight:700;letter-spacing:0.2em">{cat}</span></div>
<div style="position:absolute;right:80px;top:225px">{taza(fg, 120)}</div>
<div style="position:absolute;left:90px;right:90px;top:400px">
<h2 class="serif" style="margin:0;font-size:112px;line-height:0.94;color:{fg}">{titulo}</h2>
<div style="margin-top:40px;display:flex;align-items:baseline;gap:22px"><span class="serif" style="font-size:190px;line-height:0.85;color:{cifra_color}">{cifra}</span><span style="font-size:28px;line-height:1.3;font-weight:600;color:{fg}">{cifra_txt}</span></div>
<p style="margin:50px 0 0;font-size:40px;line-height:1.42;color:{fg}">{cuerpo}</p>
<div style="margin-top:64px;padding:40px 44px;background:{caja_bg};color:{caja_fg};transform:rotate(-1.2deg);box-shadow:0 16px 30px rgba(20,24,30,0.18)">
<div style="font-size:21px;font-weight:700;letter-spacing:0.22em;color:{TERF};margin-bottom:12px">¿Y A TI QUÉ?</div>
<div style="font-size:37px;line-height:1.4">{ati}</div></div>
<div style="margin-top:34px;font-size:22px;color:{fg};opacity:0.7">Fuente: {fuente}</div></div>
{pie(n + 1, fg)}""", bg)

S = []

# 1 Portada: ilustración de taza (sin fotos; Berny pidió no usar sus fotos aquí, 25 oct 2026), fondo tinta liso
TAZA_GRANDE = f"""<svg aria-hidden="true" width="760" height="640" viewBox="0 0 760 640" style="position:absolute;left:160px;top:930px">
<g fill="none" stroke="{MAR}" stroke-width="10" stroke-linecap="round"><path d="M250 40c-30 40 30 70 0 120"/><path d="M340 20c-30 45 30 80 0 140"/><path d="M430 40c-30 40 30 70 0 120"/></g>
<ellipse cx="350" cy="560" rx="330" ry="46" fill="{TER}"/>
<path d="M130 200h440v190c0 100-90 170-220 170S130 490 130 390z" fill="{AZ}"/>
<path d="M570 250c90 0 120 40 120 85s-40 90-125 80" fill="none" stroke="{AZ}" stroke-width="44" stroke-linecap="round"/>
<ellipse cx="350" cy="200" rx="220" ry="34" fill="#8A6A55"/>
<rect x="268" y="300" width="164" height="164" rx="12" fill="{TIN}"/>
<text x="350" y="410" text-anchor="middle" font-family="Archivo" font-weight="800" font-size="92" fill="{AZ}" style="font-stretch:88%">BL</text></svg>"""
S.append(("DosS1-01-Portada", story("Tu dosis semanal", MAR, f"""
<img src="{M.SELLO_MARFIL}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;right:80px;top:230px;width:130px;transform:rotate(-8deg)">
<div style="position:absolute;left:90px;top:260px;font-size:26px;font-weight:700;letter-spacing:0.24em;color:{TER}">☕ TU DOSIS SEMANAL</div>
<div style="position:absolute;left:90px;top:305px;font-size:26px;font-weight:700;letter-spacing:0.24em;color:{MAR};opacity:0.75">{SEMANA}</div>
<h1 class="serif" style="position:absolute;left:90px;right:90px;top:400px;margin:0;font-size:104px;line-height:0.96">Lo que pasó esta semana, <span style="background:{AZ};color:{TIN};padding:0 12px">mientras te tomas el cafecito</span></h1>
<div style="position:absolute;left:90px;top:820px;display:flex;gap:14px">
{''.join(f'<span style="padding:14px 26px;border-radius:999px;background:{c};color:{TIN};font-size:24px;font-weight:700;letter-spacing:0.18em">{t}</span>' for t, c in [("FISCAL", AZ), ("LABORAL", SAL), ("LEGAL", TER)])}</div>
{TAZA_GRANDE}
<div style="position:absolute;right:90px;bottom:280px;padding:16px 26px;background:{MAR};color:{TIN};font-size:26px;font-weight:700;border-radius:4px">3 sorbos →</div>
<div style="position:absolute;left:90px;bottom:290px;font-size:20px;font-weight:700;letter-spacing:0.18em;color:{MAR}">{H}</div>""", TIN)))

# 2 Fiscal — azul polvo liso
S.append(("DosS1-02-Fiscal", sorbo(1, "FISCAL", AZ, TIN, MAR,
    f'Viene otro <span style="background:{MAR};padding:0 12px">perdón de multas</span>',
    "100%", "de descuento en<br>multas y recargos",
    "El paquete fiscal 2027 pasó comisiones del Senado el 21 de octubre y esta semana lo vota el pleno. Trae un nuevo programa para adeudos de 2025 y años anteriores.",
    "El programa actual cierra este <b>sábado 31</b>. El de 2027 todavía no es ley: no dejes tu adeudo esperando algo que puede cambiar.",
    "Expansión, 21 y 22 oct", PIZ, MAR, PIZ)))

# 3 Laboral — pizarra liso
S.append(("DosS1-03-Laboral", sorbo(2, "LABORAL · IMSS", PIZ, MAR, SAL,
    f'La Modalidad 40 <span style="background:{SAL};color:{TIN};padding:0 12px">ya tiene tope</span>',
    "+1 UMA", "máximo sobre tu<br>último salario",
    "Desde el 22 de octubre, quien entre a la Modalidad 40 solo puede cotizar con su último salario registrado más una UMA. Antes podías subir hasta 25 UMA.",
    "Si ya estabas inscrito, conservas tus condiciones. Si planeabas tu pensión con Modalidad 40, toca hacer números otra vez.",
    "acuerdo IMSS, DOF 21 oct", MAR, TIN, SAL)))

# 4 Legal — terracota suave liso
S.append(("DosS1-04-Legal", sorbo(3, "LEGAL", TER, TIN, MAR,
    f'Tu casa va a tener <span style="background:{MAR};padding:0 12px">su propia “CURP”</span>',
    "2027", "trámites catastrales<br>en línea",
    "Desde el 24 de octubre está vigente la nueva Ley General de Armonización Catastral y Registral: cada inmueble tendrá una <b>Clave Única Catastral</b>.",
    "La ley no sube las tasas del predial. Pero si tu municipio actualiza el valor catastral de tu casa, sí podrías pagar más.",
    "Expansión Política, 25 oct", PIZ, MAR, PIZ)))

# 5 Cierre — marfil liso, sticker de Berny estilo revista sin degradado
S.append(("DosS1-05-Cierre", story("Cierre dosis semanal", TIN, f"""
<img src="{M.SELLO_PIZARRA}" alt="" aria-hidden="true" style="position:absolute;right:80px;top:230px;width:130px;transform:rotate(-8deg)">
<div style="position:absolute;left:90px;right:220px;top:280px">
<h2 class="serif" style="margin:0;font-size:108px;line-height:0.95">¿Cuál de los 3 <span style="background:{AZ};padding:0 12px">te pegó más?</span></h2>
<p style="margin:40px 0 0;font-size:36px;line-height:1.42;max-width:820px">Respóndeme esta historia con <b>1, 2 o 3</b>. Y si alguno te toca de cerca, en GGTZ te ayudamos.</p>
<div style="margin-top:40px;display:flex;gap:16px">{''.join(f'<span class="serif" style="width:110px;height:110px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;font-size:64px">{t}</span>' for t, c in [("1", AZ), ("2", SAL), ("3", TER)])}</div></div>
<div aria-hidden="true" class="serif" style="position:absolute;left:40px;bottom:520px;font-size:230px;line-height:0.8;letter-spacing:-0.05em;color:#E6E0D3;white-space:nowrap">LATORRE</div>
<img src="{BERNY}" alt="Bernardo Latorre, Tax Consultant" style="position:absolute;right:-60px;bottom:220px;width:620px;height:auto;filter:drop-shadow(0 18px 26px rgba(20,24,30,0.25))">
<div style="position:absolute;left:90px;bottom:300px;display:flex;flex-direction:column;gap:10px;font-size:26px;font-weight:600">
<span>81 2758 0277</span>
<img src="{M.LOGO_H_PIZARRA}" alt="Bernardo Latorre, Tax Consultant" style="width:320px;margin-left:-8px">
<span style="font-size:16px;font-weight:700;letter-spacing:0.26em;color:#5F7E9E">SOCIO EN GGTZ CONSULTORES</span></div>""", MAR)))

for name, html in S:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok", len(S))

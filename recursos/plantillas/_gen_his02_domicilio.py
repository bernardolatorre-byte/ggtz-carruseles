# "Historias de despacho" — Ep. 02: RFC no localizado / sello digital restringido por cambio de domicilio sin aviso.
# Copia de las funciones de _gen_his01_opinion.py (diseño v2.1); único cambio: sello BL bajo la tarjeta de la última lámina.
# Formato v2 (11 oct 2026, pedido por Berny): muy parecido al post de referencia
# (@yosoydiegodiaz): fondo de papel claro, una sola tarjeta negra tipo publicación de X
# centrada en cada lámina, solo texto. v2.1 (11 oct): avatar con foto de Berny y toques mínimos
# (cinta azul polvo, etiqueta de la serie, puntos de avance, una frase clave en azul polvo, giro leve).
# Debe verse claramente distinto de los carruseles de martes y jueves.
import pathlib
OUT = pathlib.Path(__file__).parent
PAPEL = "/_blob/69e0532c9283413a0cbdcf3a9f33ca9b"  # texturas/papel-arrugado.jpg
AVATAR = "/_blob/ee09a830e465eee2f30b4449a3fe87db"  # berny/fotos/avatar-historias.jpg
SELLO = "/_blob/89b150b4a0eaffd521105fa61198e074"  # marca/sello-pizarra.png
TOTAL = 8
FECHA = "9:45 p. m. · 23/10/26"  # fecha y hora reales de publicación; nunca métricas

def page(title, inner, n=1, sello=False):
    rot = [-0.8, 0.7, -0.5, 0.8, -0.7, 0.5, -0.8, 0.6][(n-1) % 8]
    tx = [330, 520, 380, 560, 340, 500, 400, 540][(n-1) % 8]
    dots = "".join(f'<span style="width: {26 if i==n else 10}px; height: 10px; border-radius: 5px; background: {"#2B3542" if i==n else "rgba(43,53,66,0.25)"}"></span>' for i in range(1, TOTAL+1))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0}}
.card p{{margin:0}}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: 'Hanken Grotesk', sans-serif; background-color: #ECEAE6; background-image: url({PAPEL}); background-size: cover; display: flex; align-items: center; justify-content: center">
<div style="position: absolute; top: 92px; left: 0; right: 0; text-align: center; font-size: 21px; font-weight: 700; letter-spacing: 0.28em; color: #5F7E9E">HISTORIAS DE DESPACHO</div>
<div style="display: flex; flex-direction: column; align-items: center">
<div style="position: relative; transform: rotate({rot}deg)">
<div aria-hidden="true" style="position: absolute; left: {tx}px; top: -22px; width: 150px; height: 44px; background: rgba(183,207,230,0.82); transform: rotate({-3 if n % 2 else 4}deg); z-index: 2; box-shadow: 0 2px 4px rgba(0,0,0,0.08)"></div>
{inner}
</div>
{f'<img src="{SELLO}" alt="Sello BL" style="width: 90px; height: 90px; margin-top: 40px; transform: rotate(-6deg); opacity: 0.92">' if sello else ''}
</div>
<div style="position: absolute; bottom: 96px; left: 0; right: 0; display: flex; justify-content: center; gap: 10px">{dots}</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{ renderVals() {{ return {{}}; }} }}
</script>
</body>
</html>
"""

ICONS = """<span style="display: flex; justify-content: space-between; width: 100%">
<svg aria-hidden="true" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#71767B" stroke-width="1.7"><path d="M21 11.5a8.4 8.4 0 0 1-12.2 7.5L4 20l1.1-4.4A8.4 8.4 0 1 1 21 11.5z"/></svg>
<svg aria-hidden="true" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#71767B" stroke-width="1.7"><path d="M4 9l3-3 3 3M7 6v9a3 3 0 0 0 3 3h5M20 15l-3 3-3-3M17 18V9a3 3 0 0 0-3-3H9"/></svg>
<svg aria-hidden="true" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#71767B" stroke-width="1.7"><path d="M12 20s-7-4.4-9-8.6C1.6 8.4 3.5 5 6.8 5c2 0 3.4 1.2 5.2 3 1.8-1.8 3.2-3 5.2-3 3.3 0 5.2 3.4 3.8 6.4C19 15.6 12 20 12 20z"/></svg>
<svg aria-hidden="true" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#71767B" stroke-width="1.7"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>
<svg aria-hidden="true" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#71767B" stroke-width="1.7"><path d="M12 3v12M7 8l5-5 5 5M5 14v6h14v-6"/></svg>
</span>"""

def card(*parts, size=34):
    body = "".join(f"<p>{p}</p>" for p in parts)
    return f"""<div class="card" style="width: 780px; box-sizing: border-box; padding: 46px 48px 36px; background: #000000; color: #E7E9EA; border-radius: 32px; box-shadow: 0 34px 70px rgba(0,0,0,0.28), 0 6px 14px rgba(0,0,0,0.18)">
<div style="display: flex; align-items: center; gap: 20px">
<img src="{AVATAR}" alt="Bernardo Latorre" style="width: 82px; height: 82px; border-radius: 50%; object-fit: cover; flex-shrink: 0">
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 31px; font-weight: 700">Bernardo Latorre</span><span style="font-size: 26px; color: #71767B">@bernardolatorre.fiscal</span></div>
</div>
<div style="margin-top: 34px; font-size: {size}px; line-height: 1.38; display: flex; flex-direction: column; gap: 26px">{body}</div>
<div style="margin-top: 34px; font-size: 24px; color: #71767B">{FECHA}</div>
<div style="margin-top: 22px; padding-top: 24px; border-top: 1px solid #2F3336">{ICONS}</div>
</div>"""

K = lambda t: f'<span style="color: #B7CFE6; font-weight: 600">{t}</span>'
U = lambda t: f'<span style="font-weight: 600; letter-spacing: 0.01em">{t}</span>'

S = {}
S["His2-01-Portada"] = page("Historias 2 · 1", n=1, inner=card(
    U("LUIS NO PUDO FACTURARLE A SU MEJOR CLIENTE…"),
    f"Y todo por {K('mudarse de local.')}", size=40))
S["His2-02-Contexto"] = page("Historias 2 · 2", n=2, inner=card(
    "Luis instala y da mantenimiento a minisplits en Apodaca.",
    "En marzo el negocio creció y se cambió a una bodega más grande, a 15 minutos del local viejo.",
    f"Cambió el letrero, Google Maps y sus tarjetas. {K('Al SAT no le avisó.')}"))
S["His2-03-Problema"] = page("Historias 2 · 3", n=3, inner=card(
    "Meses después fue a facturar un servicio de $85,000 a una cadena de restaurantes.",
    K("El sistema no lo dejó."),
    "El SAT le había restringido su sello digital. Sin sello, no hay factura. Sin factura, no hay pago."))
S["His2-04-Motivo"] = page("Historias 2 · 4", n=4, inner=card(
    "¿Qué pasó? El SAT fue a verificar su domicilio fiscal… al local viejo.",
    "Lo encontró vacío y lo marcó como no localizado.",
    f"Luis pensaba que la dirección {K('“solo era un dato”.')} Es de los descuidos que más veo."))
S["His2-05-Ley"] = page("Historias 2 · 5", n=5, inner=card(
    "Lo que casi nadie sabe:",
    f"Tu domicilio fiscal es donde el SAT te busca. Si te cambias, {K('tienes que presentar el aviso.')}",
    "Si desocupas tu domicilio sin avisar, el SAT puede restringir temporalmente tu sello digital.",
    '<span style="color: #71767B">(Art. 27, apartado B, fr. II y III, y art. 17-H Bis, fr. III del CFF; art. 29, fr. IV del Reglamento del CFF)</span>'))
S["His2-06-Solucion"] = page("Historias 2 · 6", n=6, inner=card(
    "Luis presentó el aviso de cambio de domicilio.",
    "Luego metió la solicitud de aclaración con su contrato de renta y comprobante de domicilio.",
    f"La ley dice que el sello se restablece {K('al día siguiente de la solicitud.')} Así fue: facturó y cobró.",
    '<span style="color: #71767B">(Tienes hasta 40 días hábiles para pedir la aclaración: art. 17-H Bis del CFF)</span>'))
S["His2-07-Leccion"] = page("Historias 2 · 7", n=7, inner=card(
    "Lo que me quedo de esta historia:",
    f"Si cambias de local, casa u oficina, {K('el aviso al SAT va en la misma lista')} que el letrero y la luz.",
    "Y revisa tu buzón tributario: ahí te llega todo lo que el SAT te dice."))
S["His2-08-Cierre"] = page("Historias 2 · 8", n=8, sello=True, inner=card(
    "¿Tu domicilio fiscal sigue siendo donde trabajas hoy? Cuéntame 👇",
    "Si no estás seguro, escríbeme DOMICILIO y lo revisamos.",
    K("📲 81 2758 0277 · GGTZ Consultores"),
    '<span style="font-size: 24px; color: #71767B">Historia ilustrativa: nombre y cifras inventados.</span>'))

for k, v in S.items():
    (OUT / f"{k}.dc.html").write_text(v)
print(len(S))

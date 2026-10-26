# Lunes legal #2 (26 oct 2026): "¿Tu marca ya es tuya?" (Leg2-*).
# Fuente: Ley Federal de Protección a la Propiedad Industrial (LFPPI), reforma DOF 3 abr 2026:
# arts. 170, 172, 173 (fr. I, IV, V, XVIII, XXII), 178, 214, 220, 233 y 237 (verificados en Luthor, corte 25 oct 2026).
# Herramientas del IMPI: Marcanet (consulta de disponibilidad) y ClasNiza (clasificación de productos y servicios).
import importlib.util as _u, pathlib
HERE = pathlib.Path(__file__).parent
def _load(n):
    s = _u.spec_from_file_location(n, HERE / f"{n}.py"); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
G = _load("_gen_oct20_22"); M = _load("_marca")
page, foot, cierre, sello = G.page, G.foot, G.cierre, G.sello
TOT = 7
H = "@bernardolatorre.fiscal"
NARANJAS = "/_blob/1b2f2713c15f34a4723e193276de30d4"
INK = "#1E242C"
S = []

# 1. Portada (degradado bruma, claro): sello ® gigante tipo hule + etiqueta colgante
regi = f"""
<div aria-hidden="true" style="position:absolute;left:580px;top:560px;width:470px;height:470px;transform:rotate(-12deg)">
  <svg width="470" height="470" viewBox="0 0 560 560">
    <defs><filter id="tinta"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="6"/></filter></defs>
    <g filter="url(#tinta)" fill="none" stroke="#C98F7E" opacity="0.92">
      <circle cx="280" cy="280" r="262" stroke-width="16"/>
      <circle cx="280" cy="280" r="226" stroke-width="5"/>
    </g>
    <text x="280" y="372" text-anchor="middle" font-family="Archivo" font-weight="800" font-size="300" fill="#C98F7E" opacity="0.92" filter="url(#tinta)">R</text>
  </svg>
</div>"""
tag = """
<div style="position:absolute;left:130px;top:960px;transform:rotate(-7deg);transform-origin:20px 50%">
  <svg aria-hidden="true" width="120" height="40" viewBox="0 0 120 40" style="position:absolute;left:-104px;top:42px"><path d="M2 30 C 40 2, 80 40, 118 18" fill="none" stroke="#2B3542" stroke-width="3"/></svg>
  <div style="position:relative;width:400px;height:190px;background:#F4F1EA;clip-path:polygon(14% 0,100% 0,100% 100%,14% 100%,0 50%);box-shadow:0 18px 30px rgba(30,36,44,0.2);display:flex;align-items:center">
    <div style="position:absolute;left:28px;top:83px;width:24px;height:24px;border-radius:50%;background:#C9DAEA;border:3px solid #2B3542"></div>
    <div style="margin-left:86px;display:flex;flex-direction:column;gap:8px">
      <div style="font-size:18px;font-weight:700;letter-spacing:0.24em;color:#5F7E9E">TU MARCA</div>
      <div class="serif" style="font-size:48px;line-height:0.95;color:#2B3542">¿Registrada?</div>
      <div style="font-size:20px;color:#3A4552">☐ Sí &nbsp; ☐ No &nbsp; ☐ Ni idea</div>
    </div>
  </div>
</div>"""
S.append(("Leg2-01-Portada", page("Lunes legal: registra tu marca", "", INK, f"""
{M.grad("bruma")}
<img src="{M.SELLO_PIZARRA}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;right:80px;top:80px;width:120px;transform:rotate(8deg)">
<div class="kicker" style="position:absolute;left:90px;top:110px;font-weight:700;color:#2B3542">⚖️ LUNES LEGAL</div>
<h1 class="serif" style="position:absolute;left:90px;right:220px;top:230px;margin:0;font-size:150px;line-height:0.9;color:#2B3542">¿Tu marca ya es <span style="background:linear-gradient(transparent 14%,#B7CFE6 14%,#B7CFE6 92%,transparent 92%);padding:0 10px">tuya?</span></h1>
<p style="position:absolute;left:90px;width:560px;top:600px;margin:0;font-size:33px;line-height:1.4;color:#2B3542">Usar un nombre no es lo mismo que tenerlo registrado. Lo que dice la ley, sin rodeos.</p>
{regi}
{tag}
<div style="position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-size:21px;font-weight:600;color:#2B3542"><span>GGTZ Consultores · {H}</span><span>Desliza →</span></div>
""", " isolation: isolate;")))

# 2. Mito vs realidad (sarga oscura) + sello FALSO
S.append(("Leg2-02-Mito", page("Mito", "bg-sarga", "#F4F1EA", f"""
<div style="position:absolute;left:90px;right:90px;top:110px">
<div class="kicker" style="color:#D9B4A8;font-weight:700">EL MITO MÁS CARO</div>
</div>
<div class="hoja" style="position:absolute;left:90px;right:120px;top:190px;padding:46px 50px;color:#2B3542;transform:rotate(-1.5deg);box-shadow:0 20px 36px rgba(0,0,0,0.35)">
<div class="serif" style="font-size:66px;line-height:1.02">"Yo uso ese nombre desde hace años: <span style="color:#C98F7E">ya es mío</span>"</div>
</div>
{sello('FALSO', '#D9B4A8', -14, 700, 470, 50)}
<div style="position:absolute;left:90px;right:90px;top:620px;display:flex;flex-direction:column;gap:34px">
<div class="kicker" style="color:#A9C9A9;font-weight:700">LA REALIDAD</div>
<h2 class="serif" style="margin:0;font-size:78px;line-height:0.98">Cualquiera puede usar una marca. <span style="color:#B7CFE6">La exclusiva solo la da el registro.</span></h2>
<p style="margin:0;font-size:31px;line-height:1.45;color:rgba(244,241,234,0.9)">Y entre dos solicitudes, el IMPI toma en cuenta <b style="color:#F4F1EA">la que se presentó primero</b>. Si alguien la pide antes que tú, te puede ganar el nombre.</p>
</div>
{foot("Fuente: arts. 170 y 220 LFPPI · " + H, 2, TOT, True)}""")))

# 3. Qué puedes registrar (degradado noche)
tipos = [("Aa", "Nombre", "palabras, letras, números"), ("◆", "Logo", "dibujos y combinaciones de colores"),
         ("▣", "Forma 3D", "el envase o la forma del producto"), ("♪", "Sonido", "un jingle o tono"),
         ("✿", "Olor", "sí, también"), ("▤", "Imagen comercial", "empaque, decoración, diseño del local")]
cards = "".join(
    f'<div style="padding:26px 26px 24px;background:rgba(244,241,234,0.08);border:1px solid rgba(244,241,234,0.22);border-radius:6px;transform:rotate({r}deg)">'
    f'<div style="font-size:40px;line-height:1;color:#B7CFE6">{i}</div>'
    f'<div class="serif" style="font-size:46px;line-height:1;margin-top:14px">{t}</div>'
    f'<div style="font-size:23px;line-height:1.35;margin-top:8px;color:rgba(244,241,234,0.78)">{d}</div></div>'
    for (i, t, d), r in zip(tipos, [-1.2, 1, 0.8, -1, -0.8, 1.2]))
S.append(("Leg2-03-Tipos", page("Qué puedes registrar", "", "#F4F1EA", f"""
{M.grad("noche")}
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:rgba(244,241,234,0.8);font-weight:700">QUÉ PUEDE SER UNA MARCA</div>
<h2 class="serif" style="margin:24px 0 40px;font-size:84px;line-height:0.96">No solo el <span style="background:#B7CFE6;color:{INK};padding:0 12px">nombre</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{cards}</div>
<div style="margin-top:36px;display:flex;gap:18px;align-items:flex-start;padding:22px 26px;background:#F4F1EA;color:{INK};transform:rotate(-0.8deg)">
<div class="serif" style="flex:none;font-size:30px;line-height:1.1;color:#C98F7E">NUEVO<br>2026</div>
<div style="font-size:25px;line-height:1.4">Desde la reforma del 3 de abril de 2026 también se reconocen marcas <b>de posición, de movimiento y multimedia</b>.</div>
</div>
</div>
{foot("Fuente: art. 172 LFPPI · " + H, 3, TOT, True)}""", " isolation: isolate;")))

# 4. Lo que NO se registra (papel) + polaroid naranjas
def no(t, ej):
    return (f'<div style="display:flex;gap:20px;align-items:flex-start;padding:17px 0;border-bottom:1px solid rgba(43,53,66,0.15)">'
            f'<svg aria-hidden="true" width="34" height="34" viewBox="0 0 34 34" style="flex:none;margin-top:4px"><circle cx="17" cy="17" r="16" fill="#D9B4A8"/><path d="M11 11l12 12M23 11L11 23" stroke="{INK}" stroke-width="3" stroke-linecap="round"/></svg>'
            f'<div style="font-size:27px;line-height:1.35"><b>{t}</b> <span style="color:#3A4552">{ej}</span></div></div>')
filas = (no("El nombre común de lo que vendes.", "«Panadería» para una panadería.") +
         no("Lo que solo describe.", "«Deliciosas» para unas galletas.") +
         no("Letras, números o colores solos.", "Sin nada más que los distinga.") +
         no("Lo que se parece a otra marca", "ya registrada o pedida antes, para productos o servicios iguales o parecidos.") +
         no("Lo que se pide de mala fe.", "Por ejemplo, para quitarle el nombre a su dueño."))
S.append(("Leg2-04-NoSe", page("Lo que no se registra", "bg-papel", INK, f"""
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:#5F7E9E;font-weight:700">ANTES DE ENAMORARTE DEL NOMBRE</div>
<h2 class="serif" style="margin:22px 0 0;width:560px;font-size:80px;line-height:0.96;color:#2B3542">Esto <span style="background:linear-gradient(transparent 12%,#D9B4A8 12%,#D9B4A8 90%,transparent 90%);padding:0 8px">no</span> se puede registrar</h2>
</div>
<div style="position:absolute;left:700px;top:70px;width:300px;box-sizing:border-box;padding:12px 12px 56px;background:#FFFFFF;transform:rotate(5deg);box-shadow:0 18px 34px rgba(30,36,44,0.28)">
<img src="{NARANJAS}" alt="Naranjas apiladas en un puesto de mercado" style="display:block;width:100%;height:290px;object-fit:cover">
<div style="position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:22px;font-weight:600;color:#2B3542">«Naranjas»… para naranjas</div>
</div>
{G.tape(780, 52, 140, -5)}
<div class="hoja" style="position:absolute;left:90px;right:90px;top:470px;padding:14px 40px;box-shadow:0 16px 30px rgba(30,36,44,0.14);transform:rotate(-0.6deg)">{filas}</div>
<div style="position:absolute;left:90px;right:90px;top:1010px;display:flex;gap:20px;align-items:flex-start;padding:28px 32px;background:#2B3542;color:#F4F1EA;transform:rotate(0.6deg);box-shadow:0 16px 30px rgba(30,36,44,0.2)">
<svg aria-hidden="true" width="38" height="38" viewBox="0 0 24 24" fill="#B7CFE6" style="flex:none;margin-top:3px"><circle cx="12" cy="12" r="11"/><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#262F3B" stroke-width="2.4" stroke-linecap="round"/></svg>
<div style="font-size:27px;line-height:1.4">Por eso conviene <b>buscar antes de invertir</b> en logo, letreros, empaques y letreros de la fachada: si el nombre choca con otro, el IMPI te lo puede negar.</div>
</div>
{foot("Fuente: art. 173 fr. I, IV, V, XVIII y XXII LFPPI · " + H, 4, TOT)}""")))

# 5. Pasos (degradado salvia, claro)
pasos = [("Busca que esté libre", "Revisa en Marcanet, la base pública del IMPI, si ya existe algo igual o parecido."),
         ("Ubica tus productos o servicios", "Cada marca se pide para productos o servicios específicos; el IMPI los ordena por clases (ClasNiza)."),
         ("Presenta la solicitud", "Datos y correo del solicitante, la imagen de la marca, la fecha de primer uso (o que aún no la usas) y qué vas a vender con ella."),
         ("Dale seguimiento", "El IMPI puede pedirte aclaraciones con plazo. Contesta a tiempo hasta recibir tu título.")]
pp = "".join(
    f'<div style="display:flex;gap:26px;align-items:flex-start;padding:22px 0;border-bottom:1px solid rgba(30,36,44,0.16)">'
    f'<div class="serif" style="flex:none;width:76px;height:76px;border-radius:50%;background:#2B3542;color:#F4F1EA;display:flex;align-items:center;justify-content:center;font-size:44px;line-height:1">{i+1}</div>'
    f'<div><div class="serif" style="font-size:44px;line-height:1;color:#2B3542">{t}</div><div style="font-size:26px;line-height:1.4;margin-top:10px;color:#2B3542">{d}</div></div></div>'
    for i, (t, d) in enumerate(pasos))
S.append(("Leg2-05-Pasos", page("Cómo se registra", "", INK, f"""
{M.grad("salvia")}
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:#2B3542;font-weight:700">PASO A PASO</div>
<h2 class="serif" style="margin:22px 0 22px;font-size:84px;line-height:0.96;color:#2B3542">Cómo se pide <span style="background:#FFFDF8;padding:0 10px">al IMPI</span></h2>
{pp}
<div style="margin-top:44px;padding:34px 38px;background:#2B3542;color:#F4F1EA;transform:rotate(-0.8deg);box-shadow:0 18px 32px rgba(30,36,44,0.22)">
<div class="kicker" style="font-size:19px;color:#B7CFE6">OJO CON ESTO</div>
<div style="font-size:28px;line-height:1.42;margin-top:14px">No basta con que no exista el nombre <b>idéntico</b>: también cuenta lo que se <b>parezca</b> y se venda en lo mismo. Por eso la búsqueda se hace con calma.</div>
</div>
</div>
{foot("Fuente: arts. 214 y 220 LFPPI; marcanet.impi.gob.mx · " + H, 5, TOT)}""", " isolation: isolate;")))

# 6. Línea de vida (terracota liso) con "10" gigante
hitos = [("0", "Te la otorgan", "Empieza a correr la vigencia."),
         ("3", "Declara que la usas", "Dentro de los 3 meses siguientes a que cumpla 3 años. Si no, caduca sola."),
         ("10", "Renuévala", "En los 6 meses antes de que venza (hay 6 meses de gracia después), declarando otra vez su uso.")]
hh = "".join(
    f'<div style="position:relative;display:flex;gap:28px;align-items:flex-start;padding-bottom:34px">'
    f'<div style="flex:none;width:96px;height:96px;border-radius:50%;background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:1;box-shadow:0 10px 20px rgba(30,36,44,0.18)">'
    f'<div class="serif" style="font-size:44px;line-height:0.9">{a}</div><div style="font-size:14px;font-weight:700;letter-spacing:0.18em">AÑO{"" if a=="1" else "S"}</div></div>'
    f'<div style="padding-top:8px"><div class="serif" style="font-size:46px;line-height:1;color:{INK}">{t}</div><div style="font-size:26px;line-height:1.4;margin-top:8px;color:#2B3542">{d}</div></div></div>'
    for (a, t, d), (bg, fg) in zip(hitos, [("#F4F1EA", INK), ("#B7CFE6", INK), ("#2B3542", "#F4F1EA")]))
S.append(("Leg2-06-Vigencia", page("Vigencia", "", INK, f"""
<div class="serif" aria-hidden="true" style="position:absolute;right:-40px;top:-120px;font-size:720px;line-height:1;color:rgba(255,253,248,0.32)">10</div>
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:#2B3542;font-weight:700">REGISTRARLA NO ES PARA SIEMPRE</div>
<h2 class="serif" style="margin:22px 0 10px;width:700px;font-size:96px;line-height:0.94;color:#2B3542">Dura <span style="background:#F4F1EA;padding:0 10px">10 años</span>… si la cuidas</h2>
<p style="margin:0 0 44px;width:640px;font-size:29px;line-height:1.4;color:#2B3542">Y se renueva por periodos iguales. Apunta estas fechas:</p>
<div style="position:relative">
<div aria-hidden="true" style="position:absolute;left:46px;top:20px;bottom:60px;border-left:4px dashed rgba(43,53,66,0.45)"></div>
{hh}
</div>
<div class="hoja" style="margin-top:14px;padding:34px 38px;color:{INK};transform:rotate(0.7deg);box-shadow:0 16px 30px rgba(30,36,44,0.18)">
<div class="kicker" style="font-size:19px;color:#C98F7E">SI SE TE PASA</div>
<div style="font-size:28px;line-height:1.42;margin-top:14px">El registro <b>caduca solo</b>: no te llega ningún aviso y, una vez libre, alguien más puede pedir tu nombre. Guarda las fechas en tu calendario.</div>
</div>
</div>
{foot("Fuente: arts. 178, 233 y 237 LFPPI · " + H, 6, TOT)}""", " background: #D9B4A8;")))

# 7. Cierre
S.append(("Leg2-07-Cierre", cierre("¿Ya registraste", "tu marca?",
    "En GGTZ te ayudamos con tu empresa: constitución, marcas, contratos y temas laborales.",
    "Agenda tu asesoría", "Comenta <b>MARCA</b> y guarda este post para cuando la vayas a pedir.", fondo="atardecer")))

for name, html in S:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok", len(S))

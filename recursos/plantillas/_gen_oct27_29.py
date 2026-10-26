# Carruseles del martes 27 oct ("¿El SAT ve tu cuenta de banco?", Ban-*) y jueves 29 oct
# ("Último aviso: regularización del SAT", Reg-*). Identidad de marca: Archivo ExtraBold, degradados, sello BL, cierre "revista".
# Fuentes: LISR art. 55 (fr. I y IV) y art. 91 (Luthor, corte 20 oct 2026); comunicado SAT 7 oct 2026 vía Expansión y UnoTV.
import importlib.util as _u, pathlib
HERE = pathlib.Path(__file__).parent
def _load(n):
    s = _u.spec_from_file_location(n, HERE / f"{n}.py"); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
G = _load("_gen_oct20_22"); M = _load("_marca")
page, foot, cierre = G.page, G.foot, G.cierre
H = "@bernardolatorre.fiscal"
ISO = " isolation: isolate;"
BL = lambda i: f"/_blob/{i}"
BILLETES = BL("29e4c8d2580b23552880ae35ab069428")
FAMILIA = BL("faddc9c76095ba578488017124a3ec07")
CALCU = BL("5a1a8dcde3274fba772abbf2746128b4")
SATCAP = BL("0adc0a675d66cb76d2f8d28aa693463f")

def sello(src=M.SELLO_MARFIL, x=880, y=80, s=120, r=-8):
    return f'<img src="{src}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;left:{x}px;top:{y}px;width:{s}px;transform:rotate({r}deg)">'

def foto_pol(src, cap, x, y, w, h, rot, pos="50% 50%", alt=""):
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;box-sizing:border-box;padding:14px 14px 64px;background:#FFFDF8;transform:rotate({rot}deg);box-shadow:0 20px 38px rgba(20,24,30,0.35)">'
            f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:{h}px;object-fit:cover;object-position:{pos}">'
            f'<div class="serif" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:28px;color:#262F3B">{cap}</div></div>')

def tag(t, c):
    return f'<div class="kicker" style="font-weight:700;color:{c}">{t}</div>'

# =========================== MARTES 27: ¿El SAT ve tu cuenta de banco? ===========================
T = 8
B = []

# 1 Portada: degradado noche + estado de cuenta rotado con una lupa encima (motivo: lupa/estado de cuenta, nuevo)
filas = "".join(
    f'<div style="display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(43,53,66,0.14);font-size:22px;{st}"><span>{a}</span><span>{b}</span></div>'
    for a, b, st in [("TRANSFERENCIA SPEI", "$4,800.00", ""), ("PAGO TARJETA", "-$1,250.00", ""),
                     ("DEPÓSITO EN EFECTIVO", "$16,000.00", "background:#B7CFE6;margin:0 -16px;padding:14px 16px;font-weight:700"),
                     ("TRASPASO PROPIO", "$2,000.00", ""), ("COMPRA EN LÍNEA", "-$689.00", "")])
B.append(("Ban-01-Portada", page("¿El SAT ve tu cuenta de banco?", "", "#F4F1EA", f"""
{M.grad("noche")}
{sello()}
<div style="position:absolute;left:90px;top:100px">{tag("TU DINERO Y EL SAT", "rgba(244,241,234,0.85)")}</div>
<h1 class="serif" style="position:absolute;left:90px;right:90px;top:190px;margin:0;font-size:112px;line-height:0.94">¿El SAT ve tu <span style="color:#B7CFE6">cuenta de banco?</span></h1>
<div style="position:absolute;left:150px;top:640px;width:640px;box-sizing:border-box;padding:34px 40px 30px;background:#FFFDF8;color:#262F3B;transform:rotate(-4deg);box-shadow:0 26px 50px rgba(0,0,0,0.45)">
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span class="serif" style="font-size:34px">Estado de cuenta</span><span style="font-size:18px;letter-spacing:0.18em;color:#5F7E9E">OCTUBRE</span></div>
{filas}</div>
<svg aria-hidden="true" width="340" height="340" viewBox="0 0 340 340" style="position:absolute;left:600px;top:760px;filter:drop-shadow(0 18px 26px rgba(0,0,0,0.45))">
<circle cx="130" cy="130" r="98" fill="rgba(183,207,230,0.18)" stroke="#F4F1EA" stroke-width="18"/>
<path d="M200 200 L300 300" stroke="#F4F1EA" stroke-width="34" stroke-linecap="round"/></svg>
<p style="position:absolute;left:90px;right:420px;bottom:150px;margin:0;font-size:30px;line-height:1.4;color:rgba(244,241,234,0.88)">Lo que el banco sí le reporta, lo que no, y cuándo sí te debe preocupar.</p>
{foot(H, 1, T, True)}""", ISO)))

# 2 Respuesta corta (sarga + polaroid de billetes)
B.append(("Ban-02-Corta", page("La respuesta corta", "bg-sarga", "#F4F1EA", f"""
<div style="position:absolute;left:90px;top:110px;right:90px">{tag("LA RESPUESTA CORTA", "#B7CFE6")}
<h2 class="serif" style="margin:26px 0 0;font-size:86px;line-height:0.98">No ve tus movimientos en vivo… <span style="color:#B7CFE6">pero sí le llegan reportes.</span></h2>
<p style="margin:34px 0 0;max-width:820px;font-size:32px;line-height:1.45;color:rgba(244,241,234,0.86)">Los bancos tienen obligaciones de informarle al SAT. Y si un día te revisa, tus estados de cuenta son lo primero que va a mirar.</p></div>
{foto_pol(BILLETES, "el efectivo deja huella", 470, 760, 470, 360, 5, "50% 40%", "Billetes de 500 pesos")}
{G.tape(600, 742, 190, -4)}
{foot("Arts. 55 y 91 LISR", 2, T, True)}""")))

# 3 Lo que el banco SÍ reporta (papel)
items = [("Depósitos en efectivo", "cuando en el mes suman más de <b>$15,000</b> en todas tus cuentas del mismo banco. Se reporta cada mes, a más tardar el día 17."),
         ("Cheques de caja", "todos los que compres en efectivo."),
         ("Intereses", "lo que te paga tu inversión, cada año a más tardar el 15 de febrero.")]
fil = "".join(f'<div style="display:flex;gap:26px;padding:26px 0;border-bottom:1px solid rgba(43,53,66,0.15)"><div style="flex:none">{G.num_badge(i+1)}</div><div><div class="serif" style="font-size:44px;line-height:1">{a}</div><div style="margin-top:10px;font-size:29px;line-height:1.42;color:#2B3542">{b}</div></div></div>' for i, (a, b) in enumerate(items))
B.append(("Ban-03-Reporta", page("Lo que sí reporta", "bg-papel", "#1E242C", f"""
<div style="position:absolute;left:90px;right:90px;top:110px">{tag("LO QUE EL BANCO SÍ LE AVISA AL SAT", "#5F7E9E")}
<h2 class="serif" style="margin:24px 0 20px;font-size:84px;line-height:0.98">3 cosas que <span style="background:linear-gradient(transparent 12%,#B7CFE6 12%,#B7CFE6 90%,transparent 90%);padding:0 8px">sí se reportan</span></h2>
<div style="background:#FFFDF8;padding:6px 40px;box-shadow:0 16px 30px rgba(30,36,44,0.14);transform:rotate(-0.6deg)">{fil}</div></div>
{foot("Art. 55, fracciones I y IV LISR", 3, T)}""")))

# 4 Lo que NO es depósito en efectivo (salvia)
B.append(("Ban-04-NoCuenta", page("Lo que no cuenta", "", "#1E242C", f"""
{M.grad("salvia")}
<div style="position:absolute;left:90px;right:90px;top:120px">{tag("Y AQUÍ VIENE EL MATIZ", "#2B3542")}
<h2 class="serif" style="margin:26px 0 30px;font-size:88px;line-height:0.96">Las transferencias <span style="background:#FFFDF8;padding:0 10px">no entran</span> en ese reporte</h2>
<p style="margin:0;font-size:32px;line-height:1.45;color:#2B3542;max-width:860px">Para la ley, no son depósitos en efectivo las transferencias electrónicas, los traspasos entre cuentas ni los cheques.</p>
<div style="margin-top:46px;display:flex;gap:18px;flex-wrap:wrap">
{''.join(f'<span style="padding:16px 26px;border:2px solid #262F3B;border-radius:999px;font-size:26px;font-weight:700">{c}</span>' for c in ["SPEI", "Traspasos", "Cheques"])}</div>
<div style="margin-top:60px;padding:30px 36px;background:#262F3B;color:#F4F1EA;transform:rotate(-1deg);max-width:820px;font-size:30px;line-height:1.42">Ojo: que no estén en ESE reporte no quiere decir que el SAT no las pueda conocer si te revisa.</div></div>
{foot("Art. 55, último párrafo LISR", 4, T)}""", ISO)))

# 5 Discrepancia fiscal (sierra)
B.append(("Ban-05-Discrepancia", page("Discrepancia fiscal", "", "#F4F1EA", f"""
{M.grad("sierra")}
<div style="position:absolute;left:90px;right:90px;top:130px">{tag("LO QUE SÍ TE DEBE PREOCUPAR", "rgba(244,241,234,0.85)")}
<h2 class="serif" style="margin:26px 0 0;font-size:100px;line-height:0.94">Gastar más de lo que <span style="color:#B7CFE6">declaras</span></h2>
<p style="margin:34px 0 0;font-size:32px;line-height:1.45;color:rgba(244,241,234,0.9);max-width:860px">Se llama <b>discrepancia fiscal</b>. Si en un año tus gastos, compras, depósitos, inversiones y pagos de tarjeta suman más que tus ingresos declarados, el SAT puede presumir que la diferencia es ingreso que no declaraste.</p></div>
<div style="position:absolute;left:90px;right:90px;bottom:170px;display:flex;align-items:flex-end;gap:40px">
<div style="flex:1"><div style="height:150px;background:rgba(244,241,234,0.85)"></div><div style="margin-top:12px;font-size:24px;font-weight:700;letter-spacing:0.12em">LO QUE DECLARAS</div></div>
<div style="flex:1"><div style="height:290px;background:#B7CFE6;position:relative"><div class="serif" style="position:absolute;top:-70px;left:0;font-size:60px;color:#B7CFE6">?</div></div><div style="margin-top:12px;font-size:24px;font-weight:700;letter-spacing:0.12em">LO QUE GASTAS</div></div></div>
{foot("Art. 91 LISR", 5, T, True)}""", ISO)))

# 6 Lo que no se considera (foto familia + texto)
B.append(("Ban-06-Familia", page("Traspasos a familia", "bg-lino", "#1E242C", f"""
<div style="position:absolute;left:90px;right:90px;top:110px">{tag("TRANQUILO, ESTO NO SE CUENTA", "#5F7E9E")}
<h2 class="serif" style="margin:24px 0 0;font-size:80px;line-height:0.98">Pasarte dinero <span style="background:linear-gradient(transparent 12%,#A9C9A9 12%,#A9C9A9 90%,transparent 90%);padding:0 8px">entre los tuyos</span></h2>
<p style="margin:28px 0 0;font-size:30px;line-height:1.45;color:#2B3542;max-width:520px">En la discrepancia no cuentan los traspasos entre tus propias cuentas ni a las de tu cónyuge, papás o hijos.</p>
<p style="margin:22px 0 0;font-size:30px;line-height:1.45;color:#2B3542;max-width:520px">Tampoco lo que depositas a otra persona si demuestras que fue un pago por algo que compraste o rentaste.</p></div>
{foto_pol(FAMILIA, "papás, hijos y cónyuge", 620, 470, 380, 470, 4, "50% 35%", "Familia al aire libre")}
{G.tape(720, 455, 170, -6, "rgba(169,201,169,0.9)")}
{foot("Art. 91, cuarto párrafo LISR", 6, T)}""")))

# 7 Si te llega el oficio (papel blanco, 20 días)
pasos = ["Te notifican cuánto detectaron y de dónde salió el dato.",
         "Tienes <b>20 días</b> para explicar por escrito el origen del dinero y dar pruebas.",
         "Si no lo explicas, la diferencia se te cobra como ingreso omitido."]
lis = "".join(f'<div style="display:flex;gap:22px;align-items:flex-start;padding:22px 0;border-bottom:1px solid rgba(43,53,66,0.15)"><span class="serif" style="font-size:48px;line-height:1;color:#5F7E9E;width:56px">{i+1}</span><div style="font-size:30px;line-height:1.42">{p}</div></div>' for i, p in enumerate(pasos))
B.append(("Ban-07-Oficio", page("Si te llega el oficio", "hoja", "#1E242C", f"""
<div style="position:absolute;left:90px;right:90px;top:110px">{tag("SI TE LLEGA UNA DISCREPANCIA", "#C98F7E")}
<div style="display:flex;align-items:baseline;gap:24px;margin-top:10px"><span class="serif" style="font-size:250px;line-height:0.85;color:#262F3B">20</span><span class="serif" style="font-size:64px;line-height:1">días para<br>responder</span></div>
<div style="margin-top:20px">{lis}</div>
<div style="margin-top:34px;padding:26px 32px;background:#262F3B;color:#F4F1EA;font-size:28px;line-height:1.42">Guarda contratos, CFDI y estados de cuenta, y declara en tu anual los préstamos y donativos que la ley te pide informar.</div></div>
{foot("Art. 91, fracción II LISR", 7, T)}""")))

# 8 Cierre
B.append(("Ban-08-Cierre", cierre("¿Tu cuenta y tu declaración", "cuadran?",
    "Antes de que el SAT te pregunte, revisamos juntos que tus ingresos, gastos y depósitos cuenten la misma historia.",
    "Agenda tu asesoría", "Guárdalo y compártelo con quien deposita todo en efectivo.", fondo="atardecer")))

# =========================== JUEVES 29: Último aviso regularización ===========================
T2 = 7
R = []

# 1 Portada: neblina + hoja de calendario arrancable "31 OCT"
R.append(("Reg-01-Portada", page("Último aviso: regularización SAT", "", "#F4F1EA", f"""
{M.grad("neblina")}
{sello()}
<div style="position:absolute;left:90px;top:100px">{tag("ÚLTIMO AVISO", "#D9B4A8")}</div>
<h1 class="serif" style="position:absolute;left:90px;right:90px;top:180px;margin:0;font-size:104px;line-height:0.95">Se acaba el <span style="color:#B7CFE6">perdón de multas</span> del SAT</h1>
<div style="position:absolute;left:560px;top:560px;width:380px;transform:rotate(5deg);box-shadow:0 26px 50px rgba(0,0,0,0.4)">
<div style="background:#C98F7E;color:#FFFDF8;text-align:center;padding:18px 0;font-size:30px;font-weight:700;letter-spacing:0.3em">OCTUBRE</div>
<div style="background:#FFFDF8;color:#262F3B;text-align:center;padding:10px 0 34px;position:relative">
<div class="serif" style="font-size:250px;line-height:1">31</div><div style="font-size:26px;font-weight:700;letter-spacing:0.24em;color:#5F7E9E">SÁBADO</div>
<div aria-hidden="true" style="position:absolute;left:0;right:0;top:0;height:12px;background:repeating-linear-gradient(90deg,#C98F7E 0 14px,transparent 14px 28px)"></div></div></div>
<p style="position:absolute;left:90px;width:420px;top:620px;margin:0;font-size:32px;line-height:1.42;color:#F4F1EA"><b>Te quedan 2 días</b> para pedir hasta el 100% de descuento en multas y recargos.</p>
{foot(H, 1, T2)}""", ISO)))

# 2 Qué es (sarga + polaroid calculadora)
R.append(("Reg-02-Que", page("Qué es", "bg-sarga", "#F4F1EA", f"""
<div style="position:absolute;left:90px;right:90px;top:110px">{tag("¿DE QUÉ SE TRATA?", "#B7CFE6")}
<h2 class="serif" style="margin:26px 0 0;font-size:84px;line-height:0.98">Pagas el impuesto, y el SAT te quita <span style="color:#B7CFE6">lo que se le colgó encima</span></h2>
<p style="margin:34px 0 0;max-width:520px;font-size:31px;line-height:1.45;color:rgba(244,241,234,0.88)">El Programa de Regularización Fiscal 2026 da hasta <b>100% de descuento</b> en multas, recargos y gastos de ejecución de adeudos de 2024 o años anteriores.</p></div>
{foto_pol(CALCU, "hasta 100% menos", 600, 640, 380, 380, 4, "60% 50%", "Calculadora sobre un escritorio")}
{G.tape(700, 625, 170, -5)}
{foot("Comunicado SAT, 7 oct 2026", 2, T2, True)}""")))

# 3 Quién puede entrar (papel checklist)
si = ["Ingresos de 2024 de hasta <b>$300 millones</b>", "Adeudos de <b>2024 o años anteriores</b>", "Aunque ya te estén revisando o tengas un crédito fiscal firme"]
no = ["Estar en las listas del 69-B", "Haber usado el beneficio de 2025", "Tener un juicio contra el SAT (tendrías que desistirte)"]
ck = lambda t, ok: f'<div style="display:flex;gap:18px;align-items:flex-start;padding:14px 0;font-size:28px;line-height:1.38"><svg aria-hidden="true" width="34" height="34" viewBox="0 0 34 34" style="flex:none;margin-top:3px"><circle cx="17" cy="17" r="16" fill="{"#A9C9A9" if ok else "#D9B4A8"}"/><path d="{"M10 17l5 5 9-10" if ok else "M11 11l12 12M23 11L11 23"}" fill="none" stroke="#1E242C" stroke-width="3"/></svg><div>{t}</div></div>'
R.append(("Reg-03-Quien", page("Quién puede entrar", "bg-papel", "#1E242C", f"""
<div style="position:absolute;left:90px;right:90px;top:100px">{tag("¿TE TOCA?", "#5F7E9E")}
<h2 class="serif" style="margin:22px 0 24px;font-size:84px;line-height:0.98">Quién <span style="background:linear-gradient(transparent 12%,#B7CFE6 12%,#B7CFE6 90%,transparent 90%);padding:0 8px">sí puede entrar</span></h2>
<div style="background:#FFFDF8;padding:22px 40px;box-shadow:0 16px 30px rgba(30,36,44,0.14);transform:rotate(-0.6deg)">{''.join(ck(t, True) for t in si)}</div>
<div class="kicker" style="margin:40px 0 10px;font-weight:700;color:#C98F7E">NO APLICA SI…</div>
<div style="padding:0 6px">{''.join(ck(t, False) for t in no)}</div></div>
{foot("Comunicado SAT, 7 oct 2026", 3, T2)}""")))

# 4 Sí / No te perdonan (salvia)
R.append(("Reg-04-SiNo", page("Qué te perdonan", "", "#1E242C", f"""
{M.grad("salvia")}
<div style="position:absolute;left:90px;right:90px;top:300px">{tag("LO QUE CASI NADIE ENTIENDE", "#2B3542")}
<h2 class="serif" style="margin:24px 0 46px;font-size:88px;line-height:0.96">El impuesto <span style="background:#FFFDF8;padding:0 10px">no se perdona</span></h2>
<div style="display:flex;gap:28px">
<div style="flex:1;background:#262F3B;color:#F4F1EA;padding:36px 34px;transform:rotate(-1.5deg)"><div class="serif" style="font-size:46px;color:#A9C9A9">Sí</div>
<div style="margin-top:18px;font-size:30px;line-height:1.6">Multas<br>Recargos<br>Gastos de ejecución</div></div>
<div style="flex:1;background:#FFFDF8;padding:36px 34px;transform:rotate(1.5deg);box-shadow:0 14px 28px rgba(30,36,44,0.12)"><div class="serif" style="font-size:46px;color:#C98F7E">No</div>
<div style="margin-top:18px;font-size:30px;line-height:1.6">El ISR, IVA o impuesto que debes: ese se paga completo y actualizado</div></div></div></div>
{foot("Comunicado SAT, 7 oct 2026", 4, T2)}""", ISO)))

# 5 Cómo se pide (noche + captura del portal)
pasos2 = ["Entra a <b>sat.gob.mx</b> con tu RFC y contraseña.", "Desde Mi portal manda un <b>escrito libre</b> pidiendo el beneficio.", "Espera la respuesta del SAT.", "Paga lo que te indiquen dentro del plazo."]
pl = "".join(f'<div style="display:flex;gap:18px;padding:16px 0;border-bottom:1px solid rgba(244,241,234,0.18);font-size:28px;line-height:1.4"><span class="serif" style="color:#B7CFE6;font-size:36px;width:40px">{i+1}</span><div>{p}</div></div>' for i, p in enumerate(pasos2))
R.append(("Reg-05-Como", page("Cómo se pide", "", "#F4F1EA", f"""
{M.grad("noche")}
<div style="position:absolute;left:90px;top:110px;width:520px">{tag("CÓMO SE PIDE", "rgba(244,241,234,0.85)")}
<h2 class="serif" style="margin:24px 0 26px;font-size:80px;line-height:0.96">En línea, en <span style="color:#B7CFE6">4 pasos</span></h2>{pl}
<p style="margin:24px 0 0;font-size:24px;line-height:1.4;color:rgba(244,241,234,0.7)">También puedes ir a una oficina del SAT.</p></div>
<div style="position:absolute;left:640px;top:300px;width:370px;padding:14px;background:#111;border-radius:44px;transform:rotate(4deg);box-shadow:0 26px 50px rgba(0,0,0,0.5)">
<img src="{SATCAP}" alt="Captura del portal del SAT en el celular" style="display:block;width:100%;height:auto;border-radius:32px"></div>
{foot("Comunicado SAT, 7 oct 2026", 5, T2, True)}""", ISO)))

# 6 Después del 31 (terracota liso, urgencia)
R.append(("Reg-06-Despues", page("Después del 31", "", "#1E242C", f"""
<div style="position:absolute;inset:0;background:#D9B4A8"></div>
<div style="position:absolute;left:90px;right:90px;top:150px">{tag("¿Y SI NO ALCANZO?", "#262F3B")}
<h2 class="serif" style="margin:26px 0 0;font-size:96px;line-height:0.95">El 1 de noviembre todo <span style="background:#FFFDF8;padding:0 10px">vuelve a contar</span></h2>
<p style="margin:40px 0 0;font-size:32px;line-height:1.45;max-width:860px">Cuando cierre, tu adeudo sigue sumando recargos. La Ley de Ingresos 2027 trae otro programa, pero todavía no es ley y sus reglas pueden cambiar. Si tienes algo pendiente con el SAT, estos dos días valen oro.</p>
<div style="margin-top:56px;display:inline-block;padding:22px 30px;border:4px solid #262F3B;border-radius:10px;transform:rotate(-3deg);font-size:30px;font-weight:700;letter-spacing:0.16em">CIERRA EL SÁBADO 31</div></div>
{sello(M.SELLO_PIZARRA, 870, 1080, 110, 6)}
{foot(H, 6, T2)}""")))

# 7 Cierre
R.append(("Reg-07-Cierre", cierre("¿Algo pendiente", "con el SAT?",
    "Revisamos tu caso esta semana y te decimos si te conviene entrar al programa antes del 31.",
    "Agenda tu asesoría", "Compártelo con quien trae adeudos con el SAT: le puede ahorrar mucho.", fondo="atardecer")))

for name, html in B + R:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok", len(B), len(R))

# Lunes legal #1 (19 oct 2026): "¿Tu equipo trabaja sin contrato?" (Leg1-*).
# Fuente: LFT arts. 24, 25, 26, 35, 39-A y 784 (verificados en Luthor, corte 17 oct 2026).
import importlib.util as _u, pathlib
HERE = pathlib.Path(__file__).parent
def _load(n):
    s = _u.spec_from_file_location(n, HERE / f"{n}.py"); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
G = _load("_gen_oct20_22"); M = _load("_marca")
page, foot, cierre = G.page, G.foot, G.cierre
TOT = 7
TAG = '<div class="kicker" style="font-weight:700">⚖️ LUNES LEGAL</div>'
MANO = "/_blob/f6ef9d166eaf01db13ae40b4bfb2954d"
PILAS = "/_blob/ca63cdca5b3b1bd737eae1c366d66408"
H = "@bernardolatorre.fiscal"
S = []

# 1. Portada (sierra)
S.append(("Leg1-01-Portada", page("Lunes legal: contrato laboral", "", "#F4F1EA", f"""
{M.grad("sierra")}
<img src="{M.SELLO_MARFIL}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;right:80px;top:80px;width:130px;transform:rotate(-8deg)">
<div style="position:absolute;left:90px;top:110px;color:rgba(244,241,234,0.9)">{TAG}</div>
<h1 class="serif" style="position:absolute;left:90px;right:90px;top:520px;margin:0;font-size:116px;line-height:0.94">¿Tu equipo trabaja <span style="color:#B7CFE6">sin contrato?</span></h1>
<p style="position:absolute;left:90px;right:200px;top:900px;margin:0;font-size:34px;line-height:1.4;color:rgba(244,241,234,0.88)">Lo que dice la Ley Federal del Trabajo y por qué te conviene ponerlo por escrito.</p>
{foot(H, 1, TOT, True)}""", " isolation: isolate;")))

# 2. Mito (foto firmando)
S.append(("Leg1-02-Mito", page("Mito", "", "#F4F1EA", f"""
<img src="{MANO}" alt="Mano firmando un documento" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 40%">
<div aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,27,35,0.15) 0%,rgba(21,27,35,0.55) 40%,rgba(21,27,35,0.94) 70%)"></div>
<div style="position:absolute;left:90px;right:90px;bottom:150px;display:flex;flex-direction:column;gap:30px">
<div class="kicker" style="color:#D9B4A8;font-weight:700">EL MITO</div>
<h2 class="serif" style="margin:0;font-size:84px;line-height:0.98">"Si no firmamos nada, <span style="color:#B7CFE6">no hay relación laboral</span>"</h2>
<p style="margin:0;font-size:32px;line-height:1.45;color:rgba(244,241,234,0.9)"><b>Falso.</b> Si no hay contrato escrito, el trabajador conserva todos sus derechos y la falta se le imputa al patrón.</p>
<div style="font-size:22px;color:rgba(244,241,234,0.65)">Art. 26, Ley Federal del Trabajo</div>
</div>
{foot(H, 2, TOT, True)}""")))

# 3. Carga de la prueba (foto expedientes)
S.append(("Leg1-03-Prueba", page("Carga de la prueba", "", "#F4F1EA", f"""
<img src="{PILAS}" alt="Pilas de expedientes en una oficina" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(0.6)">
<div aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,27,35,0.92) 0%,rgba(21,27,35,0.7) 45%,rgba(21,27,35,0.2) 100%)"></div>
<div style="position:absolute;left:90px;right:90px;top:130px;display:flex;flex-direction:column;gap:30px">
<div class="kicker" style="color:#B7CFE6;font-weight:700">SI LLEGA A UN JUICIO</div>
<h2 class="serif" style="margin:0;font-size:96px;line-height:0.95">El que tiene que probar <span style="background:#B7CFE6;color:#1E242C;padding:0 12px">eres tú</span></h2>
<p style="margin:0;max-width:820px;font-size:32px;line-height:1.45;color:rgba(244,241,234,0.92)">Cuando hay controversia, la ley le pide al patrón demostrar las condiciones de trabajo con documentos. Sin contrato, te quedas sin tu mejor prueba.</p>
<div style="font-size:22px;color:rgba(244,241,234,0.7)">Art. 784, Ley Federal del Trabajo</div>
</div>
{foot(H, 3, TOT, True)}""")))

# 4. Lo que tendrías que probar (noche)
items = ["Fecha de ingreso y antigüedad", "El contrato de trabajo", "Monto y pago del salario", "Jornada y horas extra",
         "Vacaciones, prima vacacional y aguinaldo", "PTU", "Alta y aportaciones al IMSS, Infonavit y SAR"]
chips = "".join(f'<div style="display:flex;gap:22px;align-items:center;padding:20px 0;border-bottom:1px solid rgba(244,241,234,0.18);font-size:32px"><span class="serif" style="color:#B7CFE6;font-size:34px;width:46px">{i+1:02d}</span>{t}</div>' for i, t in enumerate(items))
S.append(("Leg1-04-Lista", page("Qué te toca probar", "", "#F4F1EA", f"""
{M.grad("noche")}
<div style="position:absolute;left:90px;right:90px;top:110px">
<div class="kicker" style="color:rgba(244,241,234,0.8);font-weight:700">ALGUNAS COSAS QUE TE TOCA PROBAR</div>
<h2 class="serif" style="margin:28px 0 36px;font-size:80px;line-height:0.98">Y todo empieza por <span style="background:#B7CFE6;color:#1E242C;padding:0 12px">el papel</span></h2>
{chips}
</div>
{foot("Art. 784 LFT", 4, TOT, True)}""", " isolation: isolate;")))

# 5. Qué debe decir (marfil papel)
req = [("Datos de ambos", "nombre, CURP, RFC y domicilio del trabajador y del patrón"),
       ("Tipo de relación", "tiempo indeterminado, obra o tiempo determinado, temporada; si hay periodo de prueba"),
       ("Puesto y lugar", "qué va a hacer y dónde"),
       ("Jornada y salario", "horario, monto, forma, día y lugar de pago"),
       ("Capacitación", "que se le capacitará conforme a la ley"),
       ("Descanso y vacaciones", "y demás condiciones que acuerden"),
       ("Beneficiarios", "quién cobra lo pendiente si el trabajador fallece")]
filas = "".join(f'<div style="display:flex;gap:20px;align-items:flex-start;padding:15px 0;border-bottom:1px solid rgba(43,53,66,0.15)"><svg aria-hidden="true" width="34" height="34" viewBox="0 0 34 34" style="flex:none;margin-top:4px"><circle cx="17" cy="17" r="16" fill="#A9C9A9"/><path d="M10 17l5 5 9-10" fill="none" stroke="#1E242C" stroke-width="3"/></svg><div style="font-size:28px;line-height:1.35"><b>{a}:</b> {b}</div></div>' for a, b in req)
S.append(("Leg1-05-Checklist", page("Qué debe decir", "bg-papel", "#1E242C", f"""
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:#5F7E9E;font-weight:700">CHECKLIST</div>
<h2 class="serif" style="margin:22px 0 26px;font-size:78px;line-height:0.98">Lo que debe decir <span style="background:linear-gradient(transparent 12%,#B7CFE6 12%,#B7CFE6 90%,transparent 90%);padding:0 8px">tu contrato</span></h2>
<div style="background:#FFFDF8;padding:16px 36px;box-shadow:0 16px 30px rgba(30,36,44,0.14);transform:rotate(-0.6deg)">{filas}</div>
</div>
{foot("Art. 25 LFT", 5, TOT)}""")))

# 6. Plazo y periodo de prueba (salvia)
S.append(("Leg1-06-Plazos", page("Plazos", "", "#1E242C", f"""
{M.grad("salvia")}
<div style="position:absolute;left:90px;right:90px;top:120px;display:flex;flex-direction:column;gap:40px">
<div class="kicker" style="color:#2B3542;font-weight:700">2 DETALLES QUE CASI NADIE CUIDA</div>
<div>
<h2 class="serif" style="margin:0 0 18px;font-size:76px;line-height:0.98">Si no dices el plazo, <span style="background:#FFFDF8;padding:0 10px">es indefinido</span></h2>
<p style="margin:0;font-size:31px;line-height:1.45;color:#2B3542">A falta de estipulación expresa, la relación es por tiempo indeterminado. <span style="color:#5F7E9E">(Art. 35 LFT)</span></p>
</div>
<div style="height:2px;background:rgba(30,36,44,0.18)"></div>
<div>
<h2 class="serif" style="margin:0 0 18px;font-size:76px;line-height:0.98">Periodo de prueba: <span style="background:#FFFDF8;padding:0 10px">30 días</span></h2>
<p style="margin:0;font-size:31px;line-height:1.45;color:#2B3542">Máximo 30 días; hasta 180 para puestos de dirección o labores técnicas o profesionales especializadas. Solo en relaciones indefinidas o de más de 180 días, y con salario y seguridad social completos. <span style="color:#5F7E9E">(Art. 39-A LFT)</span></p>
</div>
<p style="margin:0;font-size:27px;line-height:1.4;color:#2B3542"><b>Y fírmalo en dos tantos:</b> uno para ti y otro para tu trabajador. <span style="color:#5F7E9E">(Art. 24 LFT)</span></p>
</div>
<img src="{M.SELLO_PIZARRA}" alt="" aria-hidden="true" style="position:absolute;right:80px;bottom:120px;width:110px;transform:rotate(6deg)">
{foot(H, 6, TOT)}""", " isolation: isolate;")))

# 7. Cierre
S.append(("Leg1-07-Cierre", cierre("¿Tu equipo ya tiene", "contrato?",
    "En GGTZ te ayudamos con tu empresa: constitución, marcas, contratos y temas laborales.",
    "Agenda tu asesoría", "Comenta <b>CONTRATO</b> y te paso el checklist completo.", fondo="atardecer")))

for name, html in S:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok", len(S))

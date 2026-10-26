# Guía de estilo: carruseles @bernardolatorre.fiscal

Estándar aprobado por Berny el 9 de octubre de 2026 (versión "v2": Cierre fiscal y RESICO). **Todo carrusel nuevo se hace así**, pero cada uno debe traer algo distinto y nuevo. Las plantillas de referencia están en `recursos/plantillas/` (Cie-* y Res-*).

## Identidad de marca: base de TODOS los diseños (aprobada por Berny el 13 oct 2026)

Logo "Bernardo Latorre · Tax Consultant" (inspiración: tipografía serif clásica tipo correo postal, sello circular y estampilla). Archivos en `recursos/marca/` (PNG transparentes, 2x; se regeneran con `python3 recursos/marca/_gen_marca.py`), ids en `assets.json`:

| Pieza | Archivo | Id | Uso |
|---|---|---|---|
| Logo principal (2 líneas + sello) | logo-principal-pizarra.png / -marfil.png | 2b162f4a5a3bf9e2b3b91b5c5abfc022 / 740e8448ef889bbdab01a3d4234291b0 | Portadas de presentación, documentos, propuestas |
| Logo horizontal (estampilla + nombre) | logo-horizontal-pizarra.png / -marfil.png | 7afe418b8551e87bb3f0f8e196d8230f / 916dbd49a3cb1e203b606fc4f660fbea | Cierre de carruseles, firmas, encabezados |
| Sello circular BL | sello-pizarra.png / sello-marfil.png | 89b150b4a0eaffd521105fa61198e074 / 5b8391f45478910a1d0d8ca2823faf9b | Marca pequeña en portadas o historias (90–130 px, puede ir girado ±8°) |
| Estampilla BL | estampilla-azul.png / estampilla-pizarra.png | fb44d2d96240b0ee464978e203027ae7 / 9755ee19657fbb11fb0cb1e5d1302b65 | Avatar, sellos, elementos gráficos |
| Foto de perfil IG | perfil-instagram-1080.png | 6675c9a47ae55a2cbe563c941226204b | Perfil de Instagram/WhatsApp |

- **Tipografía (cambiada el 13 oct 2026 a petición de Berny):** títulos, preguntas, números grandes, textos corridos de ganchos y el logo = **Archivo ExtraBold** (peso 800, ancho `font-stretch: 88%`, `letter-spacing: -0.03em`; archivo `recursos/fuentes/Archivo[wdth,wght].ttf`, OFL; Google Fonts `family=Archivo:wdth,wght@62..125,100..900`). Estilo grotesco pesado tipo GT Pressura (la referencia de Berny; GT Pressura es de pago, por eso se usa Archivo). En las plantillas basta la clase `.serif` (ya apunta a Archivo 800) o `font-family: 'Archivo'` (las plantillas llevan una regla que fuerza el peso 800). Texto y etiquetas = Hanken Grotesk. Sin cursivas: la palabra clave va en color (azul polvo) o con marcador. Interlineado de títulos 0.9–1.0. Pieza nueva inspirada en su referencia: lámina tipo lista (palabras grandes una debajo de otra separadas por líneas finas, con texto pequeño en vertical al costado). Archivo ExtraBold e Instrument Serif ya no se usan.
- **Logo en cada diseño:** todo carrusel, historia, anuncio o documento lleva la marca al menos una vez: el sello en la portada/primera pantalla o el logo horizontal en el cierre (la función `cierre()` ya lo trae, con "SOCIO EN GGTZ CONSULTORES" abajo). Versión marfil sobre fondos oscuros o fotos; versión pizarra sobre fondos claros. Nunca deformar, recolorear fuera de la paleta ni poner sobre fondos que le quiten contraste.
- **Paleta:** la misma de siempre (pizarra, marfil, azul polvo, salvia, terracota). Nunca dorado ni amarillo.
- Lienzo editable del logo: artifact "Logo Bernardo Latorre"; sistema de marca: artifact "Marca Bernardo Latorre".

## Lo que no cambia

- **Frases prohibidas (Berny, 18 oct 2026), en TODAS las publicaciones:** nunca usar el rótulo "en corto" ni la entrada "A ver, siéntate" (ni variantes). Se entra directo a la noticia y los recortes llevan un rótulo propio del tema o ninguno.
- **Formato:** 1080×1350 px, de 7 a 9 láminas. Se renderiza con `python3 recursos/render.py <carpeta_plantillas> <carpeta_salida> <archivos.dc.html>`.
- **Paleta:**
  - Pizarra #262F3B / #2B3542.
  - Marfil #F4F1EA / #FFFDF8.
  - Azul polvo #B7CFE6 como acento principal.
  - Salvia #A9C9A9 y terracota suave #D9B4A8 / #C98F7E como acentos secundarios.
  - Texto en #1E242C. **Nunca dorado.**
- **Tipografía:** Archivo ExtraBold para los títulos (palabra clave en color, sin cursiva; ver Identidad de marca) y Hanken Grotesk para el texto. Las etiquetas pequeñas van en mayúsculas con letter-spacing de 0.24em.
- **Portada:** nunca lleva la foto de Berny (excepción: posts de presentación personal, donde él pidió salir en portada y un tono formal). Su foto (sticker recortado) aparece solo en la última lámina, junto al botón para agendar.
- **Última lámina (13 oct 2026: SIN fotos genéricas):** nunca fotos de banco ni de Monterrey. Usa la función `cierre()` de `_gen_oct20_22.py`: fondo degradado de marca, sello BL arriba, pregunta en grande, botón de llamada a la acción, tarjeta para comentar/guardar, el sticker de Berny en estilo "portada de revista" (recorte grande que sangra a la derecha con "LATORRE" gigante y tenue detrás; elegido por Berny el 18 oct 2026, ya no el círculo salvia; variantes en `marco_berny()`), "81 2758 0277 · @bernardolatorre.fiscal", el logo horizontal y "SOCIO EN GGTZ CONSULTORES".
- **Pie de cada lámina:** la fuente legal ("Fuente: art. X LISR"), el usuario de Instagram y la numeración "03 / 08".
- **Datos:** toda cifra o artículo se verifica en la ley vigente (Luthor o una fuente oficial) o en el DOF y el SAT antes de usarse.
- **Imágenes:**
  - Solo del banco `recursos/` (fotos de Unsplash con licencia libre, capturas del SAT) o fotos nuevas de Unsplash con licencia libre, nunca de Google.
  - Las capturas del SAT siempre van dentro de un marco de navegador o de celular y con contexto educativo.
  - No usar fotos con texto en inglés, ni moneda o formularios de otros países.

## Portada: analizarla siempre contra las anteriores

Berny pidió (10 oct 2026) que las portadas nunca se vean iguales. Antes de diseñar una portada, revisa las **4 últimas** en `historial.md` y compara estos 4 rasgos:

1. **Motivo principal**: el objeto o la escena (billetes, pareja, lista, persona, edificio, gráfica…). **No se repite en las últimas 4 portadas.** Dinero (billetes o monedas) es el motivo más trillado del tema: úsalo como máximo 1 de cada 6 portadas.
2. **Tipo de fondo**: foto a todo lo ancho, pantalla dividida, color liso, textura sin foto, collage. No repitas el mismo tipo en dos portadas seguidas.
3. **Color dominante**: pizarra oscuro, marfil, azul polvo, salvia, terracota, foto en B/N. No repitas el de la portada anterior.
4. **Acomodo del título**: abajo en tarjeta, arriba grande, mitad izquierda, centrado, dentro de un objeto (celular, hoja, ticket). No repitas el de la portada anterior.

Después de renderizar, arma una tira con tu portada nueva junto a las 4 anteriores y mírala: si dos se parecen a primera vista, rehaz la nueva. Anota en `historial.md` la composición **y el motivo principal**.

## Degradados (pedido de Berny, 13 oct 2026: usarlos MÁS)

- **En cada carrusel, al menos 3 láminas con fondo degradado**, siempre la última (`cierre()`) y de preferencia la portada; reparte las demás entre las de en medio (una oscura y una clara funcionan bien). Las otras alternan con lino, papel, sarga, foto o color liso.
- Se hacen con `grad(nombre)` de `recursos/plantillas/_marca.py` (capa que va como PRIMER hijo de la lámina; la lámina lleva `isolation: isolate`). Degradados disponibles: oscuros (texto marfil) `sierra`, `noche`, `atardecer`, `neblina`; claros (texto tinta) `salvia`, `bruma`. Ejemplos: `Grad-0*.dc.html` y el RESICO v3 (`Res2-*`).
- Solo con colores de la paleta; nunca dorado ni amarillo. No pongas dos láminas seguidas con el mismo degradado.

## Ritmo visual (para que no se vea plano)

- **Alternar fondos.** Nunca dos láminas seguidas con el mismo fondo. Las opciones son:
  - Lino claro (`.bg-lino`).
  - Papel cuadriculado (`.bg-papel`).
  - Sarga oscura (`.bg-sarga`).
  - Foto a todo lo ancho con degradado pizarra.
  - Bloque de color sólido.
- **Por carrusel, como mínimo:**
  - 3 láminas con degradado (ver arriba).
  - 2 fotos reales en las láminas de en medio (nunca en la última).
  - 1 captura de pantalla real (del SAT, el DOF, el IMSS o Banxico) si el tema lo permite.
  - 1 lámina oscura.
  - 1 lámina con un número grande como protagonista.
- **Inclinar elementos.** Tarjetas, polaroids y stickers van rotados entre -6° y 6°. Se pueden agregar cinta adhesiva (washi tape), sombras y elementos que se salgan del margen.

## Catálogo de piezas (combinar y rotar)

| Pieza | Descripción | Usada en |
|---|---|---|
| Foto a todo lo ancho + tarjeta "hoja" rotada | Portada con título sobre papel | Cie-01 |
| Foto girada + tarjeta + sticker con cifra | Portada con dato | Res-01 |
| Número gigante + barra de meses | Fecha o cifra protagonista | Cie-02 |
| Lista de verificación en hoja + polaroid | Pasos o requisitos | Cie-03 |
| Cuadrícula 2×2 + recuadro oscuro + captura en navegador | Comparativo con prueba real | Cie-04 |
| Foto de fondo + tarjetas de vidrio con datos | Datos sobre ambiente | Cie-05 |
| Línea de tiempo oscura + celular con captura | Calendario o fechas límite | Cie-06 |
| Tabla oscura con barras | Tasas o rangos | Res-03 |
| Fórmula en bloques (A × B = C) | Explicar un cálculo | Res-02 |
| Tres polaroids con pie de foto | Perfiles de quién aplica | Res-04 |
| Ejemplo numérico: "Cobras $X → pagas $Y" | Caso práctico | Res-07 |
| Dos columnas: "Te conviene si / Compara si" | Decisión | Res-07 |

**Piezas nuevas para estrenar** (usar al menos una que no se haya usado antes en cada carrusel y agregarla a esta tabla):

- Mito contra realidad, con un sello "FALSO" o "CIERTO".
- Encuesta o quiz en lámina: "¿Cuál crees que es?", con la respuesta en la siguiente lámina.
- Recibo o ticket dibujado con un desglose de cifras.
- Antes y después, o error contra acierto, con una tachadura.
- Mapa de México o de Nuevo León con un dato.
- Conversación de chat (WhatsApp) con la duda de un cliente.
- Termómetro o semáforo de riesgo.
- Cuenta regresiva de días.
- Notas adhesivas (post-it) con tips.
- Captura de un titular del DOF dentro de un marco.
- Gráfica de barras o de línea con datos reales (inflación de INEGI, tipo de cambio de Banxico, UMA).
- Recorte de periódico simulado, sin marcas reales de medios.
- Lámina "Guárdalo para después", con una lista resumida.

## Ganchos y texto (tendencias 2026)

- **Primera lámina:** una pregunta o una promesa concreta, en 6 palabras o menos ("¿Te conviene el RESICO?", "Cierra el año sin sorpresas"). Agregar un número cuando sea posible.
- **Llamada a la acción:** pedir que **guarden** o **comenten** (funciona mucho mejor que pedir "likes"). La pie de foto incluye una pregunta.
- **Pie de foto:** escrito con las palabras que la gente busca (SEO dentro de Instagram) y con 1 o 2 hashtags relevantes (máximo 5).
- **Tono:** cálido, directo y de tú, para personas físicas y PyMEs de México. Nada de lenguaje de abogado.

## Datos de Berny para textos

- Es **socio** de GGTZ Consultores (no "socio fundador").
- En posts formales o de presentación: usar "Bernardo Latorre", no el apodo "Berny". No mencionar el Caso ICPNL 2017 en texto (la foto sí se puede usar).

## Formato de sábado: "Historias de despacho" (desde 17 oct 2026)

Pedido por Berny el 11 oct 2026 a partir de un post de referencia (@yosoydiegodiaz, instagram.com/p/DeNUiTOjsYP). **Este formato NO sigue el estilo de martes y jueves**: Berny lo quiere muy parecido a la referencia y claramente distinto de sus otros carruseles. Se publica **los sábados por la mañana** (10:00 suele ser la mejor hora).

- **Diseño fijo (v2.1, aprobado 11 oct):** fondo de papel claro texturizado (`texturas/papel-arrugado.jpg`, id `69e0532c9283413a0cbdcf3a9f33ca9b`) y **una sola tarjeta negra tipo publicación de X centrada**, de 780 px, solo texto. Toques mínimos, siempre los mismos: etiqueta "HISTORIAS DE DESPACHO" arriba (azul acero, letter-spacing), un trozo de cinta azul polvo en el borde superior de la tarjeta, la tarjeta girada menos de 1°, puntos de avance abajo y **una frase clave por tarjeta en azul polvo** (#B7CFE6, seminegrita). Nada más: sin fotos, capturas, títulos serif, post-its, pies de página, numeración ni logotipo.
- **Avatar:** la foto de Berny recortada en círculo (`berny/fotos/avatar-historias.jpg`, id `ee09a830e465eee2f30b4449a3fe87db`). Es la única foto suya en estos posts; no lleva el sticker de cierre.
- **Tarjeta:** "Bernardo Latorre" + "@bernardolatorre.fiscal", sin palomita de verificado; texto blanco en párrafos cortos; la primera lámina abre con una frase en MAYÚSCULAS; línea de hora y fecha reales de publicación; fila de íconos (responder, repostear, me gusta, guardar, compartir) **sin números: nunca métricas inventadas**. Generador: `plantillas/_gen_his01_opinion.py` (funciones `page(title, n, inner)`, `card()` y `K()` para la frase clave).
- **Narrativa:** gancho con el personaje → contexto → el problema → el motivo → lo que dice la ley (artículo entre paréntesis en gris dentro de la tarjeta) → cómo se resolvió → lo que me quedo de esta historia → pregunta para comentar + "📲 81 2758 0277 · GGTZ Consultores" + "Historia ilustrativa: nombre y cifras inventados." en gris.
- **Personaje ficticio** con nombre común y cifras inventadas; nunca presentarlo como cliente real.
- Verificar la ley igual que en todos los posts. El pie de foto sigue las reglas de siempre e incluye la línea de historia ilustrativa.

## Formato de domingo: historias "Chismesito fiscal" (desde 11 oct 2026)

Pedido por Berny el 11 oct 2026: cada domingo, **historias de Instagram** (1080×1920) con LA noticia fiscal más relevante de la semana, contada como chisme entre amigos. **Estilo deliberadamente sencillo, poco producido** (ref. @emiliocovi, instagram.com/p/DeLvbOEHPjy): NO usa las tarjetas, texturas, fotos ni capas de los carruseles.

- **Plantillas:** `plantillas/Chi-01-Story.dc.html` (gancho) y `Chi-02-Story.dc.html` (detalle). Cada semana se copian con prefijo nuevo.
- **Pantalla 1 (gancho):** fondo de UN color liso (azul polvo, salvia, terracota suave o marfil; alternar cada semana), etiqueta pequeña "☕ CHISMESITO FISCAL · fechas de la semana", y la noticia como texto corrido en Archivo ExtraBold grande (~60 px), tono de plática (sin muletillas de arranque como "A ver, siéntate": se entra directo a la noticia), con UNA frase resaltada con marcador. Cierra con la fuente entre paréntesis en texto chico y un garabato de línea simple (taza, ojos, lupa…).
- **Pantalla 2 (detalle):** fondo marfil o blanco, "lo que casi nadie te dice" en serif grande con resaltado, un recorte tipo hoja blanca con el texto clave (si es un artículo de ley, transcribirlo literal de Luthor/DOF y resaltar lo importante; si es resumen, sin rótulo o con un rótulo propio del tema, nunca "en corto").. Pie: "@BERNARDOLATORRE.FISCAL · GGTZ CONSULTORES".
- **Sin llamado a la acción** (Berny lo pidió así el 11 oct 2026): nada de botones, teléfono ni "escríbeme". Solo el pie "@BERNARDOLATORRE.FISCAL · GGTZ CONSULTORES" en la pantalla 2.
- **Música SIEMPRE:** cada pantalla se publica como video MP4 de 10 s (1080×1920, H.264 + AAC) con música instrumental ORIGINAL generada con `python3 recursos/musica_lofi.py` (cambia la semilla `default_rng(...)`, los acordes o el bpm cada semana para que no suene igual). Pantalla 1 usa el segundo 0–10 y la 2 el 11.7–21.7, con fade de entrada y salida. Nunca usar canciones con derechos.
- **Publicación (cambio pedido por Berny el 18 oct 2026):** las dos pantallas se dejan listas y se programan de una vez, en la misma corrida: primero la pantalla 1 a la hora elegida y enseguida la 2 para 3 minutos después (nunca a la misma hora ni con 1 minuto de diferencia: el 11 oct salieron al revés así). Ya no se espera a que la 1 salga para programar la 2.
- **Máximo 2 pantallas** (3 solo si la noticia lo exige). Nada de fotos, sombras dramáticas, elementos rotados ni stickers.
- **Zona segura de Instagram:** nada en los 200 px de arriba ni en los 220 px de abajo.
- **Noticia:** de fuente oficial (SAT, DOF, SHCP, Congreso, SCJN, IMSS) y verificada; útil para personas físicas o PyMEs; no repetir la de domingos anteriores.
- **Entrega:** PNG por pantalla + un PDF con todas, en `AAAA-MM-DD-chismesito-<tema>/`.

## Formato de miércoles: "Miércoles en 3 láminas"

Pedido por Berny el 13 oct 2026: cada miércoles, un carrusel **sencillo y muy puntual de 3 láminas** (1080×1350) sobre UNA noticia fiscal o económica de la semana. Referencia aprobada: `plantillas/_gen_economia_digital.py` (Ecd-*, v3).

- **Fondo = fotos del día a día de Berny** (tendencia que él pidió): cada lámina lleva a todo lo ancho una foto distinta de `berny/fotos/vida-*` (ver README), elegida para que tenga relación con la noticia (comida/puestos para pagos o consumo, oficina para SAT, cerro/carretera para plazos o "el camino", avión para viajes, etc.). Encima, un degradado pizarra oscuro (rgba(20,24,30,0.85) → transparente) donde va el texto, dejando ver el motivo de la foto en la otra mitad. No repetir las fotos de la semana anterior.
- **Texto con el lenguaje del Chismesito:** Archivo ExtraBold corrido en marfil con sombra suave, UNA frase con marcador azul polvo (`.hl`, texto oscuro), tono de plática.
- **Lámina 1 (gancho):** etiqueta "📲 MIÉRCOLES EN 3 LÁMINAS" + "01 / 03", pregunta grande (~120 px, una palabra en cursiva), la noticia en 2–3 renglones con el resaltado, y la fuente en una etiquetita marfil abajo.
- **Lámina 2 (detalle):** "Y lo que casi nadie te dice:" con la frase clave resaltada arriba, y abajo un recorte de hoja marfil con 3–4 viñetas (rótulo del tema, p. ej. "Lo demás"; nunca "en corto").
- **Lámina 3 (remate):** "¿Y a ti en qué te pega?" con un resaltado arriba; abajo, en texto chico: invitación a guardar + "¿Dudas…? 81 2758 0277" (sin partir el teléfono).
- **Pie en láminas 2 y 3:** "@BERNARDOLATORRE.FISCAL · GGTZ CONSULTORES" y la numeración, en marfil.
- **Nada de:** foto o sticker recortado de Berny, la foto de Monterrey de cierre, texturas (lino, papel, sarga), polaroids, botones ni la función `cierre()`. Ni identificaciones, documentos, pantallas con información de clientes o personas reconocibles sin permiso.
- **Datos:** solo lo verificado (fuente oficial o dos medios serios que coincidan), con el estatus claro.
- **También como historias:** las mismas 3 láminas se renderizan en 1080×1920 (`story()` del generador: foto a todo lo alto y el contenido centrado en la zona segura) y se publican como 3 historias, una por una y en orden (la siguiente solo después de confirmar que la anterior ya salió, con 3 min de diferencia).
- **Fotos con cuidado (Berny, 13 oct 2026):** antes de usar una foto mírala completa con Read y descártala si trae caras reconocibles de otras personas, pantallas o documentos legibles, placas legibles, marcas muy protagonistas o algo que no se vea bien para un contador. Ante la duda, otra foto.
- **Publicación:** miércoles a las 10:00 el carrusel; las historias se programan todas de una vez en la misma corrida (pedido de Berny, 18 oct 2026): la 1 a los 3 minutos del carrusel y cada una de las siguientes 3 minutos después de la anterior.

## Formato de lunes: "Lunes legal" (desde 19 oct 2026)

Pedido por Berny el 18 oct 2026: cada lunes a las 9:00, un carrusel con un tema **legal para emprendedores y empresas**, rematando con que **en GGTZ Consultores les ayudamos con su empresa** (GGTZ es despacho fiscal y legal; Berny es socio y contador, no abogado: el texto habla de "en GGTZ te ayudamos", nunca "como abogado").

- **Temas (rotar, no repetir del historial):** constituir una empresa (S.A. de C.V., S. de R.L., S.A.S., cuál conviene, socios y capital, acta constitutiva, poderes, asambleas y libros), registrar una marca ante el IMPI (búsqueda fonética, clases, vigencia, renovación, qué pasa si no la registras), temas laborales (contratos por escrito, prestaciones de ley, vacaciones, aguinaldo, PTU, finiquito vs. liquidación, NOM-035, subcontratación/REPSE, reglamento interior), contratos con clientes y proveedores, avisos de privacidad, pagarés y cobranza, sucesión y protocolo familiar, franquicias, cumplimiento corporativo anual.
- **Verificación:** todo artículo o requisito se revisa en la ley vigente con Luthor (LGSM, LFT, Ley Federal de Protección a la Propiedad Industrial, Código de Comercio, LFPDPPP) o en gob.mx / impi.gob.mx / dof.gob.mx. Sin datos inventados ni costos que no estén publicados. Nada de asesoría a un caso concreto: explicar en general.
- **Diseño:** la identidad de marca y las reglas de los carruseles (Archivo ExtraBold, degradados en al menos 3 láminas, sello BL en la portada, `cierre()` sin fotos genéricas). Etiqueta en la portada "⚖️ LUNES LEGAL". 6 a 8 láminas. Fotos del banco o del día a día de Berny solo si encajan (oficina, firma, negocio), con el mismo cuidado de siempre.
- **Cierre:** `cierre()` con una pregunta del tema y el texto "En GGTZ te ayudamos con tu empresa: constitución, marcas, contratos y temas laborales." y botón "Agenda tu asesoría".
- **Pie de foto:** gancho, 3–5 líneas de valor, "En GGTZ Consultores te ayudamos con tu empresa 👉 81 2758 0277", pregunta para comentar y 3–5 hashtags (#Emprendedores #Empresas #MarcaRegistrada #DerechoLaboral #Monterrey según el tema).
- **Publicación:** lunes 9:00 (America/Monterrey).

## Formato de lunes 7:00: "Tu dosis semanal" (HISTORIAS, desde 26 oct 2026)

Pedido por Berny el 25 oct 2026: cada lunes a las 7:00, **historias de Instagram** (1080×1920, NO carrusel) con lo más relevante de la semana anterior (lunes a domingo) en lo **fiscal, laboral y legal**, muy llamativas, "mientras te tomas el cafecito mañanero", sin perder la identidad de marca. **Sin degradados tornasol** (nada de `grad()`): fondos de color liso de la paleta. Referencia aprobada: `plantillas/_gen_dosis_2026_10_26.py` (DosS1-*). Convive con el "Lunes legal" de las 9:00 (no repetir la misma noticia en los dos).

- **5 historias:** portada + 3 "sorbos" (FISCAL, LABORAL/IMSS, LEGAL) + cierre. Si una semana no hay noticia de alguna categoría, se usa otra de las dos, pero siempre 3 sorbos.
- **Zona segura:** nada en los 200 px de arriba ni en los 220 de abajo (el contenido empieza en ~230 y el pie va en bottom 260).
- **Portada:** foto de café de Berny (`vida-cafe-terraza-playa` u otra suya con café) con sombra oscura arriba, "☕ TU DOSIS SEMANAL" + fechas, título "Lo que pasó esta semana, mientras te tomas el cafecito" con marcador azul polvo, chips FISCAL / LABORAL / LEGAL, sello BL y botón "3 sorbos →".
- **Cada sorbo:** fondo liso (fiscal azul polvo, laboral pizarra, legal terracota suave), "☕ SORBO N" + chip de categoría, taza de línea arriba a la derecha, titular en Archivo 112 px con marcador, cifra o dato gigante (190 px), qué pasó en 2–3 renglones (40 px) y la caja "¿Y A TI QUÉ?" ligeramente girada; fuente chica abajo y pie "@BERNARDOLATORRE.FISCAL · N / 5".
- **Cierre:** marfil liso, "¿Cuál de los 3 te pegó más?", "Respóndeme esta historia con 1, 2 o 3", círculos 1-2-3 de colores, sticker de Berny con "LATORRE" tenue detrás, teléfono, logo horizontal pizarra y "SOCIO EN GGTZ CONSULTORES".
- **Noticias:** de la semana anterior, verificadas en fuente oficial (DOF, SAT, IMSS, STPS, Congreso, SCJN, Luthor) o dos medios serios; estatus claro. No repetir lo del Chismesito del domingo ni lo del miércoles salvo avance nuevo.
- **Publicación:** las 5 historias se programan de una vez: la 1 a las 7:00 y cada siguiente 3 minutos después (7:03, 7:06, 7:09, 7:12), `instagramData.type "STORY"`, sin texto. Carpeta `AAAA-MM-DD-dosis-semanal/`.

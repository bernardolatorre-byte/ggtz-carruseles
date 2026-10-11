# Guía de estilo: carruseles @bernardolatorre.fiscal

Estándar aprobado por Berny el 9 de octubre de 2026 (versión "v2": Cierre fiscal y RESICO). **Todo carrusel nuevo se hace así**, pero cada uno debe traer algo distinto y nuevo. Las plantillas de referencia están en `recursos/plantillas/` (Cie-* y Res-*).

## Lo que no cambia

- **Formato:** 1080×1350 px, de 7 a 9 láminas. Se renderiza con `python3 recursos/render.py <carpeta_plantillas> <carpeta_salida> <archivos.dc.html>`.
- **Paleta:**
  - Pizarra #262F3B / #2B3542.
  - Marfil #F4F1EA / #FFFDF8.
  - Azul polvo #B7CFE6 como acento principal.
  - Salvia #A9C9A9 y terracota suave #D9B4A8 / #C98F7E como acentos secundarios.
  - Texto en #1E242C. **Nunca dorado.**
- **Tipografía:** Instrument Serif para los títulos (con una palabra clave en cursiva) y Hanken Grotesk para el texto. Las etiquetas pequeñas van en mayúsculas con letter-spacing de 0.24em.
- **Portada:** nunca lleva la foto de Berny (excepción: posts de presentación personal, donde él pidió salir en portada y un tono formal). Su foto (sticker recortado) aparece solo en la última lámina, junto al botón para agendar.
- **Última lámina:**
  - Una foto real de Monterrey en una banda superior.
  - Una pregunta en grande.
  - Un botón de llamada a la acción.
  - Una tarjeta que invite a comentar o a guardar.
  - "81 2758 0277 · @bernardolatorre.fiscal" y el logotipo GGTZ CONSULTORES.
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

## Ritmo visual (para que no se vea plano)

- **Alternar fondos.** Nunca dos láminas seguidas con el mismo fondo. Las opciones son:
  - Lino claro (`.bg-lino`).
  - Papel cuadriculado (`.bg-papel`).
  - Sarga oscura (`.bg-sarga`).
  - Foto a todo lo ancho con degradado pizarra.
  - Bloque de color sólido.
- **Por carrusel, como mínimo:**
  - 3 fotos reales.
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

Pedido por Berny el 11 oct 2026 a partir de un post de referencia (@yosoydiegodiaz). **Este formato NO sigue el estilo de martes y jueves**: Berny lo quiere muy parecido a la referencia y claramente distinto de sus otros carruseles. Se publica **los sábados por la mañana** (10:00 suele ser la mejor hora).

- **Diseño fijo (todas las láminas iguales):** fondo de papel claro texturizado (`texturas/papel-arrugado.jpg`, id `69e0532c9283413a0cbdcf3a9f33ca9b`) y **una sola tarjeta negra tipo publicación de X centrada**, de 780 px de ancho. Solo texto. Nada más en la lámina: sin fotos, sin capturas, sin títulos serif, sin post-its, sin pies de página ni numeración, sin logotipo.
- **Sin la cara de Berny** en ninguna lámina, ni en el cierre. El avatar es un círculo gris con "BL".
- **Tarjeta:** "Bernardo Latorre" + "@bernardolatorre.fiscal", sin palomita de verificado; texto blanco en párrafos cortos; la primera lámina abre con una frase en MAYÚSCULAS; línea de hora y fecha reales de publicación; fila de íconos (responder, repostear, me gusta, guardar, compartir) **sin números: nunca métricas inventadas**. Generador: `plantillas/_gen_his01_opinion.py` (funciones `page()` y `card()`).
- **Narrativa:** gancho con el personaje → contexto → el problema → el motivo → lo que dice la ley (artículo entre paréntesis en gris dentro de la tarjeta) → cómo se resolvió → lo que me quedo de esta historia → pregunta para comentar + "📲 81 2758 0277 · GGTZ Consultores" + "Historia ilustrativa: nombre y cifras inventados." en gris.
- **Personaje ficticio** con nombre común y cifras inventadas; nunca presentarlo como cliente real.
- Verificar la ley igual que en todos los posts. El pie de foto sigue las reglas de siempre e incluye la línea de historia ilustrativa.

## Formato de domingo: historias "Chismesito fiscal" (desde 11 oct 2026)

Pedido por Berny el 11 oct 2026: cada domingo, **historias de Instagram** (1080×1920) con LA noticia fiscal más relevante de la semana, contada como chisme entre amigos. **Estilo deliberadamente sencillo, poco producido** (ref. @emiliocovi, instagram.com/p/DeLvbOEHPjy): NO usa las tarjetas, texturas, fotos ni capas de los carruseles.

- **Plantillas:** `plantillas/Chi-01-Story.dc.html` (gancho) y `Chi-02-Story.dc.html` (detalle). Cada semana se copian con prefijo nuevo.
- **Pantalla 1 (gancho):** fondo de UN color liso (azul polvo, salvia, terracota suave o marfil; alternar cada semana), etiqueta pequeña "☕ CHISMESITO FISCAL · fechas de la semana", y la noticia como texto corrido en Instrument Serif grande (~70 px), tono de plática ("A ver, siéntate…"), con UNA frase resaltada con marcador. Cierra con la fuente entre paréntesis en texto chico y un garabato de línea simple (taza, ojos, lupa…).
- **Pantalla 2 (detalle):** fondo marfil o blanco, "lo que casi nadie te dice" en serif grande con resaltado, un recorte tipo hoja blanca con el texto clave (si es un artículo de ley, transcribirlo literal de Luthor/DOF y resaltar lo importante; si no, rotularlo "en corto"), y una invitación sencilla: "¿Tienes algo pendiente? Mándame DM o escríbeme al 81 2758 0277". Pie: "@BERNARDOLATORRE.FISCAL · GGTZ CONSULTORES".
- **Máximo 2 pantallas** (3 solo si la noticia lo exige). Nada de fotos, sombras dramáticas, elementos rotados ni stickers.
- **Zona segura de Instagram:** nada en los 200 px de arriba ni en los 220 px de abajo.
- **Noticia:** de fuente oficial (SAT, DOF, SHCP, Congreso, SCJN, IMSS) y verificada; útil para personas físicas o PyMEs; no repetir la de domingos anteriores.
- **Entrega:** PNG por pantalla + un PDF con todas, en `AAAA-MM-DD-chismesito-<tema>/`.

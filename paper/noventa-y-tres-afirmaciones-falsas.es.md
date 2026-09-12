# Noventa y tres afirmaciones falsas

### Registro versionado de un programa cuantitativo de una sola persona sobre microestructura de mercado

**Borrador 2 · 10 de septiembre de 2026 · sin enviar, sin ratificar**
*El borrador 1 se revisó contra el expediente y traía 35 errores de hecho. Al final está el registro de qué cambió.*

---

## Resumen

Examinamos un registro versionado de 93 entradas, cada una una afirmación que este programa hizo y que
después resultó falsa. Todas nombran a la parte o el instrumento que la cazó, y 25 anotan además cómo. El
registro es incompleto y no establece tasas de detección comparables entre personas, agentes o herramientas.

Lo que sostiene es una descripción. Contamos cómo se encontraron las 93, qué aparato había detrás de cada
una, y las ocasiones en que una comprobación pertinente estaba construida y nadie la había aplicado todavía
al objeto que le tocaba. El programa no estableció una ventaja operable para un participante pequeño y lento
con las pruebas y limitaciones que aquí se reportan. Su única estimación positiva, unos +18 puntos básicos en
una celda de régimen, se topó con un protocolo de revisión congelado meses antes de la corrida: las ocho
lentes del protocolo devolvieron amenaza aplicable, tres de ellas letales, y el veredicto global fue
destruido. Un diagnóstico posterior amplió una regla de admisión que ese mismo protocolo ya había señalado
como sensibilidad pendiente, y la estimación cayó a unos +3 puntos básicos. En la celda primaria ese mismo
cambio convirtió +2,6 en −1,1.

Describimos qué establece el aparato y qué no, las dos ocasiones en que el rigor fue a un sitio distinto de
donde el sistema se rompía, y las diez limitaciones que este estudio arrastra.

---

## 1. Qué es este artículo y qué no es

Es un estudio de caso descriptivo del registro de errores de un laboratorio. No afirma que el método aquí
descrito encuentre más defectos que otro. Nadie ha construido este sistema dos veces, no hay grupo de control
y un solo programa no sostiene ninguna afirmación sobre una población.

El programa funcionó unos seis meses. Su registro versionado empieza el 12 de junio de 2026 y termina el 9 de
septiembre de 2026, a lo largo de 457 commits. El trabajo anterior a esa fecha no lo acredita el repositorio
y no lo contamos como evidencia. El registro en sí es todavía más estrecho: entró en la historia el 24 de
agosto de 2026 y cambió por última vez el 28 de agosto de 2026, en trece commits. Documenta hechos
anteriores a esas fechas. Como artefacto versionado, vivió cinco días.

Insistimos en esto porque la única magnitud del artículo es un recuento, y un recuento sin la definición de
su muestra es justo lo que este laboratorio tardó seis meses en aprender a no publicar.

---

## 2. El programa

**La pregunta.** ¿Puede un participante pequeño y lento extraer ventaja sistemática de los futuros perpetuos
de criptomonedas, y dónde? Lo de lento está medido. El servidor de captura era una máquina virtual alquilada
en la Unión Europea, con copia externa en un volumen alquilado en otro centro de datos. Desde que un evento ocurría en el
mercado hasta que llegaba a nuestro servidor, la demora mediana era de 113 milisegundos y el percentil 99 de
265. Quien hace mercado y se toma en serio esta pregunta trabaja tres órdenes de magnitud más rápido.

**Los datos.** Instantáneas de libro de órdenes de niveles 2 y 3 y registros de operaciones de tres mercados,
recogidos a lo largo de once semanas. La recogida se interrumpió una vez, durante 9,4 días, por una factura
de hosting sin pagar. Un día del panel es parcial y la auditoría lo anota como tal. La captura de Binance
lleva recibo de auditoría por fichero y había producido 496 auditorías diarias sin fallos; el archivo de
Lighter, del que dependía de verdad el segundo capítulo, tenía 939 ficheros horarios y ninguna auditoría
diaria, lo cual es a su vez una de las entradas del registro. El panel del diagnóstico final cubre 79 días de
un instrumento.

**El método.** Las hipótesis se registran por adelantado, y desde el 27 de agosto de 2026 una guardia lo hace
cumplir por medios mecánicos, comparando commits en lugar de leer fechas dentro de un documento. Los seis
prerregistros reales del programa son anteriores a esa guardia y quedan eximidos uno a uno, por su nombre,
para que añadir un séptimo se vea en el diff. Las ventanas reservadas las hace cumplir un cargador que falla
cerrado, no la disciplina. Cada plan queda enlazado a su recibo por SHA-256. Cifras como el propio recuento
del registro las emite una herramienta junto con el comando que las produjo, de modo que el número no lo
teclea quien informa. Aun así el registro anota dos ocasiones en que un número se citó de memoria, con la
búsqueda pertinente abierta en pantalla.

**La respuesta.** El programa no estableció una ventaja operable con estas pruebas y estas limitaciones. Esa
frase es deliberadamente más débil que «no hay ventaja». Se examinaron ocho hipótesis, no el espacio de
hipótesis.

**El coste.** Seis meses y una persona. El alojamiento y la copia externa costaron unos pocos euros al mes;
los totales del propio expediente dicen cero dólares en datos y cómputo externo, más una compra de datos de
cuarenta y nueve dólares en el último mes. El código que sobrevive a la simplificación de cierre son 5.933
líneas entre análisis y herramientas, con 476 pruebas y una integración continua que termina en 72 segundos.

---

## 3. El registro

El registro anota lo que resultó **falso**, no lo que resultó **difícil**. Un problema duro bien resuelto no
entra. Una afirmación cómoda que no aguantó la medida, sí. Lo gobiernan tres reglas, y son la razón de que
los recuentos signifiquen algo:

1. La entrada se escribe **antes** de corregir, para que lo que quede no sea la versión ya digerida.
2. El descubridor se anota con precisión. «Lo encontró el propio autor» solo cuenta cuando lo encontró antes
   de que se lo dijeran y antes de que un instrumento lo señalara.
3. Las entradas nunca se borran. Cuando una entrada resulta a su vez equivocada, otra posterior la corrige,
   con su fecha. El registro contiene una de esas correcciones.

La muestra son 93 entradas: 84 con prefijo E y 9 con prefijo X. Los identificadores van de E-01 a E-85 sin
E-60, y de X-01 a X-09, así que quien reconstruya el conjunto por el rango contará 94 y no debe.
Veinticinco entradas, todas en la primera tabla, llevan una columna explícita con cómo se produjo la
detección. Otras dos llevan un quinto campo suelto. Las sesenta y seis restantes nombran solo al
descubridor, lo cual no significa que su texto calle el mecanismo.

**Tabla 1. Etiquetas de descubrimiento en las 93 entradas.**

| etiqueta | lo que dice la clave del propio registro | n |
|---|---|---|
| revisor externo | un revisor humano fuera del papel que implementa | 35 |
| el autor, por criterio propio | lo encontró antes de que nada lo señalara, casi siempre al volver a medir | 25 |
| revisión adversarial | protocolo congelado de ocho lentes, invocado a mano | 12 |
| arnés de mutación | se cambia una línea de código y un test nombrado tiene que fallar | 9 |
| integración continua | la suite completa sobre otro sistema operativo | 2 |
| el propio revisor, sobre sí mismo | una afirmación que retiró, o que mató al remedir, antes de que nadie se lo dijera | 2 |
| el propietario | una pregunta por una carpeta que nadie había declarado | 1 |
| un proveedor | el correo de un tercero | 1 |
| sonda | una medición escrita a propósito para dudar de la hipótesis propia | 1 |
| suite local | la batería que no es la integración continua, y ha visto lo que esta no vio | 1 |
| trinquete | una comprobación automática autoimpuesta | 1 |
| falsificador por propiedades | genera entradas adversariales y busca el contraejemplo | 1 |
| el propio error | el defecto aflorado por su propia consecuencia | 1 |
| una medición | un número que contradecía la frase de al lado | 1 |
| **total** | | **93** |

**Lo que esta tabla no dice.** Son los nombres de categoría del propio registro y como categorías las usamos.
El expediente no atribuye ninguna entrada concreta a una persona o sistema con nombre, y no vamos a suplir
una atribución que no sostiene. La sección 9 explica cómo se produjo el trabajo.

La tabla no se teclea. Una herramienta la regenera desde las tablas del registro, se niega a publicar cuando
dos filas comparten identificador, y la integración continua la comprueba en cada envío. La herramienta
existe porque el recuento se llevó a mano y llegó a decir 33, 26 y 22 a la vez en tres sitios del mismo
documento. Lo cazó un revisor externo contando él mismo las filas.

No ordenamos estas etiquetas entre sí. Cada instrumento entró en una fecha distinta, así que su exposición
difiere; el registro no ofrece denominador de oportunidades; y los errores que nadie encontró faltan por
construcción.

---

## 4. Cuatro episodios

Cada título es el hallazgo, no el tema.

### 4.1 La única estimación positiva se topó con una revisión que alguien tenía que recordar

El programa produjo una sola estimación positiva de unos +18 puntos básicos, en una celda definida por un
régimen lento, un estado de volatilidad agitado y un horizonte de 25 segundos.

Un protocolo de revisión se había escrito y congelado meses antes. Define ocho lentes y emite un veredicto
por lente. Nada lo dispara. Alguien tiene que acordarse.

Se corrió una vez, en junio, sobre el primer capítulo del programa, y devolvió un veredicto. Nadie lo aplicó
al segundo capítulo hasta el 24 de agosto de 2026. Cuando por fin se corrió, las ocho lentes reportaron
amenaza aplicable, tres letales y cinco graves, y el veredicto global del protocolo fue **destruido**. Seis
de las ocho, por sí solas, habrían rebajado la afirmación de hallazgo a hipótesis. Dos la mataron: mirada al
futuro dentro de la regla de admisión, y una variable omitida.

El protocolo tiene exactamente un veredicto registrado de esta clase. Nunca se ha corrido contra un efecto de
tamaño conocido, así que no conocemos ni su potencia ni su tasa de destrucción falsa, y destruir una
estimación no prueba que un instrumento sea severo.

### 4.2 Una reproducción exacta restringía menos de lo que parecía

El 7 de septiembre de 2026, dos semanas después de aquel veredicto y dos meses después de que se publicara la
estimación, reprodujimos la receta histórica desde custodias re-adquiridas a los mismos dos proveedores. La
comparación cubrió ocho campos históricos a lo largo de 79 días, 632 comparaciones, y todas coincidieron
exactamente.

El resultado es más débil de lo que suena, y la debilidad es la parte interesante. Las dos corridas aplicaban
la misma regla de admisión, así que la comparación no tenía potencia contra un paso que mantenía fijo. Que
las salidas coincidan exactamente no muestra que los insumos fueran idénticos: muestra que la receta, dado lo
que se le dio, es determinista. Cincuenta y cuatro horas de datos de un mercado nunca se resolvieron en ocho
de esos días, y los registros de operaciones de julio no se conservaron, así que no hay comparación posible a
nivel de insumo contra la corrida original y no se ofrece ninguna.

La regla en cuestión no era desconocida. Una enmienda fechada el 6 de julio de 2026, un día después de que
apareciera la estimación, nombraba la operación exacta y declaraba obligatoria la prueba de sensibilidad. El
protocolo congelado anotó después que esa prueba seguía pendiente y que se había dado por no inversora sin
evidencia. Cuando el analista amplió por fin la regla, la estimación de la celda compañera cayó de unos +18
puntos básicos a unos +3, y la celda primaria de cinco segundos pasó de +2,6 a −1,1. El contraste fue
negativo en 73 de los 79 días.

Dos cosas de esa decisión deben viajar con las cifras allí donde aparezcan. La ampliación se hizo después de
que el resultado fuera visible, dentro de un diagnóstico cuya propia especificación congelada se llama a sí
misma retrospectiva y post hoc. Y no la aplicó ningún control automático. Un documento la había nombrado, un
protocolo de revisión la había señalado como pendiente, y una persona actuó dos meses más tarde.

### 4.3 El aparato hizo comprobable la retirada; no la produjo

Conviene ser exactos sobre lo que hizo la maquinaria. La guardia de pre-registro fecha documentos y no dice
nada sobre puntos básicos. Los cargadores que fallan cerrados no reportaron ninguna brecha en esta línea. La
guardia de especificación pertenece a otro incidente. Las filas de mutación comprueban si las guardias tienen
dientes, no si un efecto es real. Los hashes que enlazan plan y recibo hacen el registro comprobable después
del hecho.

Ninguno retiró el número. Lo hizo un protocolo congelado que una persona tuvo que recordar, junto con una
sensibilidad que un documento había declarado obligatoria y nadie había corrido.

Lo que el aparato produjo es una afirmación sobre custodia y no sobre causalidad: la retirada está fechada,
es atribuible y no se puede deshacer en silencio. Hacemos la primera afirmación y no la segunda.

### 4.4 El rigor fue donde el trabajo era interesante

Doce sesiones de trabajo se fueron en endurecer un libro transaccional contra colisiones entre escritores,
sustitución de bytes dentro de una ventana de escritura y contención entre máquinas. Durante ese mismo
periodo el colector de datos corrió sin vigilancia dos meses y produjo 496 auditorías diarias sin fallos.

Lo que detuvo la producción de datos fue una factura de hosting sin pagar.

Hay una segunda instancia, y es la cara. Una herramienta que traduce el objetivo declarado del programa al
nocional, el número de fills y la cuota de mercado que exigiría se escribió el 25 de agosto de 2026, en el
sexto y último mes. Escrita la primera, habría contestado en una tarde una pregunta que costó seis meses: si
el objetivo exigía una ventaja un orden de magnitud mayor que cualquier cosa que el instrumento pudiera
medir.

Dos episodios en un laboratorio, sin grupo de control, no establecen ninguna ley sobre cómo se distribuye el
rigor.

---

## 5. Qué establece el aparato y qué no

**La guardia de pre-registro** establece que el commit en el que entró en la historia el texto *vigente* de un
prerregistro es ancestro estricto de los commits que introdujeron los artefactos que el documento dice
preceder, y se niega a certificar un artefacto que llegó por renombrado. **No** establece una fecha frente a
un autor que quiera falsificarla, porque las fechas de commit y la historia son valores que controla el dueño
del repositorio. Defiende del descuido del propio autor, que es la amenaza que ocurrió. Atar un recibo al
commit que introdujo el *nombre* del fichero en lugar de su *texto* normativo fue a su vez una de las
entradas del registro: un prerregistro nacido en un commit tenía sus reglas operativas escritas en otro, y el
recibo habría certificado una versión que ya no regía.

**Los cargadores que fallan cerrados** establecen que una ventana reservada no puede leerse por una ruta que
se olvidó de preguntar. **No** establecen que el diseño de la reserva fuera el correcto.

**La guardia de especificación** establece, analizando el código, que cada regla que el documento declara
implementada apunta a un símbolo que existe en el fichero que nombra. **No** establece que la regla sea
correcta, ni que el símbolo haga lo que la regla dice, ni nada en absoluto sobre las reglas que el documento
enumera sin declarar, que reporta como pendientes sin fallar. Existe porque una especificación prometió
salidas que el código descartaba. Su analizador sintáctico existe porque la primera versión de la guardia
buscaba el identificador como texto y un comentario la satisfizo. Ese segundo error lo cometió el mecanismo
después de estar construido, y lo cazó una persona leyendo.

**Las filas de mutación** establecen que para 49 mutaciones concretas del código, 47 de una sola sustitución
y dos de un par deliberado, un test nombrado falla. **No** son una puntuación de mutación: el autor eligió
las mutaciones, el autor escribió los tests, y no hay denominador de mutantes generados. No miden ni
cobertura ni severidad. Una fila se excluyó el 1 de septiembre de 2026 tras dejar de producir un fallo, con
la razón anotada al lado: al volverse obligatorio un digest, el estado que la guardia vigilaba dejó de ser
alcanzable. Esa nota recoge la explicación que se dio entonces. No es una demostración independiente de
inalcanzabilidad.

**El recuento generado** establece que la cifra impresa en un documento coincide con las tablas de ese mismo
documento. **No** establece que las tablas estén completas.

---

## 6. Objeciones

**¿Esto no es práctica de reproducibilidad con nombres nuevos?** En parte sí, y esas partes las citamos en
lugar de reclamarlas. Lo que no hemos visto en otro sitio es un repositorio en funcionamiento donde las
guardias llevan una fila adversarial explícita que nombra el test que debe fallar cuando cambia una línea de
código, de modo que un control decorativo se vuelva visible por medios mecánicos. La cobertura no es
universal: cuando se retiró la fila descrita arriba, la guardia se quedó en el código sin nada que la
acreditara, y el registro lo dice en el sitio de la fila.

**Los mecanismos se construyeron después de los errores que previenen. ¿Es esto un relato a posteriori?** Lo
fueron, y lo decimos en cada mecanismo. En los dos casos principales fue una persona leyendo quien cazó el
error, y el mecanismo es la consecuencia, no el descubridor. Un artículo que afirmara lo contrario quedaría
desmentido por su propio registro.

**¿Puede un lector verificar algo de esto?** Hoy no. El repositorio era privado a 9 de septiembre de 2026. El
código, las guardias, las filas de mutación y la definición de la integración continua son autocontenidos y
cualquiera podría correrlos cuando se abra; un espejo público saneado está especificado en el expediente y no
se ha publicado. Los datos de mercado que sostienen el diagnóstico están bajo licencia y en ningún caso se
pueden redistribuir, así que la higiene sería comprobable y el hallazgo no.

**¿Es fiable el recuento si lo produce una de las partes?** El recuento se regenera desde las tablas y lo
comprueba la integración continua, así que no puede desviarse de ellas. La *clasificación* es otra cosa y
tiene juicio dentro: «lo encontró por criterio propio» y «se lo señaló un instrumento» a veces se solapan. Un
segundo codificador es lo que este registro necesita y no tiene.

---

## 7. Qué haríamos distinto

**Escribir primero la herramienta de viabilidad.** Traducir el objetivo a nocional, fills y cuota de mercado,
con los insumos medidos y los supuestos declarados, es una tarde de trabajo. Va en la primera semana de un
programa, no en el último mes.

**Darle a cada control algo que lo dispare.** Los controles que fallaron aquí no estaban mal diseñados.
Fallaron porque alguien tenía que acordarse, y durante dos meses nadie se acordó. Al diseñar una salvaguarda,
hay que preguntarse qué la dispara cuando nadie se acuerda.

**Fijar las reglas de admisión antes de mirar.** La regla que desinfló la estimación era defendible, estaba
nombrada de antemano, y aun así se aplicó cuando su efecto ya era visible. Con suficientes reglas de limpieza
defendibles, una de ellas mata cualquier efecto. Hay que fijar el conjunto en un commit fechado y publicar la
estimación bajo todas las reglas del conjunto.

---

## 8. Limitaciones

El registro imprime seis limitaciones sobre sí mismo. Se reproducen aquí en vez de resumirse, porque un
resumen que pierde las salvedades de la tabla que resume es un modo de fallo que este registro cataloga bajo
un identificador propio.

1. **La muestra no es aleatoria ni completa.** Recoge lo encontrado mientras se llevó el registro. Los
   errores que nadie encontró faltan por construcción, y son los que más informarían.
2. **El recuento lo hace una de las partes.** Un tercero debería recontarlo.
3. **La clasificación de descubridor tiene juicio dentro.** Dos categorías se solapan.
4. **No hay grupo de control.** El mismo sistema no se ha construido dos veces, así que no hay comparación
   entre métodos disponible.
5. **La gravedad de los defectos no está normalizada.** Una etiqueta de prioridad significa lo que este
   proyecto decidió que significa.
6. **Llevar este registro no acredita la calidad del sistema.** Se puede llevar un registro impecable de un
   trabajo malo. Lo que acredita, si acredita algo, es que las afirmaciones se pueden auditar, no que sean
   correctas.

Cuatro más son nuestras.

7. **El registro está cerrado y el trabajo continuó.** Su último cambio versionado es del 28 de agosto de
   2026 y el programa llegó al 9 de septiembre. Los errores encontrados y documentados después de esa fecha,
   incluida la retirada de la estimación positiva, no están entre las 93.
8. **El método de detección consta para 25 de las 93.** El resto nombra solo al descubridor.
9. **Una sola cuenta autoría todos los commits,** así que el repositorio por sí solo no puede atribuir un
   cambio a un contribuidor frente a otro. Ningún commit lleva firma criptográfica.
10. **Las entradas de defecto y las de afirmación son poblaciones distintas.** Los defectos abiertos de la
    tabla del sistema no están entre las 93, y varios afectan a componentes que ya no existen.

---

## 9. Disponibilidad, y una declaración

El repositorio era privado a 9 de septiembre de 2026 y hay un espejo público saneado especificado y sin
publicar. El trabajo de integración continua más reciente sobre la rama principal reporta 476 pruebas pasadas
y 49 de 49 comprobaciones de mutación que fallan como se les exige. Los datos de mercado que sostienen el
diagnóstico están bajo licencia y no se redistribuyen; los recibos y hashes que los identifican, sí.

El programa se llevó a cabo con asistencia de sistemas de inteligencia artificial, que escribieron código, lo
auditaron y son el origen de parte del registro. No damos una proporción, porque las etiquetas del registro
son sus propias categorías y el expediente no atribuye entradas concretas a personas o sistemas con nombre.
Declaramos la asistencia porque es un hecho material sobre cómo se produjo el trabajo, y porque un registro de
afirmaciones falsas que ocultara una sobre sí mismo sería una contribución extraña.

---

## 10. Conclusión

Un programa de una sola persona pasó seis meses preguntando si un participante lento podía extraer ventaja
sistemática de un mercado rápido, construyó un aparato para mantenerse honesto mientras preguntaba, y no
estableció ninguna.

El programa retiró su única estimación positiva dos veces: en agosto como afirmación causal, cuando un
protocolo de revisión que alguien por fin recordó correr devolvió un veredicto de destruido, y en septiembre
como soporte de una ventaja operable, cuando un diagnóstico post hoc amplió una regla de admisión que ese
mismo protocolo ya había señalado como pendiente. En ninguno de los dos casos lo hizo un control automático.

El registro de 93 afirmaciones falsas es lo que queda, y sus entradas más útiles no son los errores. Son las
ocasiones en que una comprobación pertinente ya existía, estaba escrita con cuidado, y nadie la había
aplicado al objeto que le tocaba.

---

## Apéndice: qué cambió entre el borrador 1 y el borrador 2

El borrador 1 se revisó sección por sección contra el expediente, y cada hallazgo se clasificó como error de
hecho, límite de inferencia o problema de referencia. La revisión devolvió 68 hallazgos: 35 errores, 21
límites y 12 problemas de referencia. Los 35 errores están corregidos arriba. Los mayores fueron:

- **El mecanismo de pre-registro estaba descrito al revés.** El borrador 1 decía que la autoridad de fecha
  vive en el commit introductor. Atarse al commit introductor es la entrada E-64 del registro, el defecto que
  la guardia se reparó para no cometer. Corregido en las secciones 2 y 5.
- **La latencia.** El borrador 1 decía decenas de milisegundos. Las cifras medidas son 113 ms de mediana y
  265 ms de percentil 99. La corrección refuerza el propio argumento del artículo.
- **El coste.** El borrador 1 afirmaba unos seiscientos dólares de infraestructura. Esa cifra no existe en el
  expediente, cuyos totales dicen cero dólares en datos y cómputo externo más una compra de cuarenta y nueve.
  El «600» venía de un saldo de créditos y se convirtió a dólares de memoria.
- **La disponibilidad.** El borrador 1 decía que un lector podía correr el código. El repositorio es privado.
- **Las ocho lentes.** Ocho de ocho es el recuento de lentes que reportan amenaza aplicable, no ocho
  destrucciones. Tres eran letales, cinco graves, y el veredicto global fue uno solo: destruido.
- **La regla de admisión no estaba sin examinar.** Se había nombrado el 6 de julio de 2026, un día después de
  que apareciera la estimación, y se declaró sensibilidad obligatoria; el protocolo congelado la anotó como
  todavía pendiente.
- **Las fechas.** La reproducción es dos semanas posterior al veredicto, no dos meses. La herramienta de
  viabilidad está fechada el 25 de agosto de 2026, el sexto mes, no el octavo.
- **Los recibos de auditoría.** Cubren la captura de Binance. El archivo de Lighter, del que dependía el
  segundo capítulo, tenía 939 ficheros horarios y ninguno.
- **La conclusión fundía dos operaciones** y contradecía a la sección 4.3.

El registro de esa revisión se conserva junto a este borrador. El borrador 1 no se borra.

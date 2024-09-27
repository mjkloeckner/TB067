# Trabajo Práctico: Nivel de Transporte y Nivel de Red del Modelo TCP/IP

Redes de Comunicaciones (TB067) - 2C2024 - FIUBA  
Martin Klöckner (123456) - [mklockner@fi.uba.ar](mailto:mklockner@fi.uba.ar)

## El protocolo MQTT

MQTT (Message Query Telemetry Transport) es un protocolo de red ligero y
eficiente, implementado de extremo a extremo y con patron publisher-subscriber
(editor-suscriptor).

Este protocolo está diseñado principalmente para dispositivos en locaciones
remotas con recursos y/o ancho de banda limitado, tal como sistemas embebidos.

El protocolo MQTT se ubica en el nivel de aplicación del modelo TCP/IP, y
requiere de un protocolo del nivel de red que sea ordenado, seguro y sin perdida
de datos, tal como el protocolo TCP.

### Seguridad

Encriptacion

### Aplicaciones Comerciales

### Versiones

Las versiones de MQTT son controladas por la organización sin fines de lucro
OASIS (Organization for the Advancement of Structured Information Standards)

#### MQTT 5
#### MQTT 3.1.1
#### MQTT 3.1
#### MQTT-SN v1.2

### Referencias

[MQTT: The Standard for IoT Messaging](https://mqtt.org/)
[¿Qué es MQTT?](https://aws.amazon.com/es/what-is/mqtt/)

## Uso Práctico

> Sobre la aplicación, ¿de qué modo consigue implementar la fragmentación?

> En comparación con la fragmentación que implementa el protocolo TCP, ¿hay
> funcionalidades o características de la fragmentación en estos scripts que
> sean similares a la segmentación TCP? ¿Cuáles?

> En comparación con la segmentación que implementa el protocolo TCP, ¿hay
> funcionalidades o características de la segmentación TCP que en estos scripts
> estén ausentes? ¿Cuáles?

> Acerca de las sesiones del publicador y del suscriptor, ¿cuáles son los
> extremos de las sesiones? ¿quién toma el rol de cliente y quién de servidor?

> Sobre la extensión de las sesiones, ¿son persistentes, cómo se sostienen
> cuando no hay tráfico? ¿no son persistentes? ¿cómo se cierran (en qué momento
> y quién lo inicia)?

> En detalle sobre las sesiones:
> a. ¿Cuál es el número de secuencia del primer segmento TCP de
>    petición de conexión?
> b. ¿Cuáles son las opciones implementadas, si las hay?
> c. ¿Cuántos bytes tiene el buffer de recepción según se informa al inicio?
> d. ¿A qué hora se envió el primer segmento (el que contiene datos de la
>    aplicación)? ¿A qué hora se recibió el ACK de este primer segmento
>    que contiene datos? ¿Cuál es su RTT?
> e. ¿Cuál es la longitud (encabezado más carga útil) de cada uno de los
>    primeros cuatro segmentos TCP que transportan datos?

> HTTP indica la cantidad de datos a transmitir mediante un encabezado. Esta
> adecuación de MQTT para transmitir fragmentos no comunica la cantidad de datos
> que va a transmitir. Si algún paquete se perdiera, el suscriptor no tendría
> forma de detectar la falta. Modificar el código para simular la pérdida de un
> paquete intermedio y verificar en el suscriptor que el texto quede truncado.
> Luego modificar ambos scripts para que se comunique el largo de los datos a
> transmitir y que el suscriptor pueda validar la cantidad de datos recibidos
> versus los esperados.

> De las funcionalidades o características vinculadas a segmentación, presentes
> en TCP pero no cubiertas por estos scripts, implementar una versión mejorada,
> que incorpore al menos una mejora o una funcionalidad.  Se puede usar
> inteligencia artificial y por qué no, inteligencia natural.

# LinkedIn (ES) — when-you-cannot-test-it


Hay cambios que no se pueden probar antes de aplicarlos, y fingir lo contrario es un riesgo en sí mismo.

El laboratorio no tiene el hardware del otro fabricante. El comportamiento solo aparece por encima de un volumen de tráfico que usted no puede generar. La plataforma es única y no hay una segunda unidad en ninguna parte. Eso no son excusas. Son las condiciones reales de muchos parques.

Lo que sale mal no es que el cambio sea riesgoso. Lo que sale mal es que el plan finge que no lo es. El registro de cambio dice probado, queriendo decir que se probó algo parecido, y todo el mundo avanza con una confianza que la evidencia no sostiene.

Por eso el primer paso es nombrar la categoría en voz alta, delante de todos los que firman. Este cambio no se puede validar por adelantado. Una vez dicho eso, la conversación pasa a ser sobre exposición y no sobre certeza, y esa sí es una conversación que se puede gestionar de verdad.

Después el método cambia de forma. La primera aplicación más pequeña posible, en el sitio donde la consecuencia sea más tolerable. Un periodo de observación definido antes del segundo, lo bastante largo como para cruzar tráfico real y no una hora tranquila. Una lista explícita de qué se vigila y qué lectura significa detenerse. Y una reversión (rollback) ensayada hasta que su duración sea un número conocido, porque esa decisión la toma bajo presión alguien que está cansado.

Esa secuencia no elimina la incertidumbre. La convierte en algo acotado y medible: un sitio en lugar de cuarenta, una ventana conocida, un camino de regreso conocido y ya practicado.

El modo de falla que vale la pena evitar es el despliegue confiado de un cambio no probado sobre todo el parque en una sola ventana, porque estaba aprobado y la ventana ya estaba reservada.

Que no se pueda probar es una propiedad del cambio en sí. Que no se gestione es una decisión que alguien tomó sobre el plan.

Reserve una consulta: mzsnetworks.com

#NetOps #IngenieriaDeRedes #GestionDeCambios

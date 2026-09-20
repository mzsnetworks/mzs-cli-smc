# LinkedIn (ES) — test-before-it-touches-a-device


En casi cualquier disciplina, "lo aplicamos y vemos qué pasa" no es un plan de pruebas.

En redes sigue siendo lo habitual. El cambio se revisa leyéndolo, lo aprueba alguien que también lo leyó, y se valida aplicándolo a producción durante una ventana, mirando qué se rompe. Nadie lo llamaría una prueba en ningún otro lugar de la organización.

Leer un cambio le dice que es sintácticamente correcto. No le dice que esta ACL, en este equipo, con esta tabla de rutas, descarta el tráfico que usted olvidó que pasaba por ahí.

La alternativa no es exótica. Construya un modelo de la red — topología, direccionamiento, políticas, adyacencias — y evalúe el cambio contra el modelo antes de que llegue a un equipo. Lo que obtiene no es "la configuración compila". Es qué haría distinto la red con ese cambio aplicado, y cuáles de esas diferencias usted no pretendía provocar.

Eso es lo que hace Config Modeling, y es la práctica que más riesgo saca de la ventana de cambio, porque mueve el descubrimiento del error de las 2 de la mañana en producción a un martes por la tarde en una laptop.

Un modelo no detecta todo, y vale la pena decirlo con claridad. No le va a avisar que un transceptor se está degradando, ni que el extremo remoto tiene una política propia que nadie documentó, ni que la implementación del fabricante no coincide con su propia documentación. Lo que sí detecta es la clase de error que nace de razonar sobre una red grande dentro de la cabeza de una sola persona. En un entorno multi-sitio, esos son la mayoría.

También cambia la conversación de revisión. Los revisores dejan de discutir sintaxis y empiezan a discutir intención, que es la discusión que vale la pena tener.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #InfraestructuraComoCodigo #NetOps

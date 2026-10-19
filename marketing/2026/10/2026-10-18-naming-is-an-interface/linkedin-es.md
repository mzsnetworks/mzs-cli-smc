# LinkedIn (ES) — naming-is-an-interface


Las convenciones de nombres se tratan como tareas domésticas. En realidad son una interfaz, y la automatización es quien la consume.

Así aparece el problema. Alguien escribe un script que actúa sobre todos los switches de distribución. Para saber cuáles son, hace coincidencia sobre el hostname. La convención se mantuvo en los primeros ocho sitios y después se rompió, porque otro equipo construyó los doce siguientes, y una fusión trajo treinta más con un esquema que nadie puso por escrito.

Ahora el script necesita una tabla de excepciones. Esa tabla necesita mantenimiento constante. Y la persona que la mantiene termina siendo la única de todo el equipo que de verdad la entiende.

Lo mismo pasa con las descripciones de interfaz. Un sistema que distingue un circuito de cliente de un enlace de respaldo lee el campo de descripción, porque ese es el único lugar donde existe la distinción. Cuando ese campo es texto libre, esa capacidad no está disponible, sin importar lo que la plataforma sea capaz de hacer.

Lo que hace difícil corregir esto es que nunca llega a ser urgente. Nada está roto. Cada inconsistencia individual es pequeña, defendible, y fue la decisión obvia en su momento.

El costo no llega como una interrupción. Llega como un techo. Cada automatización acumula más casos especiales, todos razonables uno por uno, hasta que los casos especiales son el sistema y nadie se atreve a tocarlo.

La solución no es un proyecto de renombrado sobre todo el parque, que es disruptivo y casi nunca se aprueba. Es acordar la convención ahora, aplicarla a todo lo nuevo, y reconciliar el parque existente en el orden que la hoja de ruta de automatización realmente necesite. Cada pieza de esa hoja de ruta sale más barata en el momento en que los nombres significan algo.

Una máquina no puede inferir lo que usted quiso decir. Solo puede leer exactamente lo que usted escribió.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #InfraestructuraComoCodigo

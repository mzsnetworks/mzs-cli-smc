# LinkedIn (ES) — blast-radius-before-the-window


Un comité de cambio lee un diff. El riesgo casi nunca está en el diff.

El diff es honesto respecto de lo que muestra: estas líneas en este equipo pasan a ser aquellas otras líneas. Los revisores verifican la sintaxis, verifican que coincida con el estándar y lo aprueban. Lo que no pueden verificar desde esa vista es qué más toca el cambio, porque eso no vive en el equipo: vive en la topología completa.

Entonces la pregunta se termina respondiendo de memoria. Alguien con experiencia lee el cambio y dice que se ve bien, lo que en realidad significa que no se le ocurre de inmediato ninguna dependencia que se rompa. Eso tiene valor real, pero no es un método. Escala exactamente hasta donde llega la memoria de una sola persona sobre un parque que cambió el martes pasado.

Modelar el cambio contra la red prevista es la parte que sí escala. Un prefijo que se retira aquí deja de anunciarse allá. Una política que se endurece en un firewall mueve tráfico hacia un camino que fue dimensionado para respaldo y no para operación normal. Un cambio de MTU en un enlace afecta un túnel tres saltos más adelante, en el que nadie de los que están en la sala está pensando en ese momento.

Esas no son fallas exóticas ni raras. Son las ordinarias, las de todos los meses, y lo que tienen en común es que el cambio a nivel de equipo era correcto. Nada en un diff iba a revelarlas.

Config Modeling responde la pregunta del radio de impacto antes de que abra la ventana de mantenimiento, como parte de la revisión, en vez de dejar que la descubra el tráfico real a las dos de la mañana. El resultado no es un aprobado o un rechazado. Es una lista de qué más queda afectado, que es exactamente lo que el revisor necesitaba tener delante para poder aprobar bien desde el principio.

Un cambio aprobado es uno que alguien consideró seguro. Un cambio modelado es uno en el que la pregunta de verdad se hizo.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #GestionDeCambios

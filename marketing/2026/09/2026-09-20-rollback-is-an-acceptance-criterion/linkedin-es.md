# LinkedIn (ES) — rollback-is-an-acceptance-criterion


Casi todo registro de cambio tiene un plan de reversión. Muchos menos tienen una reversión (rollback) que alguna vez se haya ejecutado.

La versión habitual dice algo como "volver a la configuración anterior". Eso es una frase, no un procedimiento. No dice dónde está guardada esa configuración, si es la running o la startup, qué pasa con el estado acumulado desde entonces, ni cuánto tarda la vuelta atrás en un equipo que necesita un reload para aplicarla.

Bajo presión, a las 2 de la mañana, ese vacío es donde la interrupción se alarga en lugar de acortarse.

Y la configuración casi nunca es lo difícil. Lo que complica una vuelta atrás es el estado que se acumuló mientras el cambio estuvo activo: sesiones establecidas, entradas aprendidas, un vecino que reconvergió alrededor de la topología nueva y que ahora tendrá que reconverger de regreso. Una reversión que restaura la configuración e ignora el estado es la forma en que una interrupción sobrevive al arreglo que la causó.

Nosotros tratamos la reversión como criterio de aceptación, no como documentación. Un cambio automatizado no está terminado hasta que el camino inverso se haya ejecutado — primero contra el modelo, después en laboratorio o en un sitio canario — y el tiempo que toma sea un número conocido y no una estimación.

Suena a sobrecarga. Es justamente lo que hace rápido a todo lo demás, porque un cambio que usted puede deshacer de forma confiable se aprueba por sus méritos y no por su radio de impacto. Los equipos que pueden revertir en minutos aprueban más cambios, no menos.

La pregunta que vale hacerse sobre su último cambio automatizado: ¿alguien ejecutó la reversión, o solo existe en papel?

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #InfraestructuraComoCodigo

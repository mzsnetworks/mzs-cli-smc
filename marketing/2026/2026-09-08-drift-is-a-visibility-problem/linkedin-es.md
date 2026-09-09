# LinkedIn (ES) — drift-is-a-visibility-problem


Prueba rápida para equipos de redes multi-sitio:

¿Puede afirmar, con confianza, qué está configurado realmente en cada equipo de cada sitio — ahora mismo?

No lo que dice el documento de estándares. No lo que dicen los tickets de cambio. Lo que de verdad está ahí.

Para la mayoría de los equipos, la respuesta honesta es no. Las configuraciones se desvían:
— un arreglo de emergencia a las 3 de la mañana que nunca se documentó
— la solución "temporal" de un ingeniero de sitio, que ya lleva dos años
— una actualización de plantilla que llegó a 38 de 40 sitios

Y aquí está la parte que casi siempre se diagnostica mal. Cada una de esas decisiones fue razonable, tomada por un ingeniero competente. El arreglo de las 3 de la mañana restableció el servicio. La solución temporal desbloqueó un proyecto que ya iba tarde. La plantilla alcanzó dos equipos que esa noche estaban inaccesibles, Ansible registró los fallos, y la ejecución siguió adelante.

Nadie fue descuidado. La desviación de configuración no aparece cuando la gente deja de seguir el proceso. Aparece cuando el proceso no tiene forma de avisarle que no terminó.

Por eso más disciplina no lo resuelve. Un control de cambios más estricto y listas de verificación más largas gobiernan lo que usted pretende desplegar. Nada de eso lee la configuración en ejecución para decirle qué hay realmente.

Entonces llega la auditoría, y la validación de cumplimiento se convierte en semanas de comparaciones manuales.

Para eso construimos Driftguard — detección continua de desviación de configuración en todos los sitios, para que la respuesta a "¿qué está desplegado?" sea un dashboard y no un proyecto de arqueología.

La desviación no es un problema de disciplina. Es un problema de visibilidad. Resuelva la visibilidad.

Reserve una consulta: mzsnetworks.com

#AutomatizacionDeRedes #Cumplimiento #NetOps

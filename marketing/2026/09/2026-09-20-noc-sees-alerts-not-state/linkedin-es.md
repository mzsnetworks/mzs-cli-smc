# LinkedIn (ES) — noc-sees-alerts-not-state


Hágale a su centro de operaciones una pregunta que no sea una alerta y observe qué pasa.

"¿Cuántos sitios están corriendo la imagen aprobada?"
"¿Qué circuitos estamos pagando que no llevan tráfico?"
"¿Qué cambió en las últimas 24 horas, y quién lo hizo?"

La mayoría de los NOC no puede responder esto en el momento, y no es un problema de competencia. Fueron instrumentados para reportar eventos: algo cruzó un umbral, algo dejó de responder. Los eventos son necesarios. También son una descripción de lo que salió mal, no de lo que hay.

Y la diferencia no es de herramienta sino de pregunta. Un sistema de eventos responde "¿qué se rompió?". Un sistema de estado responde "¿qué hay?". La segunda pregunta es la que hacen las auditorías, las renovaciones de contrato y cualquier persona de finanzas, y es justo la que nadie instrumentó.

La consecuencia es sutil. Los equipos se vuelven muy buenos reaccionando y quedan ciegos ante la acumulación: las versiones de imagen separándose, el circuito que nadie canceló, el cambio que estaba bien solo y menos bien combinado con los otros dos de esa semana.

Cerrar esa brecha significa agregar estado en lugar de eventos — inventario, versiones, postura de configuración, historial de cambios — en una vista que alguien realmente abra. Para eso construimos ITOC Dashboard, y es lo que casi todo trabajo de orquestación termina produciendo como efecto secundario, porque no se puede orquestar entre sistemas sin antes reconciliar lo que cada uno cree.

La prueba es simple: ¿puede alguien fuera del equipo de redes obtener una respuesta correcta sin preguntarle a un ingeniero?

Reserve una consulta: mzsnetworks.com

#NetOps #AutomatizacionDeRedes #IngenieriaDeRedes

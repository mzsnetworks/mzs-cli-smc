# LinkedIn (ES) — what-happens-at-step-four


Una automatización de seis pasos que falla en el paso cuatro es peor que una que nunca se ejecutó.

Que nunca se ejecutó es un estado conocido. Usted está exactamente donde empezó, no hay nada aplicado a medias, y lo peor que puede pasar es que alguien lo haga a mano. Que falló en el paso cuatro es un estado que nadie diseñó: cuatro cambios aplicados, dos no, y ningún registro de cuáles fueron cuáles.

Esta es la línea real entre un script y un flujo de trabajo, y no tiene que ver con el lenguaje ni con la herramienta. Un script ejecuta pasos. Un flujo de trabajo sabe en qué punto está.

Tres cosas hacen concreta esa diferencia.

Registra el estado a medida que avanza, de modo que una falla deja un relato de lo que se completó y no un buffer de terminal que alguien tiene que leer. Es idempotente, así que la corrección es volver a ejecutarlo y no deducir a mano qué pasos hay que saltarse. Y le avisa a una persona con nombre, con contexto suficiente para que pueda actuar, en lugar de salir con código distinto de cero hacia un log que nadie está mirando a las 2 de la mañana.

Lo que vuelve esto urgente es la escala, más que la complejidad. Un trabajo de seis pasos contra un solo equipo se recupera leyendo la terminal. El mismo trabajo sobre doscientos sitios, que falla en once por tres motivos distintos, no. Ahí el scripting improvisado deja de ser ahorro y empieza a ser el riesgo.

Esto lo construimos con Workflow Engine sobre las API que usted ya tiene, para que la secuencia, los reintentos y el registro vivan en un solo lugar y no dentro de cada script. Los artefactos ordinarios siguen siendo ordinarios: Python y Ansible por debajo, porque usted tiene que poder contratar gente para eso y poder leerlo.

La pregunta que hay que hacerle a cualquier automatización de la que usted dependa no es si funciona. Es qué deja atrás cuando se detiene a la mitad.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #Orquestacion

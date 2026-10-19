# LinkedIn (ES) — api-first-is-not-a-feature


"Tiene API" aparece en todas las fichas de producto y no le dice casi nada sobre si usted va a poder automatizar contra esa plataforma.

La respuesta real la descubrimos durante el trabajo de integración, normalmente en la primera semana, y conviene saberla antes de la compra y no después de firmarla.

Cuatro cosas la deciden.

Si escribe, o solamente lee. Una API de solo lectura le da reportería. No le da aprovisionamiento, y esa diferencia es el caso de negocio completo de muchos proyectos. Los fabricantes rara vez son explícitos sobre qué operaciones están realmente expuestas.

Si soporta operaciones masivas. Un endpoint que maneja un objeto por llamada es una herramienta distinta de uno que acepta un lote completo. Con cuatrocientos objetos y un límite de tasa, las llamadas por objeto convierten una tarea de mantenimiento en un trabajo de toda la noche, y la lógica de reintentos que ahora usted tiene que escribir es justo donde viven los errores.

Si los errores son utilizables. Una falla que devuelve un motivo específico se puede manejar de forma automática. Una que devuelve un fallo genérico con estado 200 necesita que una persona lo interprete, lo que significa que la automatización deja de ser desatendida.

Si está versionada, y qué pasa cuando hay actualización. Una API que cambia de forma sin aviso convierte cada actualización de plataforma en una interrupción de la automatización de la que usted se entera después.

Nada de esto exige una evaluación larga. Exige pedir credenciales a una instancia de prueba y dedicar dos días a escribir contra ella en Python antes de firmar el contrato, en lugar de descubrirlo en el segundo mes de un proyecto que se dimensionó asumiendo que iba a funcionar.

Una API es una superficie de producto y, como tal, tiene una calidad. Trátela como algo que se evalúa, no como algo que se da por hecho.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #IntegracionDeAPI

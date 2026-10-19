# LinkedIn (ES) — a-dry-run-is-not-a-test


"Lo corrimos en dry run" se dice en los comités de cambio como si eso cerrara la discusión. No la cierra.

Un dry run le dice que el cambio es sintácticamente válido y que el equipo lo va a aceptar. Eso sirve de verdad y no es poca cosa. También es la más pequeña de las preguntas que vale la pena hacerse, y la que menos probabilidades tiene de ser el motivo por el que un cambio sale mal.

Los cambios que provocan interrupciones casi siempre se aceptan a la perfección. El comando era válido. El equipo lo tomó sin protestar. Lo que falló después fue una dependencia que nadie modeló, un patrón de tráfico que la prueba nunca generó, o un vecino que reconvergió como el diagrama no anticipaba.

Por eso nosotros separamos cuatro etapas distintas, porque cada una responde una pregunta que la anterior no alcanza a responder.

El dry run responde si la sintaxis es correcta. El modelo responde qué le hace el cambio a la topología prevista, incluidas las partes en las que usted no estaba pensando. Un laboratorio o un sitio canario responde cómo se comporta el tráfico real contra ese cambio, que es donde viven las sorpresas de verdad. Y producción con una reversión (rollback) ensayada responde la única pregunta que hizo el negocio, que es si el servicio sigue funcionando.

Los equipos saltan directo a la última etapa porque las tres primeras cuestan tiempo y el cambio parecía sencillo. Es una decisión defendible en un cambio cuyo radio de impacto es pequeño y está bien entendido. En cualquier otro caso, es la forma en que un martes se convierte en una noche larga.

Nada de esto exige más herramientas de las que la mayoría de los parques ya tiene. Exige acordar qué etapa tiene que superar cada tipo de cambio antes de entrar a una ventana, y escribirlo una sola vez en lugar de decidirlo bajo presión.

Válido no es lo mismo que seguro. Un dry run demuestra lo primero, y solo lo primero.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #GestionDeCambios

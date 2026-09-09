# LinkedIn (ES) — automation-isnt-the-risk


"¿Y si el script rompe producción?"

Es la primera pregunta que nos hace cada equipo de redes. Y es la pregunta correcta.

Los cambios manuales parecen más seguros porque hay un humano vigilando. Pero esto es lo que me enseñaron 19 años operando redes en producción: el humano que vigila a las 2 de la mañana, en la ventana de cambio número 47, es el riesgo.

No por descuido. Porque un cambio manual no deja nada que se pueda revisar. Ningún diff que leer antes de ejecutarlo. Ningún registro de lo que realmente se escribió, frente a lo que decía el ticket. Ninguna garantía de que el sitio 40 recibió lo mismo que el sitio 1.

El miedo detrás de la pregunta es el alcance del impacto: un script, cuarenta sitios, un error. Ese miedo es legítimo. Pero el ingeniero que se equivoca al teclear una VLAN a las 2 de la mañana también tiene un alcance. Solo que usted no se entera de cuál fue hasta que algo se rompe el martes siguiente.

La automatización bien hecha no es un script que alguien ejecuta esperando que funcione.

Es un cambio que está:
— probado contra un modelo de su red antes de tocar un solo equipo
— revisado por pares como se revisa el código, porque es código
— aprobado, registrado y trazable
— revertido en minutos (rollback), no reconstruido de memoria

Así construimos la automatización en MZS Networks. Python, Ansible, Terraform — con las prácticas de seguridad de ingenieros que operan producción y responden por lo que entregan.

La automatización no es el riesgo. El cambio sin revisión sí lo es.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #InfraestructuraComoCodigo #NetOps

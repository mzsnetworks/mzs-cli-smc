# LinkedIn (ES) — tools-that-dont-talk


Cuente los sistemas que toca un solo cambio rutinario en su empresa.

Se abre un ticket. Alguien revisa el monitoreo para confirmar el síntoma. Alguien entra a la plataforma de red y aplica el cambio. Alguien actualiza el ticket. Tal vez se corrige el CMDB, tal vez no. Tal vez se ajusta el umbral de monitoreo al nuevo estado, normalmente después.

Todos esos sistemas tienen API. Casi ninguno está conectado con los demás.

Lo que llena el hueco es una persona moviendo información entre pestañas del navegador. Esa persona es además el punto de falla: cuando está de vacaciones el proceso se degrada, y cuando está ocupada el CMDB es el paso que se salta. Ese rol no está en ningún organigrama y sin embargo existe, y la mayoría de los equipos solo descubre cuánto dependía de él cuando esa persona cambia de puesto.

Este es el trabajo de automatización menos vistoso que existe y con frecuencia el de mayor retorno, porque no está reemplazando criterio de ingeniería — está reemplazando transcripción. El ticket se abre, corre el enriquecimiento, el cambio se ejecuta contra la plataforma, el ticket se actualiza solo, el inventario se reconcilia, el monitoreo se ajusta.

Esto lo construimos como orquestación sobre lo que usted ya tiene, a través de las API que esos productos ya traen. Workflow Engine es la pieza que lo secuencia, con las mismas reglas de seguridad que cualquier otro cambio: probado, revisado, trazable, reversible.

Nadie pone "menos cambio de pestañas" en un caso de negocio. Ahí siguen estando las horas.

Hable con un ingeniero: mzsnetworks.com

#AutomatizacionDeRedes #NetOps #InfraestructuraComoCodigo

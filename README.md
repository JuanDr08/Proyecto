> Revisado 08/02/2024

<img src="https://github.com/JuanDr08/proyectoPython/blob/main/img/1.jpg" width="400" height="400">

<img src="https://github.com/JuanDr08/proyectoPython/blob/main/img/2.jpg" width="400" height="400">

<img src="https://github.com/JuanDr08/proyectoPython/blob/main/img/3.jpg" width="400" height="400">

<img src="https://github.com/JuanDr08/proyectoPython/blob/main/img/4.jpg" width="400" height="400">

<img src="https://github.com/JuanDr08/proyectoPython/blob/main/img/5.jpg" width="400" height="400">

<img src="https://github.com/JuanDr08/proyectoPython/blob/main/img/6.jpg" width="400" height="400">





I created the readme file after start and give structure to the project because i forget create the file before, srry

In this commit I wasted a lot of time because I was experimenting with json to try to understand the mechanism I had to use to save campers, if they existed then overwrite them, save new ones more and more and more things with json



### Tener en cuenta

* no permitir crear salas ni rutas vacias o que solo sean textos en blanco
* evitar bugs en los cruds: 
  * no permitir hacer ninguna ota opcion si no hay al menos un camper creado✔️



**Pruebas Examenes Modulos**

    * solo a grupos ya creados ✔️

    * ingresasr grupo a calificar✔️

    * verificar si el grupo existe ✔️

    * con campers asignados✔️

    * opcion para calificar 1 modulo especifico ✔️

    * verificar que el modulo exista✔️

    * calificacion camper x camper✔️

    * verificar que camper exista✔️

    * verificar que el modulo no este calificado, sino que no aparezca✔️

    * cambiar estado de modulo a calificado o no calificado ✔️

    * si pierde un modulo pasa a riesgo ✔️

    * si pierde dos pasa a filtrado ✔️

    * sumar uno a la sala del estudiante ✔️





* apenas se actualiza el modulo del camper al que se le registraron notas agregar el verificador de cuantos modulos lleva perdidos y ajustar el estado segun eso ✔️
  * si es filtrado sacarlo de la sala inmediatamente y preguntar si tambien se
    le elimina al trainer✔️

#### CRUD CAMPER 

    -	permitir modificar numero, acudiente, identificacion
    -	al eliminar un camper, eliminar tambien su registro en todas las posibles variables
    -	verificar porque al crear un nuevo camper se le cambian los estados a los otros✔️

**VERIFICAR CORRECTO FUNCIONAMIENTO**

    -	Nota de prueba de seleccion ver que pasa si ingreso str
    -	inscribir dos campers al mismo grupo y hacerlos presentar la misma prueba de modulo dos veces una en unrated y otra rated
    -	verificar que si ingreso un codigo de modulo no existente no se guarde en el json en la creacion de ruta
    -	ver si me deja agregar campers a una sala llena, luego filtrar uno de esa sala y volver a mirar si me deja ingresar ahora si uno nuevo

**AGREGAR**

    -	Modificacion manual de los estados de campers en el menu de coordinacion
    -	reportes
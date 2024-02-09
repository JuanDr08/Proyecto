import os, json

def selection():
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        dato = json.load(file)
    if(len(data) >=1):
        input("Para realizar la prueba de seleccion acontinuacion se le mostraran todos los aspirantes disponibles")
        input("Debera asignar la nota obtenida por cada alumno uno por uno (enter para continuar)")
        contador = 0
        for key, value in data.items():
            os.system("cls")
            if (value.get("estado")== "PRE-INSCRITO"):
                print(f"""
                
            -----------------------------
            Identificacion : {key}
            Nombre : {value.get("nombre")}
            Apellido : {value.get("apellido")}
            Estado : {value.get("estado")}
        """)
                nota = (int(input("Cual fue la nota teorica del camper? -> ")) + int(input("Cual fue la nota practica del camper? ->")))/2
                dato.get("seleccion").update({key : {
                    "hora" : input("A que hora presento la prueba el camper? -> "),
                    "nota" : nota
                }                    
            })
                if( nota >= 60):
                    value["estado"] = "INSCRITO"
                    input("El camper fue aprobado, ha logrado ingresar al equipo campus")
                    dato["seleccion"][key].update({"estado" : "APROBADO"})
                else:
                    value["estado"] = "FILTRADO"
                    input("El camper no ha logrado ingresar a campus, lo sentimos")
                    dato["seleccion"][key].update({"estado" : "FILTRADO"})
            else:
                contador += 1
        if (contador == len(data) or len(data) < 1):
            os.system("cls")
            input("Actualmente no hay campers registrados con estado pre-inscrito")
                
    else:
        os.system("cls")
        input("No hay ningun camper registrado")
    with open("data\Coordinacion.json", "w") as file:
        json.dump(dato, file, indent = 4)
        file.close()
    with open("data\Campers.json", "w") as file:
        json.dump(data, file, indent=4)
        file.close()
def pruebas():
    with open("data\Campers.json", "r") as file:
        camp = json.load(file)
    with open("data\Trainers.json", "r") as file:
        trai = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        admin = json.load(file)
    bandera=True
    while bandera:
        os.system("cls")
        if (len(admin["classrooms"]) < 1):
            input("No hay grupos creados, debera crear al menos uno para poder crear notas")
            bandera = False
        else:
            print("Grupos disponibles para realizar pruebas\n")
            for key, valor in admin["classrooms"].items():
                if(len(valor["campers"]) < 1):
                    print(f"- El grupo {key} no tiene campers asignados")
                else:
                    print(f"- Grupo {key}")
            grupo = input("\nIngrese el grupo de campers que desea realizar pruebas -> ").lower()
            if(grupo not in admin["classrooms"]):
                os.system("cls")
                input("El grupo que ingreso no existe, ingrese uno de los anteriormente mostrados")
                bandera = False
            elif(len(admin["classrooms"][grupo]["campers"]) < 1):
                os.system("cls")
                input(f"No hay campers registrados en el grupo {grupo}")
                bandera = False
            else:
                os.system("cls")
                print(f"""
                ***************
                *   REGLAS    *
                ***************""")
                input("1. Se le mostraran todos los modulos del grupo disponibles para calificar\ndebera ingresar exactamente el que desea calificar")
                input("2. Una vez decidido el modulo a calificar debera ingresarle a todos los campers del grupo sus respectivas notas")
                os.system("cls")
                modul = admin["classrooms"][grupo]["ruta"]
                print(f"""
        Modulos disponibles
    --------------------------
                    """)
                for key, value in admin["rutas"][modul]["modulo"].items():
                    print("- ",key)
                modulo = input("\nIngrese el nombre del modulo que desea calificar -> ").lower()
                if (modulo not in admin["rutas"][modul]["modulo"]):
                    os.system("cls")
                    input(f"El modulo {modulo} no existe, porfavor ingrese uno de los disponibles")
                else:
                    os.system("cls")
                    input(f"Campers que presentaran las pruebas del modulo {modulo}\n")
                    contador = 0
                    for key, value in camp.items():
                        if(grupo not in value):
                            pass
                        elif (value[grupo][modulo]["estado"] == "RATED"): # evaluar la forma de que si un camper tiene estado filtrado pase de el para no borrarle el registro de donde estuvo
                            contador += 1
                        else:
                            print(f"- Camper {value['nombre']} con identificacion {key}\n")
                    os.system("pause")
                    if(contador == len(camp)):
                        os.system("cls")
                        input(f"Actualmente no hay campers del grupo {grupo} que no hayan presentado las pruebas del modulo {modulo}")
                    else:
                        for key, value in camp.items():
                            os.system("cls")
                            if(grupo not in value):
                                pass
                            elif (value[grupo][modulo]["estado"] == "UNRATED"):
                                print(f"Estudiante : {value['nombre']} identificacion : {key}")
                                proyecto = int(input(f"Ingrese la nota que el estudiante saco en el proyecto -> "))*0.6
                                exam = int(input("Ingrese la nota que el estudiante saco en el examen -> "))*0.3
                                general = int(input("Ingrese la nota total que el estudiante saco en los trabajos generales -> "))*0.1
                                camp[key][grupo][modulo].update({
                                    "proyecto" : proyecto,
                                    "examen" : exam,
                                    "general" : general,
                                    "total" : (proyecto+exam+general),
                                    "fecha" : input("Cuando presento el camper la prueba? -> "),
                                    "estado" : "RATED"
                                })
                                filtro = 0
                                for key2, valor in camp[key][grupo].items():
                                    if("total" not in valor):
                                        pass
                                    elif (valor["total"] < 60):
                                        filtro += 1
                                    if(filtro == 1):
                                        camp[key]["estado"] = "RIESGO"
                                    elif(filtro == 2):
                                        camp[key]["estado"] = "FILTRADO"
                                        camp[key].pop(grupo)
                                        admin["classrooms"][grupo]["capacidad"] += 1
                                        admin["classrooms"][grupo]["campers"].pop(key)
                                        for llave, val in admin["classrooms"][grupo]["trainer"].items():
                                            trai[llave][grupo].pop(key)
                                        break
                                with open("data\Campers.json", "w") as file:
                                    json.dump(camp, file, indent = 4)
                                    file.close()
                                with open("data\Trainers.json", "w") as file:
                                    json.dump(trai, file, indent = 4)
                                    file.close()
                                with open("data\Coordinacion.json", "w") as file:
                                    json.dump(admin, file, indent = 4)
                                    file.close()
                                os.system("cls")
                                input("Notas guardadas exitosamente")
                        bandera = False
def ruta():
    with open("data\Coordinacion.json", "r") as file:
        data = json.load(file)
    print(f"""
    **************
    *    LEER    *
    **************
""")
    input("Para crear una ruta debera tener modulos creados, lo primero que hara sera crear los modulos a asignar (enter para continuar)")
    input("Cada modulo tiene 5 submodulos, los cuales son los pasos a seguir para completar el modulo")
    os.system("cls")
    if (int(input("1. crear modulos\n0. usar modulos ya creados\n-> "))):
        for x in range(int(input("Cuantos modulos desea agregar? -> "))):
            os.system("cls")
            data.get("modulos").update({str(len(data.get("modulos")) + 1).zfill(4) : {
                input(f"Ingrese el nombre del modulo {x + 1} -> ").lower() : input("Ingrese el temario -> ").upper()for x in range(5)
            }})
        input("Modulo creado exitosamente, falta agregarlo a una ruta")
    else:
        os.system("cls")
        if (len(data.get("modulos")) >= 1):
            print("Modulos disponibles para asignar a la ruta...")
            for key, value in data.get("modulos").items():
                print(f"""
        Codigo : {key}
    """)        
                contador = 1
                for key2, val in data.get("modulos")[key].items():
                    print(f"""
            Temario {contador} = {key2} : {val}
    """)
                    contador += 1
            modulos = input("Ingrese el codigo de los modulos que asignara a esta ruta -> ")
            if(modulos not in data["modulos"]):
                os.system("cls")
                input("El codigo de ese modulo no existe, porfavor ingrese uno de los mostrados")
            else:
                data.get("rutas").update({input("Ingrese el nombre de la ruta (programa al que estara orientado el aprendizaje) -> ").lower(): {
                    "modulo" : data.get("modulos")[modulos]
                }})
                input("Ruta creada exitosamente")
        else:
            os.system("cls")
            input("No hay modulos disponibles para poder crear una ruta...")
    with open("data\Coordinacion.json", "w") as file:
        json.dump(data, file, indent = 4)
def rooms():
    with open("data\Coordinacion.json", "r") as file:
        data = json.load(file)
    try:
        sala = input("Ingrese el nombre de la sala -> ").lower()
        if (sala not in data.get("rooms")):
            data.get("rooms").update({sala : {
                "capacidad" : int(input("Ingrese la capacidad maxima de la sala -> ")),
                "estado" : {
                    value : "VACIO" for key, value in data.get("horarios").items()
                }
            }})
            with open("data\Coordinacion.json", "w") as file:
                json.dump(data, file, indent = 4)
                file.close()
        else:
            os.system("cls")
            input("La sala ya existe, pruebe otro nombre")
    except ValueError:
        os.system("cls")
        input("Ingrese un digito correto")
def giveroom():
    with open("data\Campers.json", "r") as file:
        camp = json.load(file)
    with open("data\Trainers.json", "r") as file:
        trai = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        admin = json.load(file)
    if(len(camp) < 1):
        input("No hay campers registrados para poder asignar a salas de entrenamiento")
    elif(len(trai) < 1):
        input("No hay trainers registrados para poder asignar a una sala de entrenamiento")
    elif(len(admin.get("rutas")) < 1):
        input("No hay rutas creadas para poder asignar a una sala de entrenamiento")
    elif(len(admin.get("rooms")) < 1):
        input("No hay aulas creadas para poder asignar un entorno de entrenamiento")
    else:
        try:
            add = int(input("1. Si quiere crear una sala desde cero\n2. Si quiere añadir campers a una sala ya creada\n-> "))
            match(add):
                case 1:
                    os.system("cls")
                    input("Para asignar una sala se le pediran unos datos paso por paso, porfavor sigalos al pie de la letra")
                    input("Primero asignara la ruta")
                    while True:
                        os.system("cls")
                        print("Rutas disponibles")
                        for key, value in admin.get("rutas").items():
                            print(f"Ruta : {key}")
                        ruta = input("Ingrese la ruta que veran los miembros del grupo -> ").lower()
                        if (ruta not in admin["rutas"]):
                            os.system("cls")
                            input("Esa ruta no existe, porfavor ingrese una de las disponibles")
                        else:
                            os.system("cls")
                            input("Ruta añadida al grupo exitosamente")
                            os.system("cls")
                            input("Estos son los trainers y sus horarios disponibles para asignar a la clase")
                            for key, valor in trai.items():
                                print(f"\n- Trainer {valor['nombre']} Disponible en los siguientes horarios:\nIdentificacion del trainer: {key}\n")
                                for key2, valor2 in trai[key].get("horario").items():
                                    if (valor2 != "OCUPADA"):
                                        print(f"* {key2} Libre")
                                    else:
                                        print(f"* {key2} OCUPADA")
                            trainer = input("\nIngrese la identificacion del trainer que desea que trabaje con este grupo -> ")
                            if trainer not in trai:
                                os.system("cls")
                                input("No se ha encontrado un trainer con esta identificacion registrada, asegurese de escribirla bien")
                            else:
                                hora = input("Ingrese la hora que quiere asignar a este grupo -> ").lower()
                                if(hora not in trai[trainer]["horario"]):
                                    os.system("cls")
                                    input("Esa hora no existe, ingrese una de las que estan disponibles")
                                elif(trai[trainer]["horario"][hora] == "OCUPADA"):
                                    os.system("cls")
                                    input("El trainer ya tiene ocupada esa hora, igrese una diferente")
                                else:
                                    print("\n- Salas disponibles a esta hora\n")
                                    for key, valor in admin.get("rooms").items():
                                        print(f"* Sala {key} en el horario de {hora} esta {valor['estado'][hora]}")
                                    sala = input("\nIngrese la sala que quiere asignar a este grupo -> ").lower()
                                    if(sala not in admin["rooms"]):
                                        os.system("cls")
                                        input("Esa sala no existe, ingrese una que si exista")
                                    elif((admin["rooms"][sala]["estado"][hora] == "OCUPADA")):
                                        os.system("cls")
                                        input(f"La sala {sala} ya esta ocupada a la hora {hora}, porfavor ingrese una sala que este disponible")
                                    else:
                                        counter = len(admin["classrooms"]) + 1
                                        code = ruta[0:1]+str(counter)
                                        admin.get("classrooms").update({code : {
                                            "ruta" : ruta 
                                        }})
                                        trai[trainer]["horario"][hora] = "OCUPADA"
                                        admin["rooms"][sala]["estado"][hora] = "OCUPADA"
                                        admin["classrooms"][code].update({
                                            "trainer" : {trainer : trai[trainer]["nombre"]},
                                            "capacidad" : admin["rooms"][sala]["capacidad"],
                                            "campers" : {},
                                            sala : hora,
                                            "inicio" : input("Ingrese la fecha de inicio de entrenamiento de este grupo -> "),
                                            "fin" : input("Ingrese la fecha de finalizacion de entrenamiento de este grupo -> ")
                                        })   
                                        trai[trainer].update({code : {"sala" : sala}}) 
                                        input("Trainer, Hora y sala asignada correctamente")
                                        with open("data\Trainers.json", "w") as file:
                                            json.dump(trai, file, indent=4)
                                            file.close()
                                        with open("data\Coordinacion.json", "w") as file:
                                            json.dump(admin, file, indent=4)
                                            file.close()
                                        break
                case 2:
                    bandera2 = True
                    while bandera2:
                        os.system("cls")
                        if (len(admin["classrooms"]) >= 1):
                            print("Estos son los grupos disponibles para asignar campers\n")
                            for key, value in admin["classrooms"].items():
                                print(f"Gupo {key} cuenta con {value['capacidad']} espacios disponibles")
                            grupo = input("\nIngrese el grupo al que desea asignar a los campers\n-> ").lower()
                            if (grupo not in admin["classrooms"]):
                                os.system("cls")
                                input("Ese grupo no existe, ingrese uno de los mostrados")
                            elif(admin["classrooms"][grupo]["capacidad"] < 1):
                                os.system("cls")
                                input("El grupo ya no tiene capacidad para mas campers, ingrese uno que si tenga")
                            else:
                                contador = 0
                                for key,value in admin["seleccion"].items():
                                    if("estado" not in value):
                                        pass
                                    elif(value["estado"] == "APROBADO"):
                                        contador += 1
                                if(contador == len(admin["seleccion"]) and len(admin["seleccion"]) >= 1):
                                    os.system("cls")
                                    input("Los campers que aprobaron la prueba de seleccion ya se encuentran todos asignados a un grupo, por lo que no hay nada que asignar")
                                    bandera2 = False
                                elif (len(admin["seleccion"]) < 1):
                                    input("No hay campers que hayan aprobado la prueba de seleccion, revise si hay campers por presentar")
                                    bandera2 = False
                                else:
                                    os.system("cls")
                                    for key, val in camp.items():
                                        if(val["estado"] == "INSCRITO"):
                                            print(f"""
                                            * Identificacion : {key} Nombre : {val["nombre"]}
                                        """)
                                    camper = input("Ingrese la identificacion del camper que desea ingresar al grupo\n-> ")
                                    if(camper not in camp):
                                        os.system("cls")
                                        input("No se ecuentran coincidencias con la identificacion registrada, ingrese un camper existente")
                                    elif(camp[camper]["estado"] != "INSCRITO"):
                                        os.system("cls")
                                        input("Ese camper no se encuentra en el estado requerido para asignar ruta, pruebe con otro")
                                    else:
                                        os.system("cls")
                                        if(int(input("Esta seguro que desea agregar al camper a este aula?\n1. si\n0. no\n-> "))):
                                            rout = admin["classrooms"][grupo]["ruta"]
                                            admin["classrooms"][grupo]["campers"].update({camper : camp[camper]["nombre"]})
                                            camp[camper].update({grupo : {
                                                key : {"estado" : "UNRATED"} for key, value in admin["rutas"][rout]["modulo"].items()
                                                
                                            }})
                                            camp[camper]["estado"] = "APROBADO"
                                            admin["classrooms"][grupo]["capacidad"] -= 1
                                            for key, value in trai.items():
                                                if(grupo in value):
                                                    trai[key][grupo].update({camper : camp[camper]["nombre"]})
                                            with open("data\Campers.json", "w") as file:
                                                json.dump(camp, file, indent = 4)
                                            with open("data\Trainers.json", "w") as file:
                                                json.dump(trai, file, indent = 4)
                                            with open("data\Coordinacion.json", "w") as file:
                                                json.dump(admin, file, indent = 4)
                                            os.system("cls")
                                            input("Camper añadido exitosamente")
                                            os.system("cls")
                                            bandera2 = bool(int(input("Desea añadir otro camper?\n1. si\n0. no\n-> ")))
                                        else:
                                            bandera2 = True
                        else:
                            input("No hay clases creadas para asignar a algun camper")
                            bandera2 = False
                case _:
                    os.system("cls")
                    input("Ingrese una opcion de las disponibles")
        except ValueError:
            os.system("cls")
            input("Ingrese un digito valido")
def reportes():
    os.system("cls")
    with open("data\Campers.json", "r") as file:
        camp = json.load(file)
    with open("data\Trainers.json", "r") as file:
        trai = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        admin = json.load(file)
    counter = 0
    nombre = "nombre"
    input("A. Campers que se encuentran en estado inscrito\n")
    if(len(camp) < 1):
        print("Actualmente no hay campers registrados para observar su estado, registre unos campers y realice la prieba inicial...")
    else:
        counter = 0
        for key, value in camp.items():
            if (value["estado"] == "INSCRITO"):
                print(f"* El camper {value['nombre']} con identificacion {key} se encuentra en estado {value['estado']}")
            else:
                counter += 1
        if (counter == len(camp)):
            print("De los campers actualmente activos ninguno se encuentra en estado INSCRITO")
    input("\nB. Campers que aprobaron el examen inicial\n")
    if (len(admin["seleccion"]) < 1):
        print("No hay campers que hayan realizado la prueba de seleccion, porfavor revise si tiene campers pendientes por presentar la prueba...")
    else:
        counter = 0
        for key, value in admin["seleccion"].items():
            if (value['estado'] == 'APROBADO'):
                print(f'* El camper {camp[key][nombre]} aprobo el examen inicial')
            else: counter += 1 
        if(counter == len(admin["seleccion"])):
            print("Los campers que presentaron prueba de seleccion hasta el momento fueron filtrados")
    input("\nC. Trainers que se encuentran trabajando actualmente en campus\n")
    if (len(trai) < 1):
        print('Actualmente no se ecuentran treiners trabajando en campus')
    else:
        for key, value in trai.items():
            print(f"trainer {value[nombre]} con identificacion {key}")
    input("\nD. Campers en bajo rendimiento (Riesgo)\n")
    if (len(camp) < 1):
        print("No hay campers registrados para poder observar los estados")
    else:
        counter = 0
        for key, value in camp.items():
            if (value["estado"] == "RIESGO"):
                print(f"Camper {value['nombre']} con identificacion {key} se encuentra en riesgo")
            else:
                counter += 1
        if(counter == len(camp)):
            print("Actualmente no hay campers en riesgo")
    input("\nE. Campers y trainers asociados a cada uno de los grupos de entrenamiento\n")
    if(len(admin["classrooms"]) < 1):
        print("No hay grupos de entrenamiento creadas por lo que no hay campers ni trainers asociados")
    else:
        for key, value in admin["classrooms"].items():
            print(f"Grupo {key}")
            for llave, valor in value["trainer"].items():
                if(len(value["campers"]) < 1):
                    print(f"Trainer {llave} : {valor}\n- No tiene campers asociados\n")
                else:
                    print(f"Trainer {llave} : {valor}")
                    print("- campers asociados")
                    for ky, val in value["campers"].items():
                        print(f"- {ky} : {val}")
    input("\nF. Campers que perdieron y aprobaron cada modulo segun ruta de entrenamiento y trainer\n")
    if(len(admin["classrooms"]) < 1):
        input("No hay grupos de entrenamiento creados, por lo que no hay notas que que verificar")
    else:
        counter = 0
        for key, value in admin["classrooms"].items():
            if (len(value["campers"]) < 1):
                counter += 1
            else:
                print(f"- Grupo {key}")
                ruta = value["ruta"]
                print(f"- Ruta de {ruta}")
                for key2, value2 in admin["rutas"][ruta]["modulo"].items():
                    print(f"* Modulo {key2.upper()}")
                    for key3, value3 in camp.items():
                        if(key in value3 and value3[key][key2]["estado"] == "RATED"):
                            if(value3[key][key2]["total"] > 60):
                                print(f"El camper {key3} : {value3[nombre]} aprobo el modulo {key2.upper()} con una nota de {value3[key][key2]['total']}")
                            else:
                                print(f"El camper {key3} : {value3[nombre]} reprobo el modulo {key2.upper()} con una nota de {value3[key][key2]['total']}")
                        elif(key not in value3):
                            pass
                        elif (value3[key][key2]["estado"] == "UNRATED"):
                            print(f"-> modulo sin calificar aun")
                            break
                        elif (value3["estado"] == "FILTRADO" and admin["seleccion"][key3]["estado"] == "APROBADO"):
                            print(f"El camper {value3[nombre]} fue filtrado del grupo al perder dos modulos")
        os.system("pause")
        if(counter == len(admin["classrooms"])):
            input("Los grupos de entrenamiento creados no tienen ningun camper asignado, porfavor asigne campers a los grupos")

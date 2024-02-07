import os, json

def selection():
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        dato = json.load(file)
    if(len(data) >=1):
        input("Para realizar la prueba de seleccion acontinuacion se le mostraran todos los aspirantes disponibles")
        input("Debera asignar la nota obtenida por cada alumno uno por uno (enter para continuar)")
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
                if( nota >= 60):
                    value["estado"] = "INSCRITO"
                    input("El camper fue aprobado, ha logrado ingresar al equipo campus")
                else:
                    value["estado"] = "FILTRADO"
                    input("El camper no ha logrado ingresar a campus, lo sentimos")
                dato.get("seleccion").update({key : {
                            "hora" : input("A que hora presento la prueba el camper? -> "),
                            "nota" : nota
                        }                    
                    })
            else:
                os.system("cls")
                input("Actualmente no hay campers registrados con estado pre-inscrito")
                break
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
    pass
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
    if (input("Desea crear modulos o usar modulos ya creados? (1. si enter. no) ->")):
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
            data.get("rutas").update({input("Ingrese el nombre de la ruta (programa al que estara orientado el aprendizaje) -> ").lower(): {
                "modulo" : data.get("modulos")[input("Ingrese el codigo de los modulos que asignara a esta ruta -> ")]
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
        while True:
            input("Para asignar una sala se le pediran unos datos paso por paso, porfavor sigalos al pie de la letra")
            input("Primero asignara la ruta")
            os.system("cls")
            print("Rutas disponibles")
            for key, value in admin.get("rutas").items():
                print(f"Ruta : {key}")
            ruta = input("Ingrese la ruta que veran los miembros de la sala -> ").lower()
            if (ruta not in admin["rutas"]):
                os.system("cls")
                input("Esa ruta no existe, porfavor ingrese una de las disponibles")
                break
            else:
                counter = 1
                admin.get("classrooms").update({ruta[0:1]+str(counter) : {
                    "ruta" : ruta 
                }})
                os.system("cls")
                input("Ruta añadida al grupo exitosamente")
                os.system("cls")
                input("Estos son los trainers y sus horarios disponibles para asignar a la clase")
                for key, valor in trai.items():
                    print(f"\n- Trainer {valor['nombre']} Disponible en los siguientes horarios:\nIdentificacion del trainer: {key}\n")
                    for key2, valor2 in trai[key].get("horario").items():
                        if (valor2 != "OCUPADO"):
                            print(f"* {key2} Libre")
                        else:
                            print(f"* {key2} Ocupada")
                trainer = input("Ingrese la identificacion del trainer que desea que trabaje con este grupo -> ")
                if trainer not in trai:
                    os.system("cls")
                    input("No se ha encontrado un trainer con esta identificacion registrada, asegurese de escribirla bien")
                    break
                else:
                    hora = input("Ingrese la hora que quiere asignar a este grupo -> ").lower()
                    print("\n- Salas disponibles a esta hora\n")
                    for key, valor in admin.get("rooms").items():
                        print(f"* Sala {key} en el horario de {hora} esta {valor['estado'][hora]}")
                    sala = input("Ingrese la sala que quiere asignar a este grupo ").lower()
                    if(hora not in trai[trainer]["horario"]):
                        os.system("cls")
                        input("Esa hora no existe, ingrese una de las que estan disponibles")
                        break
                    elif((trai[trainer]["horario"][hora] == "OCUPADA") or (admin["rooms"][sala]["estado"][hora] == "OCUPADA")):
                        os.system("cls")
                        input("Esa hora ya esta ocupada, porfavor ingrese una que este disponible")
                        break
                    elif(sala not in admin["rooms"]):
                        os.system("cls")
                        input("Esa sala no existe, ingrese una que si exista")
                        break
                    else:
                        trai[trainer]["horario"][hora] = "OCUPADA"
                        admin["rooms"][sala]["estado"][hora] = "OCUPADA"
                        admin["classrooms"][ruta[0:1]+str(counter)].update({trainer : trai[trainer]["nombre"]})
                        admin["classrooms"][ruta[0:1]+str(counter)].update({sala : hora})              
                counter += 1
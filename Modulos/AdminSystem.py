import os, json

def selection():
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        dato = json.load(file)
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
            with open("data\Coordinacion.json", "w") as file:
                json.dump(data, file, indent = 4)
            input("Ruta creada exitosamente")
        else:
            os.system("cls")
            input("No hay modulos disponibles para poder crear una ruta...")
def rooms():
    pass
def giveroom():
    pass
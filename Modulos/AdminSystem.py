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
    input("Para crear una ruta debera tener modulos creados, lo primero que hara sera crear los modulos a asignar (enter para continuar)")
    input("Cada ruta debe tener 5 modulos asignados, por lo que debera crear 5 con el temario de su gusto")
    os.system("cls")
    data.get("modulos").update({input("Ingrese el codigo del modulo (Ej: 0001) -> ") : {
        input(f"Ingrese el nombre del modulo {x + 1} -> ").upper() : input("Ingrese el temario -> ").upper()for x in range(5)
    }})
    if (len(data.get("modulos")) >= 1):
        os.system("cls")
        print("Modulos disponibles para asignar a la ruta...")
        for key, value in data.get("modulos").items():
            print(f"""
    Codigo : {key}
""")
            for key2, val in data.get("modulos")[key].items():
                print(f"""
        Temario : {key2} : {val}
""")
        data.get("rutas").update({input("Ingrese el nombre de la ruta (progra al que estara orientado el aprendizaje) -> "): {
            "modulos" : {}
        }})
    else:
        os.system("cls")
        input("No hay modulos creados para poder crear una ruta...")

    
    
def rooms():
    pass
def giveroom():
    pass
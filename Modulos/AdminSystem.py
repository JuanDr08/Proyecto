import os, json

def selection():
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
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
            if((int(input("Cual fue la nota teorica del camper? -> ")) + int(input("Cual fue la nota practica del camper? ->")))/2 >= 60):
                value["estado"] = "INSCRITO"
                input("El camper fue aprobado, ha logrado ingresar al equipo campus")
            else:
                value["estado"] = "FILTRADO"
                input("El camper no ha logrado ingresar a campus, lo sentimos")
        else:
            os.system("cls")
            input("Actualmente no hay campers registrados con estado pre-inscrito")
    with open("data\Campers.json", "w") as file:
        json.dump(data, file, indent=4)
        file.close()
def pruebas():
    pass
def ruta():
    pass
def rooms():
    pass
def giveroom():
    pass
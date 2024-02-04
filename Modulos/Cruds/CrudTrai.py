import os, json

def create():
    print("""
     --------------------------------------
    |   Formulario Para Registrar Trainer  |
     --------------------------------------
""")
    with open("data\Trainers.json", "r") as file:
        data = json.load(file)
    data.update({input("Ingrese el numero de identificacion del trainer -> ") : {
        "nombre" : input("Ingrese nombre completo del trainer -> ").upper()
    }})
    with open("data\Campers.json", "w") as file:
        json.dump(data, file, indent = 4)
        file.close()
def read(codigo = None):
    os.system("cls")
    with open("data\Trainers.json", "r") as file:
        data = json.loads(file)
    if(codigo == None):
        print("""
     -------------------------
    |   Busqueda De Trainers  |
     -------------------------
""" )
        for key, value in data.items():
            print(f"""
    -----------------------------
    Identificacion : {key}
    Nombre Completo : {value.get("nombre")}
""")
        os.system("pause")
    else:
        os.system("cls")
        print("""
     ------------------------
    |   Actualizar  trainer  |
     ------------------------
""")
        print(f"""
    -----------------------------
    Identificacion : {codigo}
    Nombre Completo : {data[codigo].get("nombre")}
""")    
def update():
    os.system("cls")
    while True:
        read()
        tarjeta = input("Ingrese la identificacion del trainer que desea modificar -> ")
        read(tarjeta)
        print("""
¿Esta seguro que desea actualizar al trainer?
        1. Si
        2. No
        3.Cancelar
""")
        try:
            opc = int(input("Ingrese la opcion correspondiente -> "))
            match(opc):
                case 1:
                    os.system("cls")
                    input("Solo puede cambiar el nombre -> ")
                    with open("data\Trainers.json", "r") as file:
                        data = json.loads(file)
                    data[tarjeta]["nombre"] = input("Ingrese el cambio de nombre del trainer -> ")
                    with open("data\Campers.json", "w") as file:
                        json.dump(data, file, indent = 4)
                        file.close()
                case 3:
                    os.system("cls")
                    input("Volviendo...")
                    break
                case _:
                    os.system("cls")
                    input("Ingrese una opcion disponible...")
        except ValueError:
            os.system("cls")
            input("ingrese una opcion valida...")
def delete():
    pass
def menu():
    titulo = """
     -------------------------------------
    |   Bienvenido Al Menu De Trainers    |
     -------------------------------------
"""
    opciones = "1. Crear un trainer\n2. Buscar un trainer\n3. Modificar un trainer\n4. Borrar un trainer\n5. Volver"

    while True:
        os.system("cls")
        print(titulo)
        print(opciones)
        try:
            opc = int(input("Ingrese la opcion que desea realizar -> "))
            match(opc):
                case 1:
                    os.system("cls")
                    create()
                case 2:
                    os.system("cls")
                    read()
                case 3:
                    os.system("cls")
                    update()
                case 4:
                    os.system("cls")
                    delete()
                case 5:
                    os.system("cls")
                    input("Volviendo al menu principal...")
                    break
                case _:
                    input("- Porfavor ingrese una opcion valida")
        except ValueError:
            input("- Porfavor ingrese un dato valido...")
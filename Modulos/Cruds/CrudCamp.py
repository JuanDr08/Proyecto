import os, json
def create():
    titulo = """
     --------------------------------------
    |   Formulario Para Registrar Camper   |
     --------------------------------------
"""
    print(titulo)
    with open("data\Campers.json", "r") as file:
        data = json.load(file)

    edad = int(input("Cuantos años tiene el camper? -> "))
    data.update({input("Ingrese el numero de identificacion del camper -> "):{
        "nombre" : input("Ingrese el nombre del camper -> ").upper(),
        "apellido" : input("Ingrese el apellido del camper -> ").upper(),
        "direccion" : input("Ingrese la direccion del camper -> ").upper(),
        "edad" : edad,
        "estado": "PRE-INSCRITO",
        "contacto" : {
            input("- Va a ingresar un fijo o celular? -> ").upper() : int(input("Ingrese el numero de contacto -> "))
        },
        "acudiente" :  {
            'nombre' : f"{input('Ingrese nombre del tutor -> ') if(edad<18) else 'NOAPLICA'}",
            'cedula' : f"{int(input('Ingrese cedula del tutor -> ')) if(edad<18) else 'NOAPLICA'}"
        }
    }})

    with open("data\Campers.json", "w") as file:
        json.dump(data, file, indent = 4)

def read(codigo = None):
    os.system("cls")
    with open("data/Campers.json", "r") as file:
        data = json.load(file)
    titulo = """
     ------------------------
    |   Busqueda De Campers  |
     ------------------------
""" 
    if(codigo == None):
        os.system("cls")
        print(titulo)
        for key, value in data.items():
            print(f"""
        -----------------------------
        Identificacion : {key}
        Nombre : {value.get("nombre")}
        Apellido : {value.get("apellido")}
        Direccion : {value.get("direccion")}
        Edad : {value.get("edad")}
        Estado : {value.get("estado")}
        Contacto {value.get("contacto")}
        Acudiente : {value.get("acudiente")["nombre"]}, Cedula acudiente : {value.get("acudiente")["cedula"]}
    """)
        os.system("pause")
    else:
        input(f"""
        -----------------------------
        Identificacion : {codigo}
        Nombre : {data[codigo].get("nombre")}
        Apellido : {data[codigo].get("apellido")}
        Direccion : {data[codigo].get("direccion")}
        Edad : {data[codigo].get("edad")}
        Estado : {data[codigo].get("estado")}
        Contacto {data[codigo].get("contacto")}
        Acudiente : {data[codigo].get("acudiente")["nombre"]}, Cedula acudiente : {data[codigo].get("acudiente")["cedula"]}
    """)
def update(): # add the system to change the contact and to change the accudient, check the print error
    os.system("cls")
    while True:
        print("""
     -------------------------
    |   Actualizar un camper  |
     -------------------------
    """)
        read()
        tarjeta = input("Ingrese la identificacion del camper que desea modificar -> ")
        read(tarjeta)
        print("""
    ¿Esta seguro que desea actualizar al camper?
            1. Si
            2. No
            3.Cancelar
    """)
        opc = int(input("Ingrese la opcion correspondiente -> "))
        match(opc):
            case 1:
                with open("data\Campers.json", "r") as file:
                    data = json.load(file)
                actu = input("Que desea actualizar del camper? -> ").lower()
                if (actu == "edad"):
                    data[tarjeta][actu] = int(input("ingrese la nueva informacion -> "))
                else:
                    data[tarjeta][actu] = input("ingrese la nueva informacion -> ").upper()
                with open("data\Campers.json", "w") as file:
                    json.dump(data, file, indent = 4)
                os.system("cls")
                input("Camper modificado exitosamente... ")
                read(tarjeta)
                break
            case 3:
                break
def delete():
    pass
def menu():
    titulo = """
     -----------------------------------
    |   Bienvenido Al Menu De Camper    |
     -----------------------------------
"""
    opciones = "1. Inscribir un camper\n2. Buscar un camper\n3. Modificar informacion de un camper\n4. Eliminar un camper\n5. Volver"
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
                    print("volviendo al menu principal...")
                    os.system("pause")
                    break
                case _:
                    print("- Ingrese una opcion de las disponibles")
                    os.system("pause")
        except ValueError:
            print("- Ingrese un dato valido")
            os.system("pause")
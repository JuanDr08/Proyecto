import os, json
with open("data\Campers.json", "r") as file:
    data = json.load(file)
def create():
    print("""
     --------------------------------------
    |   Formulario Para Registrar Camper   |
     --------------------------------------
""")
    identi = input("Ingrese el numero de identificacion del camper -> ")
    nombre = input("Ingrese el nombre del camper -> ").upper()
    apellido = input("Ingrese el apellido del camper -> ").upper()
    direccion = input("Ingrese la direccion del camper -> ").upper()
    if(identi == "" or nombre == "" or apellido == "" or direccion == "" or identi == " " or nombre == " " or apellido == " " or direccion == " "):
        os.system("cls")
        input("No puede registrar cadenas vacias, ingrese caracteres porfavor")
    else:
        edad = int(input("Cuantos años tiene el camper? -> "))
        data.update({identi :{
            "nombre" : nombre,
            "apellido" : apellido,
            "direccion" : direccion,
            "edad" : edad,
            "estado": "PRE-INSCRITO",
            "contacto" : {
                input("- Va a ingresar un fijo o celular? -> ").upper() : int(input("Ingrese el numero de contacto -> "))
            },
            "acudiente" :  {
                'nombre' : f"{input('Ingrese nombre del tutor -> ') if(edad<18) else 'NOAPLICA'}",
                'cedula' : f"{input('Ingrese cedula del tutor -> ') if(edad<18) else 'NOAPLICA'}"
            }
        }})

        with open("data\Campers.json", "w") as file:
            json.dump(data, file, indent = 4)
            file.close()

def read(codigo = None):
    global data
    if(len(data) >= 1):
        if(codigo == None):
            print("""
        ------------------------
        |   Busqueda De Campers  |
        ------------------------
    """ )
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
            print(f"""
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
    else:
        input("No hay campers registrados para poder buscar")
def update(): # add the system to change the contact and to change the accudient, check the print error
    global data
    if (len(data) >= 1):
        while True:
            os.system("cls")
            read()
            tarjeta = input("Ingrese la identificacion del camper que desea modificar -> ")
            if (tarjeta not in data):
                os.system("cls")
                input("La identificacion ingresada no se encuentra registrada, porfavor ingrese una valida")
            else:
                os.system("cls")
                print("""
            -------------------------
            |   Actualizar un camper  |
            -------------------------
            """)
                read(tarjeta)
                print("""
        ¿Esta seguro que desea actualizar al camper?
                1. Si
                2. No
                3.Cancelar
            """)
                try:
                    opc = int(input("Ingrese la opcion correspondiente -> "))
                    match(opc):
                        case 1:
                            os.system("cls")
                            actu = input("Que desea actualizar del camper? -> ").lower()
                            if (actu not in data[tarjeta]):
                                os.system("cls")
                                input("La informacion que desea modificar no se encuentra dentro de la informacion del camper, modifique algo que exista...")
                            else:
                                if (actu == "edad"):
                                    data[tarjeta][actu] = int(input("ingrese la nueva informacion -> "))
                                else:
                                    data[tarjeta][actu] = input("ingrese la nueva informacion -> ").upper()
                                with open("data\Campers.json", "w") as file:
                                    json.dump(data, file, indent = 4)
                                os.system("cls")
                                read(tarjeta)
                                input("Camper modificado exitosamente... ")
                                break
                        case 3:
                            os.system("cls")
                            input("Volviendo...")
                            break
                except ValueError:
                    os.system("cls")
                    input("Ingrese una opcion valida...")
    else:
        input("No hay campers registrados para poder buscar")
def delete():
    global data
    if (len(data) >= 1):
        while True:
            os.system("cls")
            read()
            tarjeta = input("Ingrese la identificacion del camper que desea eliminar -> ")
            if (tarjeta not in data):
                os.system("cls")
                input("La identificacion del camper que desea eliminar no se encuentra dentro de los registros, elimine algo que exista...")
            else:
                os.system("cls")
                print("""
            -----------------------
            |   Eliminar un camper  |
            -----------------------
            """)
                read(tarjeta)
                print("""
        ¿Esta seguro que desea actualizar al camper?
                1. Si
                2. No
                3.Cancelar
            """)
                try:
                    opc = int(input("Ingrese la opcion correspondiente -> "))
                    match(opc):
                        case 1:
                            data.pop(tarjeta)
                            with open("data\Campers.json", "w") as file:
                                json.dump(data, file, indent = 4)
                            os.system("cls")
                            input("Camper eliminado exitosamente... ")
                            break
                        case 3:
                            os.system("cls")
                            input("Volviendo...")
                            break
                except ValueError:
                    os.system("cls")
                    input("Ingrese una opcion valida...")
    else:
        input("No hay campers registrados para poder buscar")
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
                    input("volviendo al menu principal...")
                    break
                case _:
                    input("- Ingrese una opcion de las disponibles")
        except ValueError:
            input("- Ingrese un dato valido")
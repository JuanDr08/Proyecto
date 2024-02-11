import os, json
def create():
    with open("data\Trainers.json", "r") as file:
        data = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        dato = json.load(file)
    print("""
     --------------------------------------
    |   Formulario Para Registrar Trainer  |
     --------------------------------------
""")
    identi = input("Ingrese el numero de identificacion del trainer (Tenga en cuenta que luego no se podra modificar) -> ")
    nombre = input("Ingrese nombre completo del trainer -> ")
    if (identi == "" or identi == " " or nombre == "" or nombre == " "):
        os.system("cls")
        input("No puede crear trainers con valores vacios o espacios, porfavor digite caracteres")
    elif(identi in data):
        os.system("cls")
        input("Esa identificacion ya existe, ingrese una diferente")
    else:
        data.update({identi : {
            "nombre" : nombre.upper(),
            "horario" : {
                value : "VACIO" for key, value in dato.get("horarios").items()
            }
        }})
        with open("data\Trainers.json", "w") as file:
            json.dump(data, file, indent = 4)
            file.close()
def read(codigo = None):
    with open("data\Trainers.json", "r") as file:
        data = json.load(file)
    if(len(data) >= 1):
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
            print(f"""
        -----------------------------
        Identificacion : {codigo}
        Nombre Completo : {data[codigo].get("nombre")}
    """)
    else:
        input("No hay trainers registrados para realizar esta accion...")    
def update():
    with open("data\Trainers.json", "r") as file:
        data = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        admin = json.load(file)
    if (len(data) >= 1): 
        while True:
            os.system("cls")
            read()
            tarjeta = input("Ingrese la identificacion del trainer que desea modificar -> ")
            if (tarjeta not in data):
                os.system("cls")
                input("La identificacion ingresada no existe, porfavor ingrese una existente")
            else:
                os.system("cls")
                print("""
            ------------------------
            |   Actualizar  trainer  |
            ------------------------
        """)
                read(tarjeta)
                print("""
        ¿Esta seguro que desea actualizar al trainer?
        
        Si el trainer esta asignado a una clase entonces
        se actualizara automaticamente el nombre
                      
        1. Si
        2. No
        3.Cancelar
        """)
                try:
                    opc = int(input("Ingrese la opcion correspondiente -> "))
                    match(opc):
                        case 1:
                            os.system("cls")
                            input("Solo puede cambiar el nombre")
                            name = input("Ingrese el cambio de nombre del trainer -> ").upper()
                            if(name == "" or name == " "):
                                os.system("cls")
                                input("No puede cambiar un dato a algo vacio")
                                break
                            else:
                                data[tarjeta]["nombre"] = name
                                if (len(admin["classrooms"]) >= 1):
                                        for key, value in admin["classrooms"].items():
                                            if (tarjeta in value["trainer"]):
                                                value["trainer"][tarjeta] = name
                            with open("data\Trainers.json", "w") as file:
                                json.dump(data, file, indent = 4)
                                file.close()
                            with open("data\Coordinacion.json", "w") as file:
                                json.dump(admin, file, indent = 4)
                                file.close()
                            os.system("cls")
                            read(tarjeta)
                            input("Trainer modificado exitosamente... ")
                            break
                        case 2:
                            pass
                        case 3:
                            os.system("cls")
                            input("Volviendo...")
                            break
                        case _:
                            os.system("cls")
                            input("Opcion no disponible, ingres una de las solicitadas")
                except ValueError:
                    os.system("cls")
                    input("Ingrese una opcion valida...")
    else:
        input("No hay trainers registrados para realizar esta accion")
def delete():
    with open("data\Trainers.json", "r") as file:
        data = json.load(file)
    if(len(data) >= 1):
        while True:
            os.system("cls")
            read()
            tarjeta = input("Ingrese la identificacion del trainer que desea eliminar -> ")
            if (tarjeta not in data):
                os.system("cls")
                input("La identificacion ingresada no se encuentra asociada a ningun trainer, ingrese una disponible")
            else:
                os.system("cls")
                print("""
            ------------------------
            |   Eliminar un trainer  |
            ------------------------
            """)
                read(tarjeta)
                print("""
        ¿Esta seguro que desea eliminar al trainer?
        
        1. Si
        2. No
        3.Cancelar
        """)
                try:
                    opc = int(input("Ingrese la opcion correspondiente -> "))
                    match(opc):
                        case 1:
                            data.pop(tarjeta)
                            with open("data\Trainers.json", "w") as file:
                                json.dump(data, file, indent = 4)
                                file.close()
                            os.system("cls")
                            input("Trainer eliminado exitosamente... ")
                            break
                        case 3:
                            os.system("cls")
                            input("Volviendo...")
                            break
                        case 2:
                            pass
                        case _:
                            os.system("cls")
                            input("Opcion no disponible, ingres una de las solicitadas")
                except ValueError:
                    os.system("cls")
                    input("Ingrese una opcion valida...")
    else:
        input("No hay trainers registrados para realizar esta accion")
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
import os, json
def create():
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
    print("""
     --------------------------------------
    |   Formulario Para Registrar Camper   |
     --------------------------------------
""")
    identi = input("Ingrese el numero de identificacion del camper (Tenga en cuenta que luego no se podra modificar) -> ")
    if(identi in data):
        os.system("cls")
        input("Esa identificacion ya existe, registre una diferente")
    else:
        nombre = input("Ingrese el nombre del camper -> ").upper()
        apellido = input("Ingrese el apellido del camper -> ").upper()
        direccion = input("Ingrese la direccion del camper -> ").upper()
        fijcel = input("- Va a ingresar un fijo o celular? -> ").upper()
        numcel = int(input(f"Ingrese el numero de {fijcel} -> "))
        if(identi == "" or nombre == "" or apellido == "" or direccion == "" or fijcel == "" or fijcel == " " or identi == " " or nombre == " " or apellido == " " or direccion == " "):
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
                    fijcel : numcel
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
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
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
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
    with open("data\Trainers.json", "r") as file:
        trai = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        admin = json.load(file)
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
        
        Se ajustaran los cambios automaticamente a todas
        las areas donde se encuentre la informacion
        modificada del camper
        
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
                            if (actu == "identidad"):
                                os.system("cls")
                                input("No puede modificar la identidad")
                                break
                            elif (actu == "estado"):
                                os.system("cls")
                                input("No puede modificar el estado")
                                break
                            elif(actu == "nombre"):
                                os.system("cls")
                                name = input("Ingrese el nuevo nombre del camper -> ").upper()
                                if (name == "" or name == " "):
                                    os.system("cls")
                                    input("No puede cambiar a nombres vacios")
                                else:
                                    data[tarjeta][actu] = name
                                    if (len(admin["classrooms"]) >= 1):
                                        for key, value in admin["classrooms"].items():
                                            if (len(value["campers"]) >= 1 and tarjeta in value["campers"]):
                                                value["campers"][tarjeta] = name
                                                for key2, value2 in trai.items():
                                                    if(key2 in value["trainer"]):
                                                        value2[key][tarjeta] = name
                            elif(actu == "contacto"):
                                fice = input("- Va a ingresar un fijo o celular? -> ").upper()
                                if (fice == "" or fice == " "):
                                    os.system("cls")
                                    input("No puede registrar un contacto vacio")
                                    break
                                else:
                                    data[tarjeta][actu].clear()
                                    data[tarjeta][actu].update({fice : int(input("Ingrese el numero de contacto -> "))})
                            elif (actu not in data[tarjeta] and actu != "identidad"):
                                os.system("cls")
                                input("La informacion que desea modificar no se encuentra dentro de la informacion del camper, modifique algo que exista...")
                                break
                            elif (actu == "edad"):
                                new = int(input("ingrese la nueva informacion -> "))
                                if(new > data[tarjeta][actu]):
                                    data[tarjeta][actu] = new
                                else:
                                    os.system("cls")
                                    input("No puede disminuir su edad, usted va creciendo y volviedose mas viejo!!!!")
                            else:
                                newInfo = input("ingrese la nueva informacion -> ").upper()
                                if (newInfo == "" or newInfo == " "):
                                    os.system("cls")
                                    input("No puede actualizar cambios en blanco")
                                    break
                                else:
                                    data[tarjeta][actu] = newInfo
                            with open("data\Trainers.json", "w") as file:
                                json.dump(trai, file, indent = 4)
                                file.close()
                            with open("data\Coordinacion.json", "w") as file:
                                json.dump(admin, file, indent = 4)
                                file.close()
                            with open("data\Campers.json", "w") as file:
                                json.dump(data, file, indent = 4)
                                file.close()
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
    with open("data\Campers.json", "r") as file:
        data = json.load(file)
    with open("data\Trainers.json", "r") as file:
        trai = json.load(file)
    with open("data\Coordinacion.json", "r") as file:
        admin = json.load(file)
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
        Al borrar el camper todos sus registros de todos
        los areas seran eliminados, por lo tanto no saldra
        ni en los reportes.
                      
        Desea continuar?
                      
        1. Si
        2. No
        3.Cancelar
            """)
                try:
                    opc = int(input("Ingrese la opcion correspondiente -> "))
                    match(opc):
                        case 1:
                            if(tarjeta in admin["seleccion"]):
                                admin["seleccion"].pop(tarjeta)
                            for key, value in admin["classrooms"].items():
                                if(tarjeta in value["campers"]):
                                    value["campers"].pop(tarjeta)
                                    for llave, valor in trai.items():
                                        if (llave in value["trainer"]):
                                            valor[key].pop(tarjeta)
                            data.pop(tarjeta)
                            with open("data\Campers.json", "w") as file:
                                json.dump(data, file, indent = 4)
                                file.close()
                            with open("data\Trainers.json", "w") as file:
                                json.dump(trai, file, indent = 4)
                                file.close()
                            with open("data\Coordinacion.json", "w") as file:
                                json.dump(admin, file, indent = 4)
                                file.close()
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
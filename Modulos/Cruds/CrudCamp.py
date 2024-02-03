import os, json
def create():
    pass
def read():
    pass
def update():
    pass
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
            opc = int(input("Ingrese la opcion que desea realizar ->"))
            match(opc):
                case 1:
                    create()
                case 2:
                    read()
                case 3:
                    update()
                case 4:
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
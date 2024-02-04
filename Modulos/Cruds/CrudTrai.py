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
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    os.system("cls")
                    input("Volviendo al menu principal...")
                case _:
                    input("Porfavor ingrese una opcion valida")
        except ValueError:
            print("Porfavor ingrese un dato valido...")
            os.system("pause")
import Modulos.Cruds.CrudCamp as camp
import Modulos.Cruds.CrudTrai as trai
import os
def menuCoo():
    pass
def report():
    pass
def menuPrincipal():
    titulo = """
\t\t\t\t  _____           __ _ _           
\t\t\t\t |  __ \         / _(_) |          
\t\t\t\t | |__) |__ _ __| |_ _| | ___  ___ 
\t\t\t\t |  ___/ _ \ '__|  _| | |/ _ \/ __|
\t\t\t\t | |  |  __/ |  | | | | |  __/\__ \ 
\t\t\t\t |_|   \___|_|  |_| |_|_|\___||___/
"""
    opciones = "1. Coordinacion Academica\n2. Registro Trainers\n3. Registro Campers\n4. Reportes"
    while True:
        os.system("cls")
        print(titulo)
        print(opciones)
        try:
            opc = int(input(" Ingrese la opcion que quiere realizar -> "))
            match(opc):
                case 1:
                    menuCoo()
                case 2:
                    trai.menu()
                case 3:
                    camp.menu()
                case 4:
                    report()
                case _:
                    os.system("cls")
                    print("Ingrese una opcion de las disponibles...")
                    os.system("pause")
        except ValueError:
            os.system("cls")
            print("Porfavor ingrese una opcion valida")
            os.system("pause")
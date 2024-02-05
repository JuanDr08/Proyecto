import Modulos.Cruds.CrudCamp as camp
import Modulos.Cruds.CrudTrai as trai
import Modulos.AdminSystem as process
import os
def menuCoo():
    while True:
        os.system("cls")
        print(f"""
    ********************************
    *    Coordinacion Academica    *
    ********************************
""")
        print(f"1. Prueba de admision\n2. Examenes modulo\n3. Crear rutas\n4. Crear salas\n5. Asignar salones\n6. Volver")
        try:
            opc = int(input("Ingrese la opcion que desea  realizar -> "))
            match(opc):
                case 1:
                    os.system("cls")
                    process.selection()
                case 2:
                    os.system("cls")
                    process.pruebas()
                case 3:
                    os.system("cls")
                    process.ruta()
                case 4:
                    os.system("cls")
                    process.rooms()
                case 5:
                    os.system("cls")
                    process.giveroom()
                case 6:
                    os.system("cls")
                    input("Volviendo...")
                    break
                case _:
                    os.system("cls")
                    input("Ingrese una opcion disponble...")
        except ValueError:
            os.system("cls")
            input("Ingrese un dato valido...")
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
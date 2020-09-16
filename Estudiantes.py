"""
****************** TRABAJO SOBRE PYTHON ******************

"""
import os

def presentacion():
    os.system("cls")
    print("****************************************")
    print("|** TRABAJO DE BASE DE DATOS AVANZADA **")
    print("|                                      |")
    print("|          JORGE ACOSTA PERTUZ         |")
    print("|           HECTOR MEJIA BUENO         |")
    print("|          MOISES RAMIREZ MARIN        |")
    print("|                                      |")
    print("|     ING. JAIDER QUINTERO MENDOZA     |")
    print("|               DOCENTE                |")
    print("|                                      |")
    print("|             UNIGUAJIRA               |")
    print("|       FACULTAD DE INGENIERIA         |")
    print("|        PROGRAMA DE SISTEMAS          |")
    print("|        DISTRITO DE RIOHACHA          |")
    print("|                2020                  |")
    print("|______________________________________|")

def menu():
    presentacion()
    os.system("pause")
    os.system("cls")
    while (True):
        print("****************************************")
        print("|************ __ M E N U __ ***********|")
        print("| 1. INGRESAR LOS DATOS DEL ESTUDIANTE |")
        print("| 2. IMPRIMIR LOS DATOS DEL EMPLEADO   |")
        print("| 3. CONSULTAR LOS DATOS DEL EMPLEADO  |")
        print("| 4. SALIR DEL PROGRAMA                |")
        print("|______________________________________|")
        print("")
        opc = int(input("DIGITE LA OPCION QUE DESEA: "))
        if  opc == 1:
            print("INGRESAR DATOS")
            # ingresarDatos()
        elif    opc == 2:
            print("IMPRIMIR DATOS")
            # imprimirDatos()
        elif    opc == 3:
            print("CONSULTAR DATOS")
            # consultarDatos()
        elif    opc == 4:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")

def main():
    menu()

if __name__ == "__main__":
    main()
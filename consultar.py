"""
****************** TRABAJO SOBRE PYTHON ******************
"""
import os
global destudiantes
global testudiantes
global lestudiantes
global destu
destudiantes = {}
testudiantes = ()
lestudiantes = []
destu = {}

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

class Estudiante():
    def __init__(self):
        self.nombre = input("INGRESE EL NOMBRE DEL ESTUDIANTE: ")
        self.nota = float(input("INGRESE LA NOTA DEL ESTUDIANTE: "))
        testudiantes = (self.nombre, self.nota)
        estudia = list(testudiantes)
        lestudiantes.append(estudia)
        for x in range(len(lestudiantes)):
            templeados = lestudiantes[x]
            print(f"ESTUDIANTE {x+1}")
            self.nombre = templeados[0]
            self.nota = templeados[1]
            print(f"ESTUDIANTE {self.nombre}")
            print(f"SU NOTA ES {self.nota}")
            if  (self.nota >= 3 and self.nota <= 5):
                print("APROBO")
            else:
                print("REPPROBO")

    
    def ConsultarEstudiante(self):
        print("****************************************")
        print("|** __ CONSULTAR POR NOMBRE __ **|")
        print("")
        varia = int(len(lestudiantes))
        x = 0
        name = input("INGRESE EL NOMBRE DEL ESTUDIANTE: ")
        while x < varia:
            testudiantes = lestudiantes[x]
            self.nombre = testudiantes[0]
            self.nota = testudiantes[1]
            if self.nombre in name:
                print(f"ESTUDIANTE {self.nombre}")
                print(f"SU NOTA ES {self.nota}")
                if  (self.nota >= 3 and self.nota <= 5):
                    print("APROBO")
                else:
                    print("REPPROBO")
                x += varia
            else:
                print("ESTUDIANTE NO ENCONTRADO")
                x += 1


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
            estudiantes = Estudiante()
        elif    opc == 2:
            print("IMPRIMIR DATOS")
            # impr
        elif    opc == 3:
            print("CONSULTAR DATOS")
            estudiantes.ConsultarEstudiante
        elif    opc == 4:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")

def main():
    menu()

if __name__ == "__main__":
    main()
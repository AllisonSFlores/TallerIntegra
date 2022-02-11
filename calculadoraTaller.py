def calculadoraChiquita():


    while (True):


        print("         Bienvenido          ")
        print("1. Suma")
        print("2. Resta")
        print("3. División")                        ######
        print("4. Multiplicación")                        ######
        print("0. Salir")
        opcionSeleccionada = input("Digite la opcion que desea --->  ")


        if (opcionSeleccionada == '1'):
            print(suma())

        else:
            if (opcionSeleccionada == '2'):
                print(resta())

            else:
                if (opcionSeleccionada =='3'):
                    print(division())

                else:
                    if (opcionSeleccionada=='4'):
                        print(multiplicacion())

                    else:
                        if (opcionSeleccionada=='0'):
                            break

                        else:
                            print("ERROR: OPCION NO VALIDA")
                    

def suma():
    primerNumero = int(input("Introduzca su primer numero: "))
    segundoNumero = int(input("Introduzca su segundo numero: "))
    return primerNumero+segundoNumero

def resta():
    primerNumero = int(input("Introduzca su primer numero: "))
    segundoNumero = int(input("Introduzca su segundo numero: "))
    return primerNumero-segundoNumero

def division():
    primerNumero = int(input("Introduzca su primer numero: "))
    segundoNumero = int(input("Introduzca su segundo numero: "))
    if(segundoNumero==0):
        print("ERROR: No se puede dividir por 0")
    else:
        return primerNumero/segundoNumero


def multiplicacion():
    primerNumero = int(input("Introduzca su primer numero: "))
    segundoNumero = int(input("Introduzca su segundo numero: "))
    return primerNumero*segundoNumero




##################################################################
# Programa Principal
##################################################################
calculadoraChiquita()

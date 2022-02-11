###Taller de GitHub y Python
###Allison, Joctan y Pamela
def calculadoraChiquita():


    while (True):


        print("         Bienvenido          ")
        print("1. Suma")
        print("2. Resta")
        print("3. Division")   
        print("4. Multipliacación")         
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
                        print(multi())

                    else:
                        if (opcionSeleccionada=='0'):
                            print("Gracias, bye")
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
    return round(primerNumero/segundoNumero,0)

def multi():
    primerNumero = int(input("Introduzca su primer numero: "))
    segundoNumero = int(input("Introduzca su segundo numero: "))
    return primerNumero*segundoNumero



##################################################################
# Programa Principal
##################################################################
calculadoraChiquita()

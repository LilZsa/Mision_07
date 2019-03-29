# Autor: Roberto Emmanuel González Muñoz
# Programa que divide y encuentra el número mayor de una lista dada por el usuario.

from tkinter import messagebox


def menu():
    opcion = int(input("_______________________________________\n"
                       "Misión 07. Ciclos While\n"
                       "Autor: Roberto Emmanuel González Muñoz\n"
                       "Matrícula: A01376803\n"
                       "1. Calcular divisiones\n"
                       "2. Encontrar el mayor\n"
                       "3. Salir\n"
                       "Teclea tu opción: \n"
                       "________________________________________\n"))
    return opcion


def dividir(dividendo, divisor):
    cociente = 0
    residuo = 0
    dividendoOriginal = dividendo

    if dividendo < divisor:
        cociente = 0
        residuo = dividendo
        print("%.d / %.d = %.d, sobra %.d" % (dividendo, divisor, cociente, residuo))

    else:
        while divisor <= dividendo:
            cociente += 1
            residuo = dividendo - divisor
            dividendo -= divisor

        print("%.d / %.d = %.d, sobra %.d" % (dividendoOriginal, divisor, cociente, residuo))


def encontrarMayor():
    datos = []
    print("Teclea una serie de números para encontrar el mayor.")
    numero = int(input("Teclea un número [-1 para salir]: "))

    while numero != -1:
        datos.append(numero)
        numero = int(input("Valor [-1 salir]: "))

    if len(datos) > 0:
        print("El mayor es: ", max(datos))

    elif numero == -1:
        print("No hay valor mayor")


def main():

    opcionmenu = menu()
    while opcionmenu != 3:

        if opcionmenu == 1:
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo, divisor)

        elif opcionmenu == 2:
            encontrarMayor()

        else:
            print("ERROR, teclea 1, 2 o 3.")
            messagebox.showerror("Error", "Teclea 1, 2 o 3.")

        opcionmenu = menu()
    print("Gracias por usar este programa, regresa pronto.")


main()

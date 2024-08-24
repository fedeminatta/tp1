# a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo 
# que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a 
# un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for, 
# while).
# BONUS: Luego, codificar una función equivalente que utilice recursividad.


def suma_bucle(numero):
    total = 0
    for i in range(1, numero + 1):
        total += i
    return total

def suma_recursiva(numero):
    if numero <= 0:
        return 0
    else:
        return numero + suma_recursiva(numero - 1)

def main():
    while True:
        entrada = input("Coloca un número entero positivo: ")
        if entrada.isdigit():
            numero = int(entrada)
            if numero > 0:
                break
            else:
                print("ingresa un número entero positivo.")
        else:
            print("ingresa un númmero entero positivo.")

    resultado_bucle = suma_bucle(numero)
    resultado_recursivo = suma_recursiva(numero)

    print(f"Suma usando bucle: {resultado_bucle}")
    print(f"Suma usando recursión: {resultado_recursivo}")

main()

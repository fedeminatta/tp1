"""
b. Escribir un programa que resuelva la secuencia de Fibonacci a pedido del 
usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro 
numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio 
anterior, validado. La función debe encargarse de calcular la secuencia para 
dicho número. A continuación, una descripción matemática de la famosa 
secuencia:
"""


def fibonacci(numero):
    secuencia = [0, 1]
    while secuencia[-1] < numero:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia


numero = int(input("Ingrese un numero: "))
resultado = fibonacci(numero)
print(f"La secuencia de Fibonacci hasta {numero} es: {resultado}")

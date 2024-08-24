 #joako
# Benja punto 1-D)
def listas_diferencia(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    comunes = list(set1.intersection(set2))
    no_comunes = list(set1.symmetric_difference(set2))
    comunes.sort(reverse=True)
    no_comunes.sort()
    print(comunes)
    print(no_comunes)


listas_diferencia(["b", "a", "c"], ["e", "b", "d", "c"])
# listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'x', 'c'])


# Benja punto 1-E)
def numeros_par_impar(entrada):
    numeros = list(map(int, entrada.split(",")))
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero**2)
    print(",".join(map(str, pares)))
    print(",".join(map(str, impares)))


entrada_usuario = input("coloca una lista de números separados por coma: ")
numeros_par_impar(entrada_usuario)


# Fede punto 1-B
def es_abc(palabra):
    palabra = palabra.lower()
    return list(palabra) == sorted(palabra)


palabra = input("Ingrese una palabra: ")

print(es_abc(palabra))



#Mateo punto 1-C
"""Escriba un procedimiento procesar_palabras(entrada) que acepte una
secuencia de palabras separadas por coma, las ordene y las imprima.
Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es: actuas,bien,felicito,que,te"""

def proocesar_palabras(entrada):
    lista= entrada.split(',')
    ordenadas= sorted(lista)
    salida= ','.join(ordenadas)
    print(f"{salida}\n")
    
entrada_usuario= input("\nIngrese una secuencia de palabras separadas por coma: ")
proocesar_palabras(entrada_usuario)

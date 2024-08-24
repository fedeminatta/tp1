
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

listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'x', 'c'])


# Benja punto 1-E)
def numeros_par_impar(entrada):
    numeros = list(map(int, entrada.split(',')))
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero ** 2)
    print(','.join(map(str, pares)))
    print(','.join(map(str, impares)))

entrada_usuario = input("coloca una lista de números separados por coma: ")
numeros_par_impar(entrada_usuario)

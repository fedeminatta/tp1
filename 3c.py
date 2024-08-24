"""Tal como sucede con la lógica proposicional, en Python muchas veces las
expresiones booleanas pueden ser simplificadas manteniendo el valor de
verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
a a and b. A continuación, intente simplificar las siguientes expresiones y
escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
valor de verdad de las expresiones ya simplificadas:

i. (a or b) or (b and c)
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == True or b == False"""

"""
Original (a or b) or (b and c) = Simplificada (a or b) or  c

Original b and c or False = Simplificada b and c

Original a and b or c or (b and a) = Simplificada a and b or c

Original a == True or b == False = Simplificada a or not b"""

def procesar_sentencias(a, b, c):

    expresion1 = (a or b) or c

    expresion2 = b and c

    expresion3 = a and b or c

    expresion4 = a or not b
    
    return expresion1, expresion2, expresion3, expresion4

a = True
b = False
c = True
print(procesar_sentencias(a, b, c))
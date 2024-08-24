import time
from calendar import isleap

from funciones import edad_dias
from funciones import calcular_dias_mes
from funciones import anio_bisiesto


# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = 0

# calcular los dias
for a in range(anio_comienzo, anio_fin):
    if anio_bisiesto(a):
        dias = dias + 366
    else:
        dias = dias + 365

# agregar los días transcurridos en este año
for m in range(1, hora_local.tm_mon):
    dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

# agregar los días transcurridos en este mes
dias = dias + hora_local.tm_mday

# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))


edad_dias(hora_local, anio_comienzo, anio_fin)

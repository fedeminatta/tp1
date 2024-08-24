def edad_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for anio in range(anio_comienzo + 1, anio_fin):
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias += 366  # Año bisiesto
        else:
            dias += 365  # Año no bisiesto

    dias_comienzo = (
        (
            365
            if not (anio_comienzo % 4 == 0 and anio_comienzo % 100 != 0)
            or (anio_comienzo % 400 == 0)
            else 366
        )
        * (hora_local.tm_yday)
        // 365
    )
    dias_fin = (
        (
            365
            if not (anio_fin % 4 == 0 and anio_fin % 100 != 0) or (anio_fin % 400 == 0)
            else 366
        )
        * (hora_local.tm_yday)
        // 365
    )

    dias_totales = dias + dias_comienzo + dias_fin

    print("Dias totales", dias_totales)


# calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2 and anio_bisiesto == True:
        return 29
    elif mes == 2 and anio_bisiesto == False:
        return 28


# calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)

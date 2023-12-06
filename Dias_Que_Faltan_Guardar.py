def dias_que_faltan():
    print('Fecha 1:')
    mes1 = int(input('Numero de mes: '))
    dia1 = int(input('Numero de dia: '))
    
    print('Fecha 2:')
    mes2 = int(input('Numero de mes: '))
    dia2 = int(input('Numero de dia: '))
    
    # Calcular el número de días transcurridos entre las dos fechas
    tiempo = ((mes2 - mes1) * 30) + (dia2 - dia1)
    
    print('')
    print('Los días que hay entre las dos fechas son:', tiempo)

# Llamar a la función para ejecutar el código
dias_que_faltan()


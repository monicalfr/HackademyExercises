def incr_salarial():
    salario = float(input('Ingresa tu salario: '))
    if salario < 15000:
        aumnt_20 = (salario * 20) / 100
        print('Su incremento salarial es de:', aumnt_20)
    elif salario > 15000:
        aumnt_15 = (salario * 15) / 100
        print('Su incremento salarial es de:', aumnt_15)

# Llamar a la función para ejecutar el código
incr_salarial()


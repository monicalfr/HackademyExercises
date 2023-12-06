def factorial_de_numero():
    numero = int(input('Ingresa el número: '))
    if numero < 0:
        print('El número no se puede calcular')
    else:
        x = 1
        factorial = 1
        while x <= numero:
            factorial *= x  # Calculando el factorial
            x += 1
        print('El factorial del número', numero, '=', factorial)

# Llamar a la función para ejecutar el código
factorial_de_numero()


def volumen_esfera():
    radio = float(input('Ingrese el radio de la esfera: '))
    PIR = float(input('Ingrese el valor de Pi: '))

    volumen = (4 / 3) * PIR * (radio ** 3)

    print('El volumen de la esfera es:', volumen)

# Llamar a la función para ejecutar el código
volumen_esfera()


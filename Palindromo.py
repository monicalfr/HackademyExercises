def es_palindromo():
    palabra = input('Ingrese una palabra: ')
    inversa = palabra[::-1]  # Obtiene la versión invertida de la palabra

    if palabra == inversa:
        print('La palabra es palíndromo.')
    else:
        print('La palabra no es palíndromo.')

# Llamar a la función para ejecutar el código
es_palindromo()


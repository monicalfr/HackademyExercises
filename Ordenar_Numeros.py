def ordenar_numeros():
    a, b, c, d, e = map(int, input('Ingrese los 5 valores a, b, c, d, e: ').split())

    while not (a < b and b < c and c < d and d < e):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if c > d:
            c, d = d, c
        if d > e:
            d, e = e, d

    print('Estos son los números ordenados:', a, b, c, d, e)

# Llamar a la función para ejecutar el código
ordenar_numeros()


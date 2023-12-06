def año_bisiesto():
    Año_ev = int(input('Ingresa el año: '))
    
    # Un año bisiesto es aquel que es divisible por 4, excepto si es divisible por 100 pero no por 400.
    if (Año_ev % 4 == 0 and Año_ev % 100 != 0) or (Año_ev % 400 == 0):
        print(Año_ev, "es un año bisiesto.")
    else:
        print(Año_ev, "no es un año bisiesto.")

# Llamamos a la función para ejecutar el código
año_bisiesto()


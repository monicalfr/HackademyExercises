def tiempo_auto():
    dist = float(input('Ingresa la distancia que el auto recorrerá en km: '))
    vel = float(input('Ingresa la velocidad a la que va el auto en km/hr: '))
    
    # Calcular el tiempo: tiempo = distancia / velocidad
    tiempo = dist / vel
    
    print('El tiempo que tomará en recorrer esa distancia, a esa velocidad es de:', tiempo, 'hr')

# Llamar a la función para ejecutar el código
tiempo_auto()


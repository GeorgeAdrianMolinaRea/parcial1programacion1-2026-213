tipo_saque = ["plano", "liftado", "cortado"]
categoria = ["elite", "experto", "avanzado"]
contador_elite_plano = 0
menor_edad = 999
contador_elite = 0
contador_experto = 0
contador_avanzado = 0
acumulador_edad_avanzado = 0
bandera = True
contador_elite_liftado = 0  
contador_elite_cortado = 0
tipo_saque_mas_usado = ""

while bandera:
    nombre_jugador = input("Ingrese el nombre del jugador: ")

    edad = int(input("Ingrese la edad del jugador (no menor a 18): "))
    while edad < 18:
        print("Edad inválida. Intente nuevamente.")
        edad = int(input("Ingrese la edad del jugador (no menor a 18): "))

    puntos = int(input("Ingrese la cantidad de puntos del jugador (número entero positivo, hasta 60): "))
    while puntos < 1 or puntos > 60:
        print("Cantidad de puntos inválida. Intente nuevamente.")
        puntos = int(input("Ingrese la cantidad de puntos del jugador (número entero positivo, hasta 60): "))

    partidos_ganados = int(input("Ingrese el número de partidos ganados por el jugador (número entero positivo, hasta 35): "))
    while partidos_ganados < 0 or partidos_ganados > 35:
        print("Número de partidos ganados inválido. Intente nuevamente.")
        partidos_ganados = int(input("Ingrese el número de partidos ganados por el jugador (número entero positivo, hasta 35): "))

    tipo_saque_jugador = input("Ingrese el tipo de saque del jugador (plano, liftado, cortado): ")
    while tipo_saque_jugador not in tipo_saque:
        print("Tipo de saque inválido. Intente nuevamente.")
        tipo_saque_jugador = input("Ingrese el tipo de saque del jugador (plano, liftado, cortado): ")

    categoria_jugador = input("Ingrese la categoría del jugador (elite, experto, avanzado): ")
    while categoria_jugador not in categoria:
        print("Categoría inválida. Intente nuevamente.")
        categoria_jugador = input("Ingrese la categoría del jugador (elite, experto, avanzado): ")
    
    respuesta = input("¿Desea ingresar otro jugador? (s/n): ")
    print("---------------------------------------------------------------------")
    if respuesta == "n":
        bandera = False

    if categoria_jugador == "elite" and tipo_saque_jugador == "plano" and 19 <= edad <= 25:
        contador_elite_plano += 1

    if puntos > 50:
        if edad < menor_edad:
            menor_edad = edad
            nombre_menor_edad = nombre_jugador
            categoria_menor_edad = categoria_jugador

    match categoria_jugador:
        case "elite":
            contador_elite += 1
            if tipo_saque_jugador == "plano":
                contador_elite_plano += 1
            elif tipo_saque_jugador == "liftado":
                contador_elite_liftado += 1
            elif tipo_saque_jugador == "cortado":
                contador_elite_cortado += 1
        case "experto":
            contador_experto += 1
        case "avanzado":
            contador_avanzado += 1
            acumulador_edad_avanzado += edad
    
    if contador_elite_plano > contador_elite_liftado and contador_elite_plano > contador_elite_cortado:
        tipo_saque_mas_usado = "plano"
    elif contador_elite_liftado > contador_elite_plano and contador_elite_liftado > contador_elite_cortado:
        tipo_saque_mas_usado = "liftado"
    elif contador_elite_cortado > contador_elite_plano and contador_elite_cortado > contador_elite_liftado:
        tipo_saque_mas_usado = "cortado"
    
total_jugadores = contador_elite + contador_experto + contador_avanzado

porcentaje_experto = (contador_experto / total_jugadores) * 100

if acumulador_edad_avanzado > 0:
    promedio_edad_avanzado = acumulador_edad_avanzado / contador_avanzado

print(f"Cantidad de jugadores de la categoría 'elite' con tipo de saque 'plano' y edad entre 19 y 25 años: {contador_elite_plano}")
print(f"Nombre y Categoría del jugador de menor edad con más de 50 puntos: {nombre_menor_edad}, {categoria_menor_edad}")
print(f"Porcentaje de jugadores de categoría 'experto': {porcentaje_experto}%")
print(f"Promedio de edad de jugadores de categoría 'avanzado': {promedio_edad_avanzado}")
print(f"Tipo de saque más usado por los jugadores de categoría 'elite': {tipo_saque_mas_usado}")

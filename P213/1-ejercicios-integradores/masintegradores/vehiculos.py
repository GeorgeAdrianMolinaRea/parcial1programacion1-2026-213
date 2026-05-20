bandera = True
tipo_vehiculos = ["auto", "camioneta", "moto"]
formas_pago = ["efectivo", "tarjeta", "transferencia"]
cliente_frecuente = ["si", "no"]
kilometros_recorridos_acumulados = 0
total_bruto = 0
total_final = 0
contador_auto = 0
contador_camioneta = 0
contador_moto = 0
kilometros_auto = 0
kilometros_camioneta = 0
kilometros_moto = 0
contador_tarjeta = 0

clientes = []
dias_cliente = []
cliente_mas_dias = ""
max_dias_cliente = 0
alquiler_mayor_monto = 0
cliente_alquiler_mayor = ""
cantidad_alquileres = 0

while bandera:
    nombre_cliente = input("Ingrese el nombre del cliente: ")

    tipo_vehiculo = input("Ingrese el tipo de vehículo (auto, camioneta, moto): ")
    while tipo_vehiculo not in tipo_vehiculos:
        print("Tipo de vehículo inválido. Intente nuevamente.")
        tipo_vehiculo = input("Ingrese el tipo de vehículo (auto, camioneta, moto): ")

    dias_alquiler = int(input("Ingrese la cantidad de días de alquiler (entre 1 y 30): "))
    while dias_alquiler < 1 or dias_alquiler > 30:
        print("Cantidad de días inválida. Intente nuevamente.")
        dias_alquiler = int(input("Ingrese la cantidad de días de alquiler (entre 1 y 30): "))

    precio_por_dia = float(input("Ingrese el precio por día (mayor a 0): "))
    while precio_por_dia <= 0:
        print("Precio por día inválido. Intente nuevamente.")
        precio_por_dia = float(input("Ingrese el precio por día (mayor a 0): "))

    kilometros_recorridos = int(input("Ingrese los kilómetros recorridos (entre 0 y 5000): "))
    while kilometros_recorridos < 0 or kilometros_recorridos > 5000:
        print("Kilómetros recorridos inválidos. Intente nuevamente.")
        kilometros_recorridos = int(input("Ingrese los kilómetros recorridos (entre 0 y 5000): "))
    kilometros_recorridos_acumulados += kilometros_recorridos

    forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    while forma_pago not in formas_pago:
        print("Forma de pago inválida. Intente nuevamente.")
        forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")

    cliente_frecuente_input = input("¿El cliente es frecuente? (si/no): ")
    while cliente_frecuente_input not in cliente_frecuente:
        print("Respuesta inválida. Intente nuevamente.")
        cliente_frecuente_input = input("¿El cliente es frecuente? (si/no): ")

    precio_bruto = dias_alquiler * precio_por_dia
    # Descuento del 15% si el cliente es frecuente
    if cliente_frecuente_input == "si":
        precio_total = precio_bruto * 0.85
    else:
        precio_total = precio_bruto

    # Recargo del 20% para camioneta sobre su costo individual
    if tipo_vehiculo == "camioneta":
        precio_total *= 1.20

    total_bruto += precio_total
    cantidad_alquileres += 1

    if tipo_vehiculo == "auto":
        contador_auto += 1
        kilometros_auto += kilometros_recorridos
    elif tipo_vehiculo == "camioneta":
        contador_camioneta += 1
        kilometros_camioneta += kilometros_recorridos
    else:
        contador_moto += 1
        kilometros_moto += kilometros_recorridos

    if forma_pago == "tarjeta":
        contador_tarjeta += 1

    cliente_existente = False
    for i in range(len(clientes)):
        if clientes[i] == nombre_cliente:
            dias_cliente[i] += dias_alquiler
            cliente_existente = True
            if dias_cliente[i] > max_dias_cliente:
                max_dias_cliente = dias_cliente[i]
                cliente_mas_dias = nombre_cliente
            break

    if not cliente_existente:
        clientes.append(nombre_cliente)
        dias_cliente.append(dias_alquiler)
        if dias_alquiler > max_dias_cliente:
            max_dias_cliente = dias_alquiler
            cliente_mas_dias = nombre_cliente

    if precio_total > alquiler_mayor_monto:
        alquiler_mayor_monto = precio_total
        cliente_alquiler_mayor = nombre_cliente

    respuesta = input("¿Desea cargar otro alquiler? (si/no): ")
    while respuesta not in ["si", "no"]:
        print("Respuesta inválida. Intente nuevamente.")
        respuesta = input("¿Desea cargar otro alquiler? (si/no): ")
    if respuesta == "no":
        bandera = False

# Si los kilómetros acumulados superan 20000, se aplica un recargo del 10% sobre el total bruto general
if kilometros_recorridos_acumulados > 20000:
    total_final = total_bruto * 1.10
else:
    total_final = total_bruto

if cantidad_alquileres > 0:
    promedio_kilometros = kilometros_recorridos_acumulados / cantidad_alquileres
else:
    promedio_kilometros = 0

if contador_auto >= contador_camioneta and contador_auto >= contador_moto:
    tipo_mas_alquileres = "auto"
elif contador_camioneta >= contador_auto and contador_camioneta >= contador_moto:
    tipo_mas_alquileres = "camioneta"
else:
    tipo_mas_alquileres = "moto"

if kilometros_auto >= kilometros_camioneta and kilometros_auto >= kilometros_moto:
    tipo_mas_kilometros = "auto"
elif kilometros_camioneta >= kilometros_auto and kilometros_camioneta >= kilometros_moto:
    tipo_mas_kilometros = "camioneta"
else:
    tipo_mas_kilometros = "moto"

print(f"Importe total bruto: {total_bruto}")
print(f"Importe total final: {total_final}")
print(f"Tipo de vehículo con mayor cantidad de alquileres: {tipo_mas_alquileres}")
print(f"Cliente que más días alquiló en total: {cliente_mas_dias}")
print(f"Promedio de kilómetros recorridos: {promedio_kilometros}")
print(f"Tipo de vehículo que acumuló más kilómetros: {tipo_mas_kilometros}")
print(f"Alquileres pagados con tarjeta: {contador_tarjeta}")
print(f"Alquiler de mayor importe: {cliente_alquiler_mayor} por {alquiler_mayor_monto}")

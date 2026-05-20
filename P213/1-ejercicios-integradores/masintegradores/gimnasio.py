bandera = True
tipos_plan = ["mensual", "trimestral", "anual"]
formas_pago = ["efectivo", "tarjeta", "transferencia"]
turnos = ["mañana", "tarde", "noche"]
alumno_nuevo = ["si", "no"]

contador_mensual = 0
contador_trimestral = 0
contador_anual = 0
contador_manana = 0
contador_tarde = 0
contador_noche = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
contador_menores_18 = 0

total_ventas = 0
total_bruto = 0.0
total_final = 0.0
suma_precios = 0.0
precio_mas_caro = 0.0
cliente_precio_mas_caro = ""

while bandera:
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    while nombre_cliente == "":
        print("Nombre inválido. Intente nuevamente.")
        nombre_cliente = input("Ingrese el nombre del cliente: ")

    tipo_plan = input("Ingrese el tipo de plan (mensual, trimestral, anual): ")
    while tipo_plan not in tipos_plan:
        print("Tipo de plan inválido. Intente nuevamente.")
        tipo_plan = input("Ingrese el tipo de plan (mensual, trimestral, anual): ")

    edad = int(input("Ingrese la edad del cliente (entre 12 y 80): "))
    while edad < 12 or edad > 80:
        print("Edad inválida. Intente nuevamente.")
        edad = int(input("Ingrese la edad del cliente (entre 12 y 80): "))

    precio_plan = float(input("Ingrese el precio del plan (mayor a 0): "))
    while precio_plan <= 0:
        print("Precio del plan inválido. Intente nuevamente.")
        precio_plan = float(input("Ingrese el precio del plan (mayor a 0): "))

    forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    while forma_pago not in formas_pago:
        print("Forma de pago inválida. Intente nuevamente.")
        forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")

    turno_elegido = input("Ingrese el turno elegido (mañana, tarde, noche): ")
    while turno_elegido not in turnos:
        print("Turno elegido inválido. Intente nuevamente.")
        turno_elegido = input("Ingrese el turno elegido (mañana, tarde, noche): ")

    alumno_nuevo_input = input("¿Es alumno nuevo? (si/no): ")
    while alumno_nuevo_input not in alumno_nuevo:
        print("Respuesta inválida. Intente nuevamente.")
        alumno_nuevo_input = input("¿Es alumno nuevo? (si/no): ")

    total_ventas += 1
    total_bruto += precio_plan
    suma_precios += precio_plan

    precio_con_descuentos = precio_plan
    if tipo_plan == "anual":
        precio_con_descuentos = precio_con_descuentos * 1.15

    if alumno_nuevo_input == "si":
        precio_con_descuentos = precio_con_descuentos * 0.90

    total_final += precio_con_descuentos

    if tipo_plan == "mensual":
        contador_mensual += 1
    elif tipo_plan == "trimestral":
        contador_trimestral += 1
    else:
        contador_anual += 1

    if turno_elegido == "mañana":
        contador_manana += 1
    elif turno_elegido == "tarde":
        contador_tarde += 1
    else:
        contador_noche += 1

    if forma_pago == "efectivo":
        contador_efectivo += 1
    elif forma_pago == "tarjeta":
        contador_tarjeta += 1
    else:
        contador_transferencia += 1

    if edad < 18:
        contador_menores_18 += 1

    if precio_plan > precio_mas_caro:
        precio_mas_caro = precio_plan
        cliente_precio_mas_caro = nombre_cliente

    continuar = input("¿Desea ingresar otra venta? (si/no): ")
    while continuar not in ["si", "no"]:
        print("Respuesta inválida. Intente nuevamente.")
        continuar = input("¿Desea ingresar otra venta? (si/no): ")
    if continuar == "no":
        bandera = False

if total_ventas > 50:
    total_final = total_final * 0.95

promedio_precios = 0.0
if total_ventas > 0:
    promedio_precios = suma_precios / total_ventas

turno_mas_clientes = "mañana"
if contador_tarde > contador_manana and contador_tarde >= contador_noche:
    turno_mas_clientes = "tarde"
elif contador_noche > contador_manana and contador_noche > contador_tarde:
    turno_mas_clientes = "noche"

forma_pago_mas_utilizada = "efectivo"
if contador_tarjeta > contador_efectivo and contador_tarjeta >= contador_transferencia:
    forma_pago_mas_utilizada = "tarjeta"
elif contador_transferencia > contador_efectivo and contador_transferencia > contador_tarjeta:
    forma_pago_mas_utilizada = "transferencia"

print("\n----- RESULTADOS -----")
print(f"Total bruto sin descuentos/recargos: {total_bruto}")
print(f"Total final con descuentos/recargos: {total_final}")
print(f"Ventas por tipo de plan: mensual={contador_mensual}, trimestral={contador_trimestral}, anual={contador_anual}")
print(f"Turno con más clientes: {turno_mas_clientes}")
print(f"Cliente que pagó el plan más caro: {cliente_precio_mas_caro}")
print(f"Promedio de precios de planes vendidos: {promedio_precios}")
print(f"Forma de pago más utilizada: {forma_pago_mas_utilizada}")
print(f"Clientes menores de 18 años: {contador_menores_18}")
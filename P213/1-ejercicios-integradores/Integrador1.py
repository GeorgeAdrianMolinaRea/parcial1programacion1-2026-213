total_cantidad_unidades = 0
suma_precios_unitarios = 0
importe_bruto_sin_descuentos = 0
importe_final = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
venta_mas_cara_tarjeta = 0

for i in range(25):
    tipo_producto = input("Ingrese el tipo de producto (alimento, limpieza, perfumería): ")
    while tipo_producto not in ["alimento", "limpieza", "perfumería"]:
        print("Tipo de producto inválido. Intente nuevamente.")
        tipo_producto = input("Ingrese el tipo de producto (alimento, limpieza, perfumería): ")

    cantidad_unidades = int(input("Ingrese la cantidad de unidades vendidas (entre 1 y 20): "))
    while cantidad_unidades < 1 or cantidad_unidades > 20:
        print("Cantidad de unidades inválida. Intente nuevamente.")
        cantidad_unidades = int(input("Ingrese la cantidad de unidades vendidas (entre 1 y 20): "))

    precio_unitario = float(input("Ingrese el precio unitario (mayor a 0): "))
    while precio_unitario <= 0:
        print("Precio unitario inválido. Intente nuevamente.")
        precio_unitario = float(input("Ingrese el precio unitario (mayor a 0): "))

    forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    while forma_pago not in ["efectivo", "tarjeta", "transferencia"]:
        print("Forma de pago inválida. Intente nuevamente.")
        forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")

    total_cantidad_unidades += cantidad_unidades
    suma_precios_unitarios += precio_unitario

    importe_venta = cantidad_unidades * precio_unitario
    importe_bruto_sin_descuentos += importe_venta

    if forma_pago == "efectivo":
        importe_venta *= 0.95
        contador_efectivo += 1
    elif forma_pago == "tarjeta":
        contador_tarjeta += 1
        if importe_venta > venta_mas_cara_tarjeta:
            venta_mas_cara_tarjeta = importe_venta
    else:
        contador_transferencia += 1

    importe_final += importe_venta

if total_cantidad_unidades > 400:
    importe_final *= 0.80
elif total_cantidad_unidades > 200:
    importe_final *= 0.90

if contador_efectivo >= contador_tarjeta and contador_efectivo >= contador_transferencia:
    forma_pago_mas_utilizada = "efectivo"
elif contador_tarjeta >= contador_transferencia:
    forma_pago_mas_utilizada = "tarjeta"
else:
    forma_pago_mas_utilizada = "transferencia"

promedio_precio_unitario = suma_precios_unitarios / 25

print(f"Importe total bruto sin descuentos: {importe_bruto_sin_descuentos}")
print(f"Cantidad total de unidades vendidas: {total_cantidad_unidades}")
print(f"Importe total final con descuentos: {importe_final}")
print(f"Venta más cara hecha con tarjeta: {venta_mas_cara_tarjeta}")
print(f"Promedio de precio unitario: {promedio_precio_unitario}")
print(f"Forma de pago más utilizada: {forma_pago_mas_utilizada}")
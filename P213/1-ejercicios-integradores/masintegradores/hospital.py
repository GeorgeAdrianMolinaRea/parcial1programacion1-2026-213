bandera = True
tipo_atenciones = ["urgencia", "control", "cirugía"]
generos = ["F", "M", "NB"]
formas_pago = ["efectivo", "tarjeta", "transferencia"]
obra_social = ["si", "no"]
dias_acumulados = 0
total_bruto = 0
total_final = 0
contador_urgencia = 0
contador_control = 0
contador_cirugia = 0
dias_urgencia = 0
dias_control = 0
dias_cirugia = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
contador_pacientes = 0
suma_costopor_dia = 0
paciente_max_costo = ""
max_costototal = 0
pacientes_mas_10_dias = 0

while bandera:
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente (entre 0 y 100): "))
    while edad < 0 or edad > 100:
        print("Edad inválida. Intente nuevamente.")
        edad = int(input("Ingrese la edad del paciente (entre 0 y 100): "))

    tipo_atencion = input("Ingrese el tipo de atención (urgencia, control, cirugía): ")
    while tipo_atencion not in tipo_atenciones:
        print("Tipo de atención inválido. Intente nuevamente.")
        tipo_atencion = input("Ingrese el tipo de atención (urgencia, control, cirugía): ")

    dias_internado = int(input("Ingrese la cantidad de días internado (entre 1 y 60): "))
    while dias_internado < 1 or dias_internado > 60:
        print("Cantidad de días inválida. Intente nuevamente.")
        dias_internado = int(input("Ingrese la cantidad de días internado (entre 1 y 60): "))
    dias_acumulados += dias_internado

    costo_por_dia = float(input("Ingrese el costo por día (mayor a 0): "))
    while costo_por_dia <= 0:
        print("Costo por día inválido. Intente nuevamente.")
        costo_por_dia = float(input("Ingrese el costo por día (mayor a 0): "))

    sexo = input("Ingrese el sexo del paciente (F, M, NB): ")
    while sexo not in generos:
        print("Sexo inválido. Intente nuevamente.")
        sexo = input("Ingrese el sexo del paciente (F, M, NB): ")

    tiene_obra_social = input("¿El paciente tiene obra social? (si/no): ")
    while tiene_obra_social not in obra_social:
        print("Respuesta inválida. Intente nuevamente.")
        tiene_obra_social = input("¿El paciente tiene obra social? (si/no): ")

    forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    while forma_pago not in formas_pago:
        print("Forma de pago inválida. Intente nuevamente.")
        forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    
    if tiene_obra_social == "si":
        costo_total = dias_internado * costo_por_dia * 0.8
    else:
        costo_total = dias_internado * costo_por_dia

    total_bruto += costo_total
    contador_pacientes += 1
    suma_costopor_dia += costo_por_dia
    if dias_internado > 10:
        pacientes_mas_10_dias += 1

    match tipo_atencion:
        case "urgencia":
            contador_urgencia += 1
            dias_urgencia += dias_internado
        case "control":
            contador_control += 1
            dias_control += dias_internado
        case "cirugía":
            contador_cirugia += 1
            dias_cirugia += dias_internado

    match forma_pago:
        case "efectivo":
            contador_efectivo += 1
        case "tarjeta":
            contador_tarjeta += 1
        case "transferencia":
            contador_transferencia += 1

    if costo_total > max_costototal:
        max_costototal = costo_total
        paciente_max_costo = nombre

    respuesta = input("¿Desea cargar otro paciente? (si/no): ")
    while respuesta not in ["si", "no"]:
        print("Respuesta inválida. Intente nuevamente.")
        respuesta = input("¿Desea cargar otro paciente? (si/no): ")
    if respuesta == "no":
        bandera = False

if dias_acumulados > 500:
    total_final = total_bruto * 0.9
else:
    total_final = total_bruto

if contador_pacientes > 0:
    promedio_costo_por_dia = suma_costopor_dia / contador_pacientes
else:
    promedio_costo_por_dia = 0

if dias_urgencia >= dias_control and dias_urgencia >= dias_cirugia:
    tipo_mas_dias = "urgencia"
elif dias_control >= dias_urgencia and dias_control >= dias_cirugia:
    tipo_mas_dias = "control"
else:
    tipo_mas_dias = "cirugía"

if contador_efectivo >= contador_tarjeta and contador_efectivo >= contador_transferencia:
    forma_pago_mas_utilizada = "efectivo"
elif contador_tarjeta >= contador_efectivo and contador_tarjeta >= contador_transferencia:
    forma_pago_mas_utilizada = "tarjeta"
else:
    forma_pago_mas_utilizada = "transferencia"

print(f"Total bruto recaudado: {total_bruto}")
print(f"Total final con descuentos aplicados: {total_final}")
print(f"Pacientes por tipo de atención: urgencia={contador_urgencia}, control={contador_control}, cirugía={contador_cirugia}")
print(f"Tipo de atención con más días acumulados: {tipo_mas_dias}")
print(f"Paciente con mayor costo total de internación: {paciente_max_costo}")
print(f"Promedio de costo por día: {promedio_costo_por_dia}")
print(f"Forma de pago más utilizada: {forma_pago_mas_utilizada}")
print(f"Pacientes con más de 10 días de internación: {pacientes_mas_10_dias}")
    
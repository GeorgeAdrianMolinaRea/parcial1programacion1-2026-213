tecnologias = ["IA", "RV/RA", "IOT"]
generos = ["Masculino", "Femenino", "Otro"]
contador_masculino_iot = 0
contador_iot_rvra = 0
mayor_edad_masculino = 0
nombre_mayor_masculino = ""
tecnologia_mayor_masculino = ""

for i in range(4):
    nombre_empleado = input("Ingrese el nombre del empleado: ")

    edad = int(input("Ingrese la edad del empleado (no menor a 18): "))
    while edad < 18:
        print("Edad inválida. Intente nuevamente.")
        edad = int(input("Ingrese la edad del empleado (no menor a 18): "))

    genero = input("Ingrese el genero del empleado (Masculino - Femenino - Otro): ")
    while genero not in generos:
        print("Género inválido. Intente nuevamente.")
        genero = input("Ingrese el genero del empleado (Masculino - Femenino - Otro): ")

    tecnologia = input("Ingrese la tecnología votada (IA, RV/RA, IOT): ")
    while tecnologia not in tecnologias:
        print("Tecnología inválida. Intente nuevamente.")
        tecnologia = input("Ingrese la tecnología votada (IA, RV/RA, IOT): ")
    
    if genero == "Masculino" and tecnologia in ["IOT", "IA"] and 25 <= edad <= 50:
        contador_masculino_iot += 1

    if tecnologia != "IA" and (genero != "Femenino" or 33 <= edad <= 40):
        contador_iot_rvra += 1
    
    if genero == "Masculino" and edad > mayor_edad_masculino:
        nombre_mayor_masculino = nombre_empleado
        tecnologia_mayor_masculino = tecnologia

porcentaje_iot_rvra = (contador_iot_rvra / 10) * 100
print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {contador_masculino_iot}")
print(f"Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje_iot_rvra}%")
print(f"Nombre y tecnología que votó, de los empleados de género masculino con mayor edad: {nombre_mayor_masculino}, {tecnologia_mayor_masculino}")
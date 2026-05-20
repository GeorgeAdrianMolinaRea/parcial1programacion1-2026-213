def mostrar_numero(numero):
    print(f"El número ingresado es: {numero}")

def pedir_numero():
    return int(input("Ingrese un número: "))

def es_par(numero):
    return numero % 2 == 0

def validar_rango(numero, desde, hasta):
    if numero < desde or numero > hasta:
        print(f"El número debe estar entre {desde} y {hasta}.")
    return desde < numero < hasta

def restar1(num1, num2):
    return num1 - num2

def restar2():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1 - num2

def restar3(num1, num2):
    print(f"La resta de {num1} y {num2} es: {num1 - num2}")

def restar4():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"La resta de {num1} y {num2} es: {num1 - num2}")

def realizar_descuento(numero):
    validar_rango(numero, 10, 100)
    return numero * 0.95

def realizar_operacion(num1, num2, operacion):
    validar_rango(num1, 10, 100)
    validar_rango(num2, 10, 100)
    if operacion == 's':
        return num1 + num2
    elif operacion == 'r':
        return num1 - num2
    else:
        print("Operación inválida.")
    
print(realizar_operacion(20, 30, 's'))

print()
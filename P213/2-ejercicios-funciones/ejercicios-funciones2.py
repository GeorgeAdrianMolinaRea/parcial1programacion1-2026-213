
def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    import math
    return math.pi * radio ** 2

def es_par_o_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
        return True
    else:        
        print(f"{numero} es un número impar.")
        return False

def encontrar_maximo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    else:
        print("Error: No se pudo determinar el máximo.")

def calcular_potencia(base, exponente):
    return base ** exponente

def es_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True

print(es_primo(7))  # True
print(es_primo(4)) # False

def mostrar_primos(hasta):
    primos = []
    for n in range(2, hasta + 1):
        if es_primo(n):
            primos.append(n)
    print(f"Los números primos entre 1 y {hasta} son: {primos}")
    return len(primos)

def imprimir_tabla_multiplicar(numero, inicio=1, fin=10):
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")

def pedir_numero_entero():
    while True:
        try:
            return int(input("Ingrese un número entero: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def pedir_numero_flotante():
    while True:
        try:
            return float(input("Ingrese un número flotante: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número flotante.")

def pedir_cadena():
    return input("Ingrese una cadena: ")
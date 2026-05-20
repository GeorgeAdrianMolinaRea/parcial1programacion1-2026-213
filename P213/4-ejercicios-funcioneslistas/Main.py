from ejercicios_funcionesylistas import *
print("Ejercicio 1")
nombres_ingresados = pedir_nombres()
print(nombres_ingresados)

print("\nEjercicio 2")
lista_inicializada = inicializar_lista()
print(lista_inicializada)

print("\nEjercicio 3")
lista_rango = pedir_numeros_rango()
print(lista_rango)

print("\nEjercicio 4")
numero_a_buscar_texto = input("Ingrese un número para buscar en la lista de ejercicio 3: ")
while not numero_a_buscar_texto.isdigit():
    print("Entrada inválida. Ingrese un número entero.")
    numero_a_buscar_texto = input("Ingrese un número para buscar en la lista de ejercicio 3: ")
numero_a_buscar = int(numero_a_buscar_texto)
encontrado = buscar_numero(lista_rango, numero_a_buscar)
print(encontrado)

print("\nEjercicio 5")
menores = obtener_menores(edades_1)
for indice in menores:
    print(f"{nombres_1[indice]} - {edades_1[indice]}")

print("\nEjercicio 6")
nombres_personas = mostrar_nombres_importados()
print(nombres_personas)

menu_usuarios()     
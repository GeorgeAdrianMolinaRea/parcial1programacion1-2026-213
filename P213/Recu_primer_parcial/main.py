from funciones import *

bandera = True
bandera_2 = True
while bandera:
    mostrar_menu()
    opcion = input("Ingrese la opcion una opcion (primero debe importar la lista para poder acceder a otras opciones): ")
    while bandera_2:
        if opcion == "1":
            bandera_2 = False
        else:
            opcion = input("Opcion no valida. Primero debe importar la lista para poder acceder a otras opciones: ")
    match opcion:
        case "1":
            lista_pokemon = importar_lista()
        case "2":
            mostrar_pokemones(lista_pokemon)
        case "3":
            agregar_pokemon(lista_pokemon)
        case "4":
            eliminar_pokemon(lista_pokemon)
        case "5":
            ordenar_pokemones(lista_pokemon)
        case "6": 
            buscar_por_tipo(lista_pokemon, 3, "mayor", "Agua")
        case "7":
            buscar(lista_pokemon, 5, "mayor")
        case "8":
            listar_pokemones_por_region(lista_pokemon)
        case _:
            print("Opcion no valida. Reingrese la opcion del 1 al 8: ")
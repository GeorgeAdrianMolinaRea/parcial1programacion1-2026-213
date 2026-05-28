# Enunciado/s:
# La Liga Pokémon abrió nuevas vacantes para entrenadores e investigadores especializados
# en análisis de datos. Para ingresar al laboratorio principal, los candidatos deberán resolver una serie
# de desafíos de programación.
# El profesor Oak compartió información confidencial de distintos Pokémon registrados en la
# Pokédex. Cada Pokémon posee datos como nombre, tipo, altura, peso, nivel, puntos de ataque y
# región de origen.
# El objetivo será resolver los requerimientos que nos soliciten. Los mejores participantes
# podrán formar parte del equipo oficial de investigación Pokémon.
# Nos pidieron hacer una aplicación con un menú que contenga las siguientes opciones:
# Consignas
# 1) Importar la lista de pokemones del archivo heroes.py
# 2) Listas todos los pokemones de una manera amena para el usuario
# 3) Agregar pokemon a la lista (se le pedirá todas las características de un pokemon al usuario y
# se agregará a la lista original)
# ● nombre y tipo no pueden ser strings vacíos
# ● nivel, peso, altura y fuerza_ataque deben ser mayores a 0
# ● región debe ser “Johto”, “Kanto”, “Sinnoh” o “Hoenn”
# 4) Eliminar pokémon por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista)
# 5) Ordenar la lista de pokémons por nombre (alfabéticamente de la Z a la A)
# 6) Ver héroe más pesado de los de tipo agua (poder ver toda la información de manera amena
# para el usuario sobre el pokémon más pesado dentro de los de tipo agua)
# 7) Ver pokemon con más fuerza de ataque (poder ver toda la información de manera amena
# para el usuario sobre el pokémon más fuerte)
# 8) Listar sólo los pokemones de una región en particular de una manera amena para el usuario
# Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):
# ● Integración de todos los temas vistos en clase hasta el momento del parcial, sin usar librerías
# ni recursos externos
# ● Que todas las opciones funcionen de manera correcta y el código este escrito siguiendo todas
# las buenas prácticas de la programación
# ● Poder defender con lenguaje fluido y técnico el entregable


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("""\n|------------------ Menú de opciones ------------------|\n1) Importar la lista de pokemones del archivo heroes.\n2) Mostrar todos los pokemones.\n3) Agregar un pokemon a la lista.\n4) Eliminar un pokémon por nombre.\n5) Ordenar la lista de pokémons por nombre (alfabeticamente de la Z a la A).\n6) Ver pokemon mas pesado del tipo agua.\n7) Ver pokemon con mas fuerza de ataque.\n8) Mostrar solo los pokemones de una region ingresada por el usuario. 
    """)

def importar_lista():
    """Importa la lista de pokemones del archivo pokemones.py"""

    print("Lista de pokemones importada exitosamente.")
    from pokemones import lista_pokemon
    return lista_pokemon 

def mostrar_pokemones(lista: list):
    """Muestra todos los pokemones de una manera amena para el usuario."""
    print("| Nombre del pokemon |    Tipo    | Altura |  Peso  | Nivel | Fuerza | Region |")
    for pokemon in range(len(lista)):
        print(f"| {lista[pokemon][0]:<18} | {lista[pokemon][1]:<10} | {lista[pokemon][2]:<6} | {lista[pokemon][3]:<6} | {lista[pokemon][4]:<5} | {lista[pokemon][5]:<6} | {lista[pokemon][6]:<6} |")

def validar_numero(dato : str):
    """Valida que el dato ingresado sea un numero y no este vacio."""
    while dato == "":
        dato = input("El dato ingresado esta vacio. Reingrese el dato: ")

    validar = ord(dato[0])
    while validar <= 44 or validar >= 58 or validar == 46 or validar == 47:
        dato = input("El dato no es un numero. Reingrese el dato: ")
        validar = ord(dato[0])
        
    return dato

def validar_tipo(dato: str):
    """Valida que el tipo ingresado sea uno de los tipos de pokemon."""
    lista_tipos = ["Agua", "Fuego", "Planta", "Eléctrico", "Hielo", "Lucha", "Veneno", "Tierra", "Volador", "Psíquico", "Bicho", "Roca", "Fantasma", "Dragón", "Siniestro", "Acero", "Hada"]
    for i in range(len(lista_tipos)):
        if dato == lista_tipos[i]:
            return False
    return True

def agregar_pokemon(lista_pokemon: list):
    """Se le pedirá todas las características de un pokemon al usuario y se agregará a la lista original."""
    pokemon_nuevo = []

    nombre_pokemon = input("Ingrese el nombre: ")
    while nombre_pokemon == "":
        nombre_pokemon = input("El nombre no puede ser vacio. Reingrese el nombre: ")
    pokemon_nuevo.append(nombre_pokemon)
    
    tipo_pokemon = input("Ingrese el tipo: ")
    while validar_tipo(tipo_pokemon):
        tipo_pokemon = input("El tipo no puede ser vacio, o debe ser uno de los siguientes: Agua, Fuego, Planta, Eléctrico,\nHielo, Lucha, Veneno, Tierra, Volador, Psíquico, Bicho, Roca, Fantasma,\nDragón, Siniestro, Acero, Hada.\nReingrese el tipo: ")
    pokemon_nuevo.append(tipo_pokemon)

    nivel_pokemon = int(validar_numero(input("Ingrese el nivel (debe ser un numero mayor a 0): ")))
    while nivel_pokemon <= 0:
        nivel_pokemon = int(validar_numero(input("El nivel debe ser mayor a 0. Reingrese el nivel: ")))
    pokemon_nuevo.append(nivel_pokemon)

    peso_pokemon = float(validar_numero(input("Ingrese el peso (debe ser un numero mayor a 0): ")))
    while peso_pokemon <= 0:    
        peso_pokemon = float(validar_numero(input("El peso debe ser mayor a 0. Reingrese el peso: ")))
    pokemon_nuevo.append(peso_pokemon)

    altura_pokemon = float(validar_numero(input("Ingrese la altura (debe ser un numero mayor a 0): ")))
    while altura_pokemon <= 0:
        altura_pokemon = float(validar_numero(input("La altura debe ser mayor a 0. Reingrese la altura: ")))
    pokemon_nuevo.append(altura_pokemon)

    fuerza_ataque_pokemon = int(validar_numero(input("Ingrese la fuerza de ataque (debe ser un numero mayor a 0): ")))
    while fuerza_ataque_pokemon <= 0:
        fuerza_ataque_pokemon = int(validar_numero(input("La fuerza de ataque debe ser mayor a 0. Reingrese la fuerza de ataque: ")))
    pokemon_nuevo.append(fuerza_ataque_pokemon)

    region_pokemon = input("Ingrese la region (Johto, Kanto, Sinnoh o Hoenn): ")
    while region_pokemon != "Johto" and region_pokemon != "Kanto" and region_pokemon != "Sinnoh" and region_pokemon != "Hoenn":
        region_pokemon = input("La region debe ser Johto, Kanto, Sinnoh o Hoenn. Reingrese la region: ")
    pokemon_nuevo.append(region_pokemon)

    lista_pokemon.append(pokemon_nuevo)

    mostrar_pokemones(lista_pokemon)

def eliminar_pokemon(lista_pokemon: list):
    """El usuario ingresa un nombre y lo intenta eliminar de la lista."""
    existe_pokemon = False
    nombre = input("Ingrese el nombre del pokemon a eliminar: ")
    while nombre == "":
        nombre = input("El nombre no puede ser vacio. Reingrese el nombre del pokemon a eliminar: ")

    for pokemon in range(len(lista_pokemon)):
        if lista_pokemon[pokemon][0] == nombre:
            existe_pokemon = True
            lista_pokemon.pop(pokemon)
            print(f"El pokemon {nombre} ha sido eliminado.")
            break
    if existe_pokemon == False:
        print("El nombre del pokemon ingresado no existe.")   
    

def ordenar_pokemones(lista: list):
    """Ordena la lista de pokemons por nombre (alfabeticamente de la Z a la A)."""
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][0] > lista[j][0]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    mostrar_pokemones(lista)

def buscar(lista: list, indice: int, maximo_minimo: str):
    """Funcion que devuelve el pokemon con el valor maximo del indice pasado por parametro."""
    maximo = 0
    pokemon = []
    print("| Nombre del pokemon |    Tipo    | Altura |  Peso  | Nivel | Fuerza |")
    
    for pokemon in range(len(lista)):
        if maximo_minimo == "mayor":
            if lista[pokemon][indice] > maximo:
                maximo = lista[pokemon][indice]
                pokemon_max = (f"| {lista[pokemon][0]:<18} | {lista[pokemon][1]:<10} | {lista[pokemon][2]:<6} | {lista[pokemon][3]:<6} | {lista[pokemon][4]:<5} | {lista[pokemon][5]:<6} | {lista[pokemon][6]:<6} |")
        elif maximo_minimo == "menor":
            if lista[pokemon][indice] < minimo:
                minimo = lista[pokemon][indice]
                pokemon_max = (f"| {lista[pokemon][0]:<18} | {lista[pokemon][1]:<10} | {lista[pokemon][2]:<6} | {lista[pokemon][3]:<6} | {lista[pokemon][4]:<5} | {lista[pokemon][5]:<6} | {lista[pokemon][6]:<6} |")
    print(pokemon_max)
def buscar_por_tipo(lista: list, indice:int, maximo_minimo:str, tipo: str):
    """Funcion que devuelve el pokemon de un tipo específico con el valor maximo del indice pasado por parametro."""
    maximo = 0
    pokemon = []
    print("| Nombre del pokemon |    Tipo    | Altura |  Peso  | Nivel | Fuerza |")

    for pokemon in range(len(lista)):
        if lista[pokemon][1] == tipo:
            if maximo_minimo == "mayor":
                if lista[pokemon][indice] > maximo:
                    maximo = lista[pokemon][indice]
                    pokemon_max = (f"| {lista[pokemon][0]:<18} | {lista[pokemon][1]:<10} | {lista[pokemon][2]:<6} | {lista[pokemon][3]:<6} | {lista[pokemon][4]:<5} | {lista[pokemon][5]:<6} | {lista[pokemon][6]:<6} |")
            elif maximo_minimo == "menor":
                if lista[pokemon][indice] < minimo:
                    minimo = lista[pokemon][indice]
                    pokemon_max = (f"| {lista[pokemon][0]:<18} | {lista[pokemon][1]:<10} | {lista[pokemon][2]:<6} | {lista[pokemon][3]:<6} | {lista[pokemon][4]:<5} | {lista[pokemon][5]:<6} | {lista[pokemon][6]:<6} |")
    print(pokemon_max)

def listar_pokemones_por_region(lista: list): 
    """Listar sólo los pokemones de una región en particular de una manera amena para el usuario."""
    region = input("Ingrese la region de la que desea listar los pokemones (Johto, Kanto, Sinnoh o Hoenn): ")
    while region != "Johto" and region != "Kanto" and region != "Sinnoh" and region != "Hoenn":
        region = input("La region debe ser Johto, Kanto, Sinnoh o Hoenn. Reingrese la region: ")

    print(f"Pokemones de la region {region}: ")
    print("| Nombre del pokemon |    Tipo    | Altura |  Peso  | Nivel | Fuerza | Region |")
    for pokemon in range(len(lista)):
        if lista[pokemon][6] == region:
            print(f"| {lista[pokemon][0]:<18} | {lista[pokemon][1]:<10} | {lista[pokemon][2]:<6} | {lista[pokemon][3]:<6} | {lista[pokemon][4]:<5} | {lista[pokemon][5]:<6} | {lista[pokemon][6]:<6} |")
'''
referencias de índice
# 0 -> nombre
# 1 -> tipo
# 2 -> altura
# 3 -> peso
# 4 -> nivel
# 5 -> fuera_ataque
# 6 -> region
'''

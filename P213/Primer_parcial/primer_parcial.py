from heroes import lista_heroes

# Enunciado/s:
# Industrias Stark decidió ampliar su departamento de IT y creó un desafío de programación
# para seleccionar candidatos.
# La empresa compartió información confidencial de distintos superhéroes pertenecientes a
# diferentes compañías.
# Cada héroe posee datos como nombre, identidad, altura, peso, género, color de ojos, color de
# pelo, fuerza e inteligencia.
# El objetivo será analizar y procesar esta información utilizando estructuras de datos y
# algoritmos en Python.
# Nos pidieron hacer una aplicación con un menú que contenga las siguientes opciones:
# Consignas
# 1) Importar la lista de heroes del archivo heroes.py
# 2) Listas todos los héroes de una manera amena para el usuario
# 3) Agregar héroe a la lista (se le pedirá todas las características de un héroe al usuario y se
# agregará a la lista original:
# ● nombre e identidad no pueden ser strings vacíos
# ● la empresa debe ser “DC Comics” o “Marvel Comics”
# ● peso, altura y fuerza deben ser mayores a 0
# ● genero M, F, NB
# ● inteligencia debe ser: “low”, “average”, “good”, “high”, “genius”.
# 4) Eliminar héroe por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista)
# 5) Ordenar la lista de héroes por nombre (alfabéticamente de la A a la Z)
# 6) Ver héroe más alto (poder ver toda la información de manera amena para el usuario sobre el
# héroe más alto)
# 7) Ver héroe más fuerte (poder ver toda la información de manera amena para el usuario sobre
# el héroe más fuerte)
# 8) Ver héroe más delgado; menos pesado (poder ver toda la información de manera amena para
# el usuario sobre el héroe menos pesado)

menu = """
1) Listar heroes
2) Agregar heroe
3) Eliminar heroe
4) Ordenar héroes por nombre
5) Ver heroe más alto
6) Ver heroe más fuerte
7) Ver heroe más delgado
8) Salir
"""

def listar_heroes(lista: list):
    print("--------------------------------Listado de heroes--------------------------------")
    for heroe in lista:
        print(f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}")

def agregar_heroe():
    heroe_nuevo = []
    nombre_nuevo = input("Ingrese el nombre del heroe: ")
    while nombre_nuevo == "":
        print("El nombre no puede ser un string vacio. Intente nuevamente.")
        nombre_nuevo = input("Ingrese el nombre del heroe: ")
    
    heroe_nuevo.append(nombre_nuevo)
    
    identidad_nueva = input("Ingrese la identidad del heroe: ")
    while identidad_nueva == "":
        print("La identidad no puede ser un string vacio. Intente nuevamente.")
        identidad_nueva = input("Ingrese la identidad del heroe: ")
    
    heroe_nuevo.append(identidad_nueva)

    empresas_validas = ["DC Comics", "Marvel Comics"]
    empresa_nueva = input("Ingrese la empresa del heroe (DC Comics o Marvel Comics): ")
    while empresa_nueva not in empresas_validas:
        print("La empresa debe ser 'DC Comics' o 'Marvel Comics'. Intente nuevamente.")
        empresa_nueva = input("Ingrese la empresa del heroe (DC Comics o Marvel Comics): ")
    
    heroe_nuevo.append(empresa_nueva)

    altura_nueva = int(input("Ingrese la altura del heroe (en cm): "))
    while altura_nueva <= 0:
        print("La altura debe ser mayor a 0. Intente nuevamente.")
        altura_nueva = int(input("Ingrese la altura del heroe (en cm): "))
    
    heroe_nuevo.append(altura_nueva)

    peso_nuevo = float(input("Ingrese el peso del heroe (en kg): "))
    while peso_nuevo <= 0:
        print("El peso debe ser mayor a 0. Intente nuevamente.")
        peso_nuevo = float(input("Ingrese el peso del heroe (en kg): "))
    
    heroe_nuevo.append(peso_nuevo)

    generos = ["M", "F", "NB"]
    genero_nuevo = input("Ingrese el genero del heroe (M, F, NB): ")
    while genero_nuevo not in generos:
        print("El genero debe ser 'M', 'F' o 'NB'. Intente nuevamente.")
        genero_nuevo = input("Ingrese el genero del heroe (M, F, NB): ")
    
    heroe_nuevo.append(genero_nuevo)

    colores_ojos = ["Azules", "Verdes", "Marrones", "Negros"]
    color_ojos_nuevo = input("Ingrese el color de ojos del heroe: ")
    while color_ojos_nuevo not in colores_ojos:
        print("El color de ojos debe ser uno de los siguientes: Azules, Verdes, Marrones, Negros. Intente nuevamente.")
        color_ojos_nuevo = input("Ingrese el color de ojos del heroe: ")
    
    heroe_nuevo.append(color_ojos_nuevo)

    colores_pelo = ["Rubio", "Castaño", "Negro", "Pelirrojo"]
    color_pelo_nuevo = input("Ingrese el color de pelo del heroe: ")
    while color_pelo_nuevo not in colores_pelo:
        print("El color de pelo debe ser uno de los siguientes: Rubio, Castaño, Negro, Pelirrojo. Intente nuevamente.")
        color_pelo_nuevo = input("Ingrese el color de pelo del heroe: ")
    
    heroe_nuevo.append(color_pelo_nuevo)

    fuerza_nueva = int(input("Ingrese la fuerza del heroe: "))
    while fuerza_nueva <= 0:
        print("La fuerza debe ser mayor a 0. Intente nuevamente.")
        fuerza_nueva = int(input("Ingrese la fuerza del heroe: "))
    
    heroe_nuevo.append(fuerza_nueva)

    inteligencias_validas = ["low", "average", "good", "high", "genius"]
    inteligencia_nueva = input("Ingrese la inteligencia del heroe (low, average, good, high, genius): ")
    while inteligencia_nueva not in inteligencias_validas:
        print("La inteligencia debe ser 'low', 'average', 'good', 'high' o 'genius'. Intente nuevamente.")
        inteligencia_nueva = input("Ingrese la inteligencia del heroe (low, average, good, high, genius): ")
    
    heroe_nuevo.append(inteligencia_nueva)

    if heroe_nuevo not in lista_heroes:
        lista_heroes.append(heroe_nuevo)
        print("Héroe agregado exitosamente.")
    else:
        print("El héroe ya existe en la lista. No se agregó.")
    
    listar_heroes(lista_heroes)

def eliminar_heroe():
    nombre = input("Ingrese el nombre del héroe a eliminar: ")  
    for heroe in lista_heroes:
        if heroe[0] == nombre:
            lista_heroes.pop(lista_heroes.index(heroe)) # Utilizamos el método pop para eliminar el héroe de la lista, y le pasamos como argumento el índice del héroe que queremos eliminar, el cual obtenemos con el método index.
            print("Héroe eliminado exitosamente.")
    print("El héroe no existe en la lista.")
    listar_heroes(lista_heroes)

def ordenar_heroes_por_nombre():
    for i in range(len(lista_heroes)-1): # Recorremos la lista de héroes hasta el penúltimo elemento, esto con el objetivo de comparar cada héroe con los siguientes y evitar comparaciones innecesarias, como que el ultimo numero no sea comparado con nada.
        for j in range(i+1, len(lista_heroes)): # Con el i+1 nos saltamos la comparación del héroe con el mismo, ya que no es necesario comparar un héroe consigo mismo. 
            if lista_heroes[i][0] > lista_heroes[j][0]:
                aux = lista_heroes[i]
                lista_heroes[i] = lista_heroes[j]
                lista_heroes[j] = aux
    print("Héroes ordenados por nombre exitosamente.")

    return lista_heroes

def filtrar(dato: str, mayor_o_menor: str):
    lista_filtrada = []
    maximo = 0
    minimo = 9999
    for heroe in lista_heroes:
        if dato == "altura":
            if mayor_o_menor == "mayor":
                if heroe[3] > maximo:
                    maximo = heroe[3]
                    lista_filtrada = [f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}"]

            elif mayor_o_menor == "menor":
                if heroe[3] < minimo:
                    minimo = heroe[3]
                    lista_filtrada = [f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}"]

        elif dato == "fuerza":
            if mayor_o_menor == "mayor":
                if heroe[8] > maximo:
                    maximo = heroe[8]
                    lista_filtrada = [f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}"]

            elif mayor_o_menor == "menor":
                if heroe[8] < minimo:
                    minimo = heroe[8]
                    lista_filtrada = [f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}"]

        elif dato == "peso":
            if mayor_o_menor == "mayor":
                if heroe[4] > maximo:
                    maximo = heroe[4]
                    lista_filtrada = [f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}"]

            elif mayor_o_menor == "menor":
                if heroe[4] < minimo:
                    minimo = heroe[4]
                    lista_filtrada = [f"Nombre: {heroe[0]}, Identidad: {heroe[1]}, Empresa: {heroe[2]}, Altura: {heroe[3]}, Peso: {heroe[4]}, Genero: {heroe[5]}, Color de ojos: {heroe[6]}, Color de pelo: {heroe[7]}, Fuerza: {heroe[8]}, Inteligencia: {heroe[9]}"]
    
    print(lista_filtrada)

bandera = True

while bandera:
    opcion = input(menu)

    match opcion:
        case "1":
            listar_heroes(lista_heroes)
        case "2":
            agregar_heroe()
        case "3":
            eliminar_heroe()
        case "4":
            listar_heroes(ordenar_heroes_por_nombre())
        case "5":
            filtrar("altura", "mayor")
        case "6":
            filtrar("fuerza", "mayor")
        case "7":
            filtrar("peso", "menor")
        case "8":
            print("Saliendo del programa...")
            bandera = False
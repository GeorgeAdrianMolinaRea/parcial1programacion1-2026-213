from lista_personas import nombres, telefonos, mails, address, postalZip, region, country, edades

def pedir_nombres():
    nombres_nuevo = []
    for i in range(10):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres_nuevo.append(nombre)
    return nombres_nuevo


def inicializar_lista():
    lista_numeros = [0] * 10
    for i in range(10):
        posicion = input(f"Ingrese la posición (0-9) para el número {i+1}: ")
        while not (posicion.isdigit() and 0 <= int(posicion) < 10):
            print("Posición inválida. Debe ser un número entre 0 y 9.")
            posicion = input(f"Ingrese la posición (0-9) para el número {i+1}: ")

        numero = input(f"Ingrese el número a guardar en la posición {posicion}: ")

        lista_numeros[int(posicion)] = int(numero)
    return lista_numeros


def pedir_numeros_rango():
    minimo_texto = input("Ingrese el valor mínimo del rango: ")
    while not minimo_texto.isdigit():
        print("Entrada inválida. Ingrese un número entero.")
        minimo_texto = input("Ingrese el valor mínimo del rango: ")
    minimo = int(minimo_texto)

    maximo_texto = input("Ingrese el valor máximo del rango: ")
    while not maximo_texto.isdigit():
        print("Entrada inválida. Ingrese un número entero.")
        maximo_texto = input("Ingrese el valor máximo del rango: ")
    maximo = int(maximo_texto)

    while maximo < minimo:
        print("El valor máximo debe ser mayor o igual al mínimo.")
        maximo_texto = input("Ingrese el valor máximo del rango: ")
        while not maximo_texto.isdigit():
            print("Entrada inválida. Ingrese un número entero.")
            maximo_texto = input("Ingrese el valor máximo del rango: ")
        maximo = int(maximo_texto)

    lista_numeros = []
    for i in range(10):
        numero_texto = input(f"Ingrese el número {i+1} dentro del rango [{minimo}, {maximo}]: ")
        while not numero_texto.isdigit():
            print("Entrada inválida. Ingrese un número entero.")
            numero_texto = input(f"Ingrese el número {i+1} dentro del rango [{minimo}, {maximo}]: ")
        numero = int(numero_texto)
        while numero < minimo or numero > maximo:
            print("Número fuera de rango. Intente nuevamente.")
            numero_texto = input(f"Ingrese el número {i+1} dentro del rango [{minimo}, {maximo}]: ")
            while not numero_texto.isdigit():
                print("Entrada inválida. Ingrese un número entero.")
                numero_texto = input(f"Ingrese el número {i+1} dentro del rango [{minimo}, {maximo}]: ")
            numero = int(numero_texto)
        lista_numeros.append(numero)
    return lista_numeros

def buscar_numero(lista, numero):
    for valor in lista:
        if valor == numero:
            return True
    return False

nombres_1 = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades_1 = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

def obtener_menores(edades_lista):
    menor = edades_lista[0]
    for edad in edades_lista:
        if edad < menor:
            menor = edad

    indices_menores = []
    for i in range(len(edades_lista)):
        if edades_lista[i] == menor:
            indices_menores.append(i)
    return indices_menores

def mostrar_nombres_importados():
    nombres_importados = []
    for nombre in nombres:
        nombres_importados.append(nombre)
    return nombres_importados

def importar_listas():
    return True


def listar_usuarios_por_pais(pais):
    resultados = []
    for i in range(len(country)):
        if country[i].lower() == pais.lower():
            resultados.append(i)
    return resultados


def listar_datos_mexico():
    indices = listar_usuarios_por_pais("Mexico")
    datos = []
    for i in indices:
        datos.append({
            "nombre": nombres[i],
            "telefono": telefonos[i],
            "mail": mails[i],
            "direccion": address[i],
            "codigo postal": postalZip[i],
            "pais": country[i]
        })
    return datos


def listar_nombre_mail_telefono_brasil():
    indices = listar_usuarios_por_pais("Brazil")
    datos = []
    for i in indices:
        datos.append({
            "nombre": nombres[i],
            "mail": mails[i],
            "telefono": telefonos[i]
        })
    return datos


def usuarios_mas_jovenes():
    edad_menor = edades[0]
    for edad in edades:
        if edad < edad_menor:
            edad_menor = edad

    resultados = []
    for i in range(len(edades)):
        if edades[i] == edad_menor:
            resultados.append({
                "nombre": nombres[i],
                "edad": edades[i],
                "pais": country[i],
                "telefono": telefonos[i],
                "mail": mails[i]
            })
    return resultados


def promedio_edad_usuarios():
    suma_edades = 0
    for edad in edades:
        suma_edades += edad
    return suma_edades / len(edades)


def brasil_mayor_edad():
    indices = listar_usuarios_por_pais("Brazil")
    mayor_edad = edades[indices[0]]
    indice_mayor = indices[0]

    for i in indices:
        if edades[i] > mayor_edad:
            mayor_edad = edades[i]
            indice_mayor = i

    return {
        "nombre": nombres[indice_mayor],
        "edad": edades[indice_mayor],
        "mail": mails[indice_mayor],
        "telefono": telefonos[indice_mayor],
        "codigo postal": postalZip[indice_mayor]
    }


def mexico_brasil_cp_mayor_8000():
    resultados = []
    for i in range(len(country)):
        if (country[i].lower() == "mexico" or country[i].lower() == "brazil") and postalZip[i] > 8000:
            resultados.append({
                "nombre": nombres[i],
                "pais": country[i],
                "codigo postal": postalZip[i],
                "telefono": telefonos[i],
                "mail": mails[i]
            })
    return resultados


def italianos_mayores_40():
    resultados = []
    for i in range(len(country)):
        if country[i].lower() == "italy" and edades[i] > 40:
            resultados.append({
                "nombre": nombres[i],
                "mail": mails[i],
                "telefono": telefonos[i],
                "edad": edades[i]
            })
    return resultados


def menu_usuarios():
    listas_importadas = False
    while True:
        print("\nMenú de opciones de usuarios:")
        print("1 - Importar listas")
        print("2 - Listar los datos de los usuarios de México")
        print("3 - Listar nombre, mail y teléfono de los usuarios de Brasil")
        print("4 - Listar los datos del/los usuario/s más joven/es")
        print("5 - Obtener un promedio de edad de los usuarios")
        print("6 - De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("7 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
        print("9 - Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            listas_importadas = importar_listas()
            print("Listas importadas correctamente.")
        elif opcion == "9":
            break
        elif not listas_importadas:
            print("Primero debe importar las listas con la opción 1.")
        elif opcion == "2":
            datos = listar_datos_mexico()
            print(datos)
        elif opcion == "3":
            datos = listar_nombre_mail_telefono_brasil()
            print(datos)
        elif opcion == "4":
            datos = usuarios_mas_jovenes()
            print(datos)
        elif opcion == "5":
            promedio = promedio_edad_usuarios()
            print(f"Promedio de edad de los usuarios: {promedio}")
        elif opcion == "6":
            datos = brasil_mayor_edad()
            print(datos)
        elif opcion == "7":
            datos = mexico_brasil_cp_mayor_8000()
            print(datos)
        elif opcion == "8":
            datos = italianos_mayores_40()
            print(datos)
        else:
            print("Opción inválida. Intente nuevamente.")

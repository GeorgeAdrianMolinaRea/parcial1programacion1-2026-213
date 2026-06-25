import json
import copy
# Enunciado/s:
# La Corporación Cápsula (Capsule Corp.) abrió una convocatoria para reclutar nuevos analistas de combate que ayuden a estudiar la evolución de los guerreros más poderosos del universo. 
# Bulma recopiló información proveniente de distintos planetas y organizaciones, registrando datos de los principales luchadores conocidos. Cada guerrero posee información sobre su nombre, raza, nivel de poder, planeta de origen, edad, cantidad de transformaciones conocidas y alineación. 
# Los aspirantes deberán desarrollar una aplicación capaz de administrar y analizar estos datos para ayudar en futuras misiones de defensa de la Tierra. Se solicita realizar una aplicación con menú que permita resolver los siguientes requerimientos.
#  Nos pidieron hacer una aplicación con un menú que contenga las siguientes opciones:

# Consignas
#     1) Traer datos desde JSON. Traer los datos del json y guardarlos en una colección
#     2) Listar a los personajes de alguna raza en específico; el usuario ingresará una raza y se mostrarán de manera amena para el usuario
#     3) Modificar personaje de la lista (se le pedirá un nombre al usuario y si existe podrá modificarle algún dato que el usuario quiera) Ejemplo:
#     • personaje a modificar: Goku
#     • característica a modificar: Edad
#     • nuevo valor: 55

#     4) Eliminar personaje por nombre (el usuario ingresa un nombre y lo intenta eliminar de la colección)
#     5) Ordenar la lista de personajes por todos estos criterios:
#     • nombre
#     • raza
#     • edad
# El usuario ingresará alguno de los 3, y por ese criterio se creará UNA COPIA DE LA COLECCIÓN ORIGINAL y se ordenará esa.
#     6) Listar los datos del personaje que más cantidad de técnicas tenga.
#     7) Listar los datos del personaje que más menos cantidad de transformaciones tenga.
#     8) Salir (cuando salga debe guardar en el archivo los cambios hechos durante el programa (modificación o eliminación) para así mantener una persistencia de los cambios)

def mostrar_menu() -> None:
    """Muestra el menú de opciones disponibles al usuario"""
    print("""|----------------------------------------------------------------------------------------------------|
1) Traer datos desde JSON (primero se debe cargar el json para poder usar las otras opciones)
2) Listar personajes de una raza específica
3) Modificar personaje
4) Eliminar personaje
5) Ordenar personajes
6) Listar personaje con más técnicas
7) Listar personaje con menos transformaciones
8) Salir
|----------------------------------------------------------------------------------------------------|
""")
    
def cargar_json() -> list:
    """Carga los datos de personajes desde el archivo JSON"""
    with open("Parcial2/dragon_ball.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_json(datos: list) -> None:
    """Guarda los datos modificados en el archivo JSON"""
    with open("Parcial2/dragon_ball.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def validar_razas(raza: str) -> bool:
    """Valida si la raza ingresada es una de las válidas en la base de datos"""
    razas_validas = ["Saiyajin", "Namekiano", "Humano", "Hibrido", "Mutante", "Bioandroide", "Majin", "Dios de la destruccion"]
    bandera = False
    for i in range(len(razas_validas)):
        if raza == razas_validas[i]:
            bandera = True
            break
    return bandera

def ordenar_datos(datos: list) -> None:
    """Formatea e imprime todos los personajes de manera legible"""
    palabra = ""
    print("|----------------------------------------------------------------------------------------------------|\n")
    for i in range(len(datos)):
            personaje = datos[i]

            for j in personaje:
                if type(personaje[j]) != list:
                    palabra += f"{j}: {personaje[j]}\n"
                elif type(personaje[j]) == list:
                    for n in personaje[j]:
                        palabra += f"{j}: {n}\n"
                    if personaje[j] == []:
                        palabra += f"{j}: No tiene\n"
            palabra += "|----------------------------------------------------------------------------------------------------|\n"
    print(palabra)

def listar_personajes_por_raza(datos: list) -> None:
    """Lista todos los personajes de una raza específica ingresada por el usuario"""
    raza = input("Ingrese la raza que desea listar(Las razas son: Saiyajin, Namekiano, Humano, Hibrido, Mutante, Bioandroide, Majin, Dios de la destruccion): ")
    while not validar_razas(raza):
        raza = input("Raza invalida, reingrese la raza que desea listar(Las razas son: Saiyajin, Namekiano, Humano, Hibrido, Mutante, Bioandroide, Majin, Dios de la destruccion): ")
    print("|----------------------------------------------------------------------------------------------------|\n")
    palabra = ""
    for i in range(len(datos)):
        if datos[i]["raza"] == raza:
            personaje = datos[i]

            for j in personaje:
                if type(personaje[j]) != list:
                    palabra += f"{j}: {personaje[j]}\n"
                elif type(personaje[j]) == list:
                    for n in personaje[j]:
                        palabra += f"{j}: {n}\n"
                    if personaje[j] == []:
                        palabra += f"{j}: No tiene\n"
            palabra += "|----------------------------------------------------------------------------------------------------|\n"
    print(palabra)

def validar_que_sea_letras(dato:str) -> bool:
    """Valida que el dato ingresado contenga solo letras"""
    es_letras = True

    for i in range(len(dato)):
        validar = ord(dato[i])
        if validar < 65 or validar > 122 or (validar > 90 and validar < 97):
            es_letras = False
            break

    return es_letras

def validar_numero(dato : str) -> bool:
    """Valida que el dato ingresado sea un número entero"""
    es_numero = True
    for i in range(len(dato)):
        validar = ord(dato[i])
        if validar <= 44 or validar >= 58 or validar == 46 or validar == 47:
            es_numero = False
            break
    
    return es_numero

def validar_caracteristica(caracteristica: str) -> bool:
    """Valida que la característica ingresada sea uno de los atributos válidos de los personajes"""
    caracteristicas_validas = ["nombre", "raza", "nivel_de_poder", "planeta", "edad", "alineacion","transformaciones", "tecnicas"]
    bandera = False
    for i in range(len(caracteristicas_validas)):
        if caracteristica == caracteristicas_validas[i]:
            bandera = True
            break
    return bandera

def modificar_personaje(datos: list) -> list:
    """Busca un personaje por nombre y modifica el atributo que el usuario especifique"""
    banderavalidacion = False
    caracteristica_encontrada = True
    nombre = input("Ingrese el nombre del personaje que desea modificar: ")
    personaje_encontrado = False
    for i in range(len(datos)):
        if datos[i]["nombre"] == nombre:
            personaje_encontrado = True
            caracteristica = input("Ingrese la caracteristica que desea modificar: ")
            while not validar_caracteristica(caracteristica):
                caracteristica = input("Caracteristica invalida, reingrese la caracteristica que desea modificar: ")
            if caracteristica == "nombre" or caracteristica == "raza" or caracteristica == "planeta" or caracteristica == "alineacion":
                nuevo_valor = input("Ingrese el nuevo valor: ")
                while not validar_que_sea_letras(nuevo_valor):
                    nuevo_valor = input("Valor invalido, reingrese el nuevo valor: ")

            elif caracteristica == "transformaciones" or caracteristica == "tecnicas":
                tecnicas_transformaciones = datos[i][caracteristica]
                print(f"Las opciones a modificar son {tecnicas_transformaciones}.")
                while caracteristica_encontrada:
                    caracteristica_secundaria = input("Ingrese lo que quiere modificar (debe ser algunos de los datos mostrados anteriormente): ")
                    for j in range(len(tecnicas_transformaciones)):
                        if caracteristica_secundaria == tecnicas_transformaciones[j]:
                            nuevo_valor = input("Ingrese el nuevo valor: ")
                            tecnicas_transformaciones[j] = nuevo_valor
                            datos[i][caracteristica] = tecnicas_transformaciones
                            caracteristica_encontrada = False
                            banderavalidacion = True
                            break

            elif caracteristica == "nivel_de_poder" or caracteristica == "edad":
                nuevo_valor = input("Ingrese el nuevo valor: ")
                while not validar_numero(nuevo_valor):
                    nuevo_valor = input("Valor invalido, reingrese el nuevo valor: ")
                nuevo_valor = int(nuevo_valor)
            if banderavalidacion == False:
                datos[i][caracteristica] = nuevo_valor
                break
            
    if not personaje_encontrado:
        print(f"El personaje {nombre} no se encontro en la lista")
    
    return datos

def eliminar_personaje(datos: list) -> list:
    """Elimina un personaje de la lista si existe con el nombre ingresado"""
    nombre = input("Ingrese el nombre del personaje que desea eliminar: ")
    personaje_encontrado = False
    for i in range(len(datos)):
        if datos[i]["nombre"] == nombre:
            personaje_encontrado = True
            print(f"El personaje {nombre} se elimino correctamente")
            datos.pop(i)
            break
            
    if not personaje_encontrado:
        print(f"El personaje {nombre} no se encontro en la lista")
    
    return datos


def ordenar_personajes(datos: list) -> list:
    """Crea una copia de los datos y la ordena según el criterio (nombre, raza o edad)"""
    criterio = input("Ingrese el criterio por el cual desea ordenar la lista(nombre, raza o edad): ")
    while criterio != "nombre" and criterio != "raza" and criterio != "edad":
        criterio = input("Criterio invalido, reingrese el criterio por el cual desea ordenar la lista(nombre, raza o edad): ")
    
    copia_datos = copy.deepcopy(datos)
    for i in range(len(copia_datos)-1):
        for j in range(i+1, len(copia_datos)):
            if copia_datos[i][criterio] > copia_datos[j][criterio]:
                aux = copia_datos[i]
                copia_datos[i] = copia_datos[j]
                copia_datos[j] = aux
    
    return copia_datos


def buscar_personaje(datos: list, max_min: str) -> dict:
    """Busca y retorna el personaje con la máxima o mínima cantidad de técnicas/transformaciones"""
    personaje_encontrado = []
    dato_ingresado = input("Ingrese el dato por el cual desea buscar el personaje(tecnicas, transformaciones): ")
    while dato_ingresado != "tecnicas" and dato_ingresado != "transformaciones":
        dato_ingresado = input("Dato invalido, reingrese el dato por el cual desea buscar el personaje(tecnicas, transformaciones): ")

    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            if max_min == "max":
                if len(datos[i][dato_ingresado]) < len(datos[j][dato_ingresado]):
                    aux = datos[i]
                    datos[i] = datos[j]
                    datos[j] = aux
            elif max_min == "min":
                if len(datos[i][dato_ingresado]) > len(datos[j][dato_ingresado]):
                    aux = datos[i]
                    datos[i] = datos[j]
                    datos[j] = aux
    
    for i in range(len(datos)):
        if len(datos[i][dato_ingresado]) == len(datos[0][dato_ingresado]):
            personaje_encontrado.append(datos[i])
            
    return personaje_encontrado

def menu() -> None:
    """Función principal que ejecuta el menú interactivo con todas las opciones disponibles"""
    bandera = True
    bandera2 = True
    while bandera:
        mostrar_menu()
        opcion = input("Ingrese una opcion del menu: ")
        while bandera2:
            if opcion == "1":
                print("El json se cargo correctamente, ya puede usar las otras opciones del menu")
                datos = cargar_json()
                bandera2 = False
            else:
                opcion = input("Reingrese una opcion del menu (primero debe cargar el json para poder usar las otras opciones): ")
        match opcion:
            case "1":
                datos = cargar_json()
            case "2":
                listar_personajes_por_raza(datos)
            case "3":
                modificar_personaje(datos)
            case "4":
                eliminar_personaje(datos)
            case "5":
                ordenar_datos(ordenar_personajes(datos))
            case "6":
                ordenar_datos(buscar_personaje(datos, "max"))            
            case "7":
                ordenar_datos(buscar_personaje(datos, "min"))
            case "8":
                print("Saliendo del programa, se guardaron los cambios correctamente")
                guardar_json(datos)
                bandera = False
            case _:
                print("Opcion invalida, ingrese una opcion del menu")
        
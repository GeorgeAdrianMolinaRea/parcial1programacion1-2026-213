def contar_vocales(cadena):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    for letra in cadena:
        if letra == "a":
            contador_a += 1
        elif letra == "e":
            contador_e += 1
        elif letra == "i":
            contador_i += 1
        elif letra == "o":
            contador_o += 1
        elif letra == "u":
            contador_u += 1

    resultado = []
    if contador_a > 0:
        resultado.append(["a", contador_a])
    if contador_e > 0:
        resultado.append(["e", contador_e])
    if contador_i > 0:
        resultado.append(["i", contador_i])
    if contador_o > 0:
        resultado.append(["o", contador_o])
    if contador_u > 0:
        resultado.append(["u", contador_u])

    return resultado


def primera_incidencia(cadena, caracter):
    indice = 0
    while indice < len(cadena):
        if cadena[indice] == caracter:
            return indice
        indice += 1
    return -1


def es_palindromo(cadena):
    cadena_minuscula = ""
    posicion = 0
    while posicion < len(cadena):
        letra = cadena[posicion]
        if letra >= "A" and letra <= "Z":
            cadena_minuscula += chr(ord(letra) + 32)
        else:
            cadena_minuscula += letra
        posicion += 1

    cadena_invertida = ""
    posicion = len(cadena_minuscula) - 1
    while posicion >= 0:
        cadena_invertida += cadena_minuscula[posicion]
        posicion -= 1

    return cadena_minuscula == cadena_invertida


def suprimir_repetidos(cadena):
    resultado = ""
    indice = 0
    while indice < len(cadena):
        letra = cadena[indice]
        if letra not in resultado:
            resultado += letra
        indice += 1
    return resultado


def suprimir_vocales(cadena):
    resultado = ""
    indice = 0
    while indice < len(cadena):
        letra = cadena[indice]
        if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and letra != "A" and letra != "E" and letra != "I" and letra != "O" and letra != "U":
            resultado += letra
        indice += 1
    return resultado


def contar_subcadena(cadena, subcadena):
    cantidad = 0
    indice = 0
    while indice <= len(cadena) - len(subcadena):
        encontrado = True
        posicion = 0
        while posicion < len(subcadena):
            if cadena[indice + posicion] != subcadena[posicion]:
                encontrado = False
                break
            posicion += 1
        if encontrado:
            cantidad += 1
        indice += 1
    return cantidad


def contar_letra(letra, cadena):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

print(contar_letra('a', 'banana'))  # Ejemplo de uso

def obtener_subcadena(cadena, inicio, fin):
    if 0 <= inicio < len(cadena) and 0 <= fin <= len(cadena) and inicio < fin:
        return cadena[inicio:fin]
    else:
        return "Posiciones no válidas"

print(obtener_subcadena('Hola Mundo', 0, 4))  # Ejemplo de uso

def char_at(cadena, indice):
    if 0 <= indice < len(cadena):
        return cadena[indice]
    else:
        return "Índice no válido"

print(char_at('Python', 2))  # Ejemplo de uso
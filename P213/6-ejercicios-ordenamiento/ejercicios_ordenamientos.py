["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","CienciasSociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]


def ordenar_nombres_ascendente(nombres, edades):
    nombres_ordenados = []
    edades_ordenadas = []
    for indice in range(len(nombres)):
        nombres_ordenados.append(nombres[indice])
        edades_ordenadas.append(edades[indice])

    n = len(nombres_ordenados)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nombres_ordenados[i] > nombres_ordenados[j]:
                temp_nombre = nombres_ordenados[i]
                nombres_ordenados[i] = nombres_ordenados[j]
                nombres_ordenados[j] = temp_nombre

                temp_edad = edades_ordenadas[i]
                edades_ordenadas[i] = edades_ordenadas[j]
                edades_ordenadas[j] = temp_edad

    return nombres_ordenados, edades_ordenadas


def ordenar_materias_por_nombre_y_puntos(materias, puntos):
    materias_ordenadas = []
    puntos_ordenados = []
    for indice in range(len(materias)):
        materias_ordenadas.append(materias[indice])
        puntos_ordenados.append(puntos[indice])

    n = len(materias_ordenadas)
    for i in range(n - 1):
        for j in range(i + 1, n):
            deberia_intercambiar = False
            if materias_ordenadas[i] > materias_ordenadas[j]:
                deberia_intercambiar = True
            elif materias_ordenadas[i] == materias_ordenadas[j]:
                if puntos_ordenados[i] < puntos_ordenados[j]:
                    deberia_intercambiar = True

            if deberia_intercambiar:
                temp_materia = materias_ordenadas[i]
                materias_ordenadas[i] = materias_ordenadas[j]
                materias_ordenadas[j] = temp_materia

                temp_punto = puntos_ordenados[i]
                puntos_ordenados[i] = puntos_ordenados[j]
                puntos_ordenados[j] = temp_punto

    return materias_ordenadas, puntos_ordenados


def ordenar_estudiantes_por_apellido_nombre_nota(estudiantes, apellidos, notas):
    estudiantes_ordenados = []
    apellidos_ordenados = []
    notas_ordenadas = []
    for indice in range(len(estudiantes)):
        estudiantes_ordenados.append(estudiantes[indice])
        apellidos_ordenados.append(apellidos[indice])
        notas_ordenadas.append(notas[indice])

    n = len(estudiantes_ordenados)
    for i in range(n - 1):
        for j in range(i + 1, n):
            cambiar = False
            if apellidos_ordenados[i] > apellidos_ordenados[j]:
                cambiar = True
            elif apellidos_ordenados[i] == apellidos_ordenados[j]:
                if estudiantes_ordenados[i] > estudiantes_ordenados[j]:
                    cambiar = True
                elif estudiantes_ordenados[i] == estudiantes_ordenados[j]:
                    if notas_ordenadas[i] < notas_ordenadas[j]:
                        cambiar = True

            if cambiar:
                temp_est = estudiantes_ordenados[i]
                estudiantes_ordenados[i] = estudiantes_ordenados[j]
                estudiantes_ordenados[j] = temp_est

                temp_ape = apellidos_ordenados[i]
                apellidos_ordenados[i] = apellidos_ordenados[j]
                apellidos_ordenados[j] = temp_ape

                temp_nota = notas_ordenadas[i]
                notas_ordenadas[i] = notas_ordenadas[j]
                notas_ordenadas[j] = temp_nota

    return estudiantes_ordenados, apellidos_ordenados, notas_ordenadas


def listar_usuarios_pais_ordenados_por_nombre(nombres, paises, edades, codigos, pais_buscado):
    nombres_sel = []
    paises_sel = []
    edades_sel = []
    codigos_sel = []
    for idx in range(len(nombres)):
        if paises[idx] == pais_buscado:
            nombres_sel.append(nombres[idx])
            paises_sel.append(paises[idx])
            edades_sel.append(edades[idx])
            codigos_sel.append(codigos[idx])

    n = len(nombres_sel)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nombres_sel[i] > nombres_sel[j]:
                temp_nombre = nombres_sel[i]
                nombres_sel[i] = nombres_sel[j]
                nombres_sel[j] = temp_nombre

                temp_pais = paises_sel[i]
                paises_sel[i] = paises_sel[j]
                paises_sel[j] = temp_pais

                temp_edad = edades_sel[i]
                edades_sel[i] = edades_sel[j]
                edades_sel[j] = temp_edad

                temp_codigo = codigos_sel[i]
                codigos_sel[i] = codigos_sel[j]
                codigos_sel[j] = temp_codigo

    return nombres_sel, paises_sel, edades_sel, codigos_sel


def listar_usuarios_mas_jovenes(nombres, paises, edades, codigos):
    if len(edades) == 0:
        return [], [], [], []

    min_edad = edades[0]
    for idx in range(1, len(edades)):
        if edades[idx] < min_edad:
            min_edad = edades[idx]

    nombres_sel = []
    paises_sel = []
    edades_sel = []
    codigos_sel = []
    for idx in range(len(edades)):
        if edades[idx] == min_edad:
            nombres_sel.append(nombres[idx])
            paises_sel.append(paises[idx])
            edades_sel.append(edades[idx])
            codigos_sel.append(codigos[idx])

    n = len(nombres_sel)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nombres_sel[i] > nombres_sel[j]:
                temp_nombre = nombres_sel[i]
                nombres_sel[i] = nombres_sel[j]
                nombres_sel[j] = temp_nombre

                temp_pais = paises_sel[i]
                paises_sel[i] = paises_sel[j]
                paises_sel[j] = temp_pais

                temp_edad = edades_sel[i]
                edades_sel[i] = edades_sel[j]
                edades_sel[j] = temp_edad

                temp_codigo = codigos_sel[i]
                codigos_sel[i] = codigos_sel[j]
                codigos_sel[j] = temp_codigo

    return nombres_sel, paises_sel, edades_sel, codigos_sel


def listar_usuarios_mexico_brasil_cp_8000(nombres, paises, edades, codigos):
    nombres_sel = []
    paises_sel = []
    edades_sel = []
    codigos_sel = []
    for idx in range(len(nombres)):
        if (paises[idx] == "Mexico" or paises[idx] == "Brasil") and codigos[idx] > 8000:
            nombres_sel.append(nombres[idx])
            paises_sel.append(paises[idx])
            edades_sel.append(edades[idx])
            codigos_sel.append(codigos[idx])

    n = len(nombres_sel)
    for i in range(n - 1):
        for j in range(i + 1, n):
            cambiar = False
            if nombres_sel[i] < nombres_sel[j]:
                cambiar = True
            elif nombres_sel[i] == nombres_sel[j]:
                if edades_sel[i] < edades_sel[j]:
                    cambiar = True

            if cambiar:
                temp_nombre = nombres_sel[i]
                nombres_sel[i] = nombres_sel[j]
                nombres_sel[j] = temp_nombre

                temp_pais = paises_sel[i]
                paises_sel[i] = paises_sel[j]
                paises_sel[j] = temp_pais

                temp_edad = edades_sel[i]
                edades_sel[i] = edades_sel[j]
                edades_sel[j] = temp_edad

                temp_codigo = codigos_sel[i]
                codigos_sel[i] = codigos_sel[j]
                codigos_sel[j] = temp_codigo

    return nombres_sel, paises_sel, edades_sel, codigos_sel

def imprimir_registros(nombres, listas):
    for indice in range(len(nombres)):
        linea = nombres[indice]
        for columna in range(len(listas)):
            linea = linea + " - " + str(listas[columna][indice])
        print(linea)

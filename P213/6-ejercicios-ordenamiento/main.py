from ejercicios_ordenamientos import *

nombres1 = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades1 = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
nombres_ordenados, edades_ordenadas = ordenar_nombres_ascendente(nombres1, edades1)
print("Ejercicio 1:")
imprimir_registros(nombres_ordenados, [edades_ordenadas])
print()

materias = ["Matematica","Investigacion Operativa","Ingles","Literatura","CienciasSociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
materias_ordenadas, puntos_ordenados = ordenar_materias_por_nombre_y_puntos(materias, puntos)
print("Ejercicio 2:")
imprimir_registros(materias_ordenadas, [puntos_ordenados])
print()

estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
notas = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
estudiantes_ordenados, apellidos_ordenados, notas_ordenadas = ordenar_estudiantes_por_apellido_nombre_nota(estudiantes, apellidos, notas)
print("Ejercicio 3:")
imprimir_registros(apellidos_ordenados, [estudiantes_ordenados, notas_ordenadas])
print()

nombres_usuarios = ["Diego", "Ana", "Carla", "Bruno", "Marta", "Pedro", "Sofia", "Lucas"]
paises_usuarios = ["Mexico", "Brasil", "Mexico", "Chile", "Brasil", "Argentina", "Mexico", "Brasil"]
edades_usuarios = [28, 22, 19, 35, 22, 40, 19, 21]
codigos_usuarios = [8500, 9001, 7900, 8120, 8300, 7700, 8450, 8050]

print("Ejercicio 4 - Opción 1:")
nombres_sel, paises_sel, edades_sel, codigos_sel = listar_usuarios_pais_ordenados_por_nombre(
    nombres_usuarios, paises_usuarios, edades_usuarios, codigos_usuarios, "Mexico")
imprimir_registros(nombres_sel, [paises_sel, edades_sel, codigos_sel])
print()

print("Ejercicio 4 - Opción 2:")
nombres_sel, paises_sel, edades_sel, codigos_sel = listar_usuarios_mas_jovenes(
    nombres_usuarios, paises_usuarios, edades_usuarios, codigos_usuarios)
imprimir_registros(nombres_sel, [paises_sel, edades_sel, codigos_sel])
print()

print("Ejercicio 4 - Opción 3:")
nombres_sel, paises_sel, edades_sel, codigos_sel = listar_usuarios_mexico_brasil_cp_8000(
    nombres_usuarios, paises_usuarios, edades_usuarios, codigos_usuarios)
imprimir_registros(nombres_sel, [paises_sel, edades_sel, codigos_sel])
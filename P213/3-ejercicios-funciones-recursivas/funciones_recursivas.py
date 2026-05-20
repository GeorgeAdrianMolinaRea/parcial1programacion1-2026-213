def suma_naturales(n):
	n = int(n)
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return n + suma_naturales(n - 1)


def potencia(base, exponente):
	base = float(base)
	exponente = int(exponente)
	if exponente == 0:
		return 1
	if exponente < 0:
		return 1 / potencia(base, -exponente)
	return base * potencia(base, exponente - 1)


def suma_digitos(numero):
	n = int(numero)
	if n < 0:
		n = -n
	if n < 10:
		return n
	return (n % 10) + suma_digitos(n // 10)


def fibonacci(n):
	n = int(n)
	if n < 0:
		raise ValueError("El índice de Fibonacci no puede ser negativo")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)


def get_int(mensaje, mensaje_error, minimo=None, maximo=None, reintentos=3):
	intentos = reintentos
	while intentos >= 0:
		try:
			valor = int(input(mensaje))
			if minimo is not None and valor < minimo:
				print(mensaje_error)
			elif maximo is not None and valor > maximo:
				print(mensaje_error)
			else:
				return valor
		except ValueError:
			print("Entrada inválida. Por favor, ingrese un número entero.")
		intentos -= 1
	raise ValueError("Número inválido tras varios intentos")




# Decoradores


def mi_decorador(funcion):
	def nueva_funcion():
		print("nueva funcionalidad 1")
		print("nueva funcionalidad 2")
		funcion()
		print("nueva funcionalidad 3")
		print("nueva funcionalidad 4")
	return nueva_funcion

@mi_decorador
def saludo():
	print("buen dia!")
@mi_decorador
def calcular():
	print("el resultado es: ",10+6)


saludo()



calcular()




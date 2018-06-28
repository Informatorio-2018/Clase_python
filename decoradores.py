# Decoradores

def mi_decorador(valido):
	def _mi_decorador(funcion):
		def funcionalida_1():
			print("nueva funcionalidad 1")
		def funcionalida_2():
			print("nueva funcionalidad 2")
		def nueva_funcion(*args):
			if valido:
				funcionalida_1()
			else:
				funcionalida_2()
			funcion(*args)
		return nueva_funcion
	return _mi_decorador

@mi_decorador(valido = True)
def saludo():
	print("buen dia!")


@mi_decorador(valido = False)
def calcular(a,b):
	print("el resultado es: ",a+b)

@mi_decorador(valido = True)
def recalcular(a,b,c,d):
	print("el resultado es: ",a+b+c+d)


saludo()
print()
a=10
b=8
calcular(a,b)
print()

recalcular(a,b,4,3)



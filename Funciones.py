def sumar(*args):
	suma = 0
	for i in args:
		suma = i + suma
	return suma

a = 10
b = 8

print("el resulktado de la suma es:	",sumar(a,b))

c = 2

print("el resulktado de suma es:	",sumar(a,b,c))


def nueva_funcion(**kwargs):
	# print(kwargs)
	print(kwargs.get("nombre","no existe"))
	print(kwargs["edad"])


nueva_funcion(nombre="juan", edad=44)
from abc import *

class Persona(ABC):
	@abstractmethod
	def __init__(self,nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido

class Cliente(Persona):
	"""
	clientes mayorista blabla
	"""
	def __init__(self,nombre,apellido,telefono):
		super().__init__(nombre,apellido)
		self.telefono=telefono

class Empleado(Persona):
	def __init__(self,nombre,apellido,salario):
		super().__init__(nombre,apellido)
		self.salario=salario

if __name__ == "__main__":

	clien = Cliente("pepe","ledesma",5555555)

	emple = Empleado("martina","noseeee",25000)


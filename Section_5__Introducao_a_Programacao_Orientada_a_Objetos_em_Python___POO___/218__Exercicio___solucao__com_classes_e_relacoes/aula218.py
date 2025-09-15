# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
# abstração, polimorfismo, encapsulamento e herança

class Carro:
	def __init__(self, nome):
		self.nome = nome
		self._motor = None
		self._fabricante = None

	@property
	def motor(self):
		return self._motor

	@motor.setter
	def motor(self, valor):
		self._motor = valor

	@property
	def fabricante(self):
		return self._fabricante

	@fabricante.setter
	def fabricante(self, valor):
		self._fabricante = valor

class Fabricante:
	def __init__(self, nome):
		self.nome = nome

class Motor:
	def __init__(self, nome):
		self.nome = nome


volkswagen = Fabricante('Volkswagen')
fiat = Fabricante('Fiat')
ford = Fabricante('Ford')
motor_1_0 = Motor('1.0')
motor_2_0 = Motor('2.0')

fusca = Carro('Fusca')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)

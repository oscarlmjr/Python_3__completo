'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores
padrão. Caso o valor não seja enviado para o parâmetro,
o valor padrão será usado.
Refatorar: editar o seu código.
'''

def soma(x, y, z=0):
	if z:   # 0 or None = falsy
		print(f'{x=} {y=} {z=}', x + y + z)
	else:
		print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)

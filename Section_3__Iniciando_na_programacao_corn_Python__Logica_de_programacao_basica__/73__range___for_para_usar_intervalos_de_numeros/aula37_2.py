"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1) default
"""
texto = 'Python'

for n, letra in enumerate(texto):
	print(n, letra)
for n in enumerate(texto):
	print(n)
for letra in texto:
	print(letra)

# Classes decoradoras (Decorator classes)
class Multiplicar:

	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		print(args, kwargs)
		return 123


@Multiplicar   # decorator
def soma(x, y):
	return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)

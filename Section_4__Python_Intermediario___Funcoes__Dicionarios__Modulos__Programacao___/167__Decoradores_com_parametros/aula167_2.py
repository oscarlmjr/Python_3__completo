# Decoradores com parâmetros
def decoradora(func):
    print(func.__name__, type(func))

    def aninhada(*args):
        print(func.__name__, type(func), *args, type(args))
        res = func(*args)
        return res + 10
    return aninhada

def blablabla(a, b, c):
    print(a, b, c)
    return decoradora

@blablabla(1, 2, 3)
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)

print(dez_mais_cinco)

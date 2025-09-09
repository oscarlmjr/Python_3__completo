

def parametros_decorador(nome):
    print(nome, type(nome))
    def decorador(func):
        print(func.__name__, type(func), nome, type(nome))

        def sua_nova_funcao(*args):
            res = func(*args)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

############################
 
# def decoradora(nome):    
#     print(nome, type(nome))
#     def decorador(func):
#         print(func.__name__, type(func), nome, type(nome))       
#         def aninhada(*args):
#             print(func.__name__, *args)
#             res = func(*args)
#             return res
#         return aninhada
#     return decorador

# @decoradora(nome='primeiro')
# def soma(x, y):
#     return x + y

# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)

############################

# def decoradora(func):    
#     print(func.__name__, type(func))
#     def aninhada(*args):
#         print(func.__name__, type(func), *args, type(args))       
#         res = func(*args)
#         return res
#     return aninhada

# @decoradora
# def soma(x, y):
#     return x + y

# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)

############################

# def func():
#     variavel = 'variável'
#     print('a')
#     # return variavel


# a = func()
# func()
# print(a)
# print()
# print(func())
# print(a)

############################

# def variaveis(x, a=0, b=0):
#   a, b = b, x
#   if a == 0:
#     a = b
#   elif a != b:
#     return soma(a, b)
#   print(a, b)

# def multiplicacao(a, b):
#   print(f'{a} * {b} = {a * b}')
  
    
# def soma(a, b):
  
#     print(f'{a} + {b} = {a + b}')
#     return multiplicacao(a, b)  

# lista = [5, 2]

# for x in lista:
#   variaveis(x)

############################

# def soma(x):
#   yield 1
#   y = x
#   yield f'x + y = {x + y}'

# def multiplicacao(x):
#   yield from soma(x)
#   y = x
#   yield f'x * y = {x * y}'


# lista = [5, 2]
# iterator = lista._iter_()

# # x, y = lista


# x = next(iterator)
# m = multiplicacao(x)

# for s in m:
#   print(s)

############################

# a = 'a'
# b = 'b'
# c = 'd'

# a, b = b, c
# print(b)

# a = 'a'
# b = 'b'

# for _ in range(3):
#   a, b = b, _
#   print(a)

############################

# a = ''
# b = ''

# def soma(x):
#   a, b = b, x
#   yield 1
#   a, b = b, x
#   yield f'{a} + {b} = {a + b}'

#   def multiplicacao(a, b, x):
#     a, b = b, x
#     yield from soma(x)
#     a, b = b, x
#     yield f'{a} * {b} = {a * b}'

#   return multiplicacao(a, b, x)

# lista = [5, 2]
# iterator = lista._iter_()
# # x, y = lista

# x = next(iterator)
# m = multiplicacao(a, b, x)
# for s in m:
#   print(s)

############################

# def funcao(*args):
#     print(len(args))
#     print(*args)
#     # print(list(*args))   # TypeError: list expected at most 1 argument, got 2
#     print(args)
#     print(list(args))
#     print(list(args)[0])


# funcao(2, 4)



# def c(a, b):
# def c(*args):
# def c():
#     return a + b

# a = 'a'
# b = 'b'

# d = lambda: c(a, b)
# print(d)
# print(d())
# print(c(a, b))
# d = c(a, b)
# print(d)
# print(c())

# def soma(x, y):
#     return x + y
#
# def multiplica(x, y):
#     return x * y
#
# def executa(funcao, *args):
#     def interna(funcao, y):
#         return funcao(*args, y)
#
#     return interna
#
# soma_com_cinco = executa(soma, 5)
# multiplica_por_dez = executa(multiplica, 10)
#
# print(soma_com_cinco(soma, 10))
# print(multiplica_por_dez(multiplica, 10))


# def funcao():  # Mais de 1 parâmetro = var()
#
#     def funcao2(par2):
#
#         print(f"var('par2') -> {par2}")
#         print(f'var == funcao2 = {var == funcao2}')
#         print(f'var == funcao = {var == funcao}\n')
#
#     return funcao2
#
# var = funcao()
# var('par2')


# def funcao():
#
#     def funcao2():
#
#         return f'return funcao2()'
#
#     return funcao2()
#
# var = funcao()
# print(f"var -> {var}")
# print(f"var == funcao() -> {var == funcao()}")
# print(f"var == funcao -> {var == funcao}\n")


# def funcao():
#     def funcao2():
#         print('funcao2')
#
#     return funcao2()
#
# funcao()


# def funcao(par2):
#     print(par2)
#
# def funcao2(par1, par2):
#     return par1(par2)
#
# funcao2(funcao, 'funcao')


# def funcao(par2):
#     return par2
#
# def funcao2(par1, par2):
#     return par1(par2)
#
# def funcao3(par3):
#     print(par3)
#
# funcao2(funcao, funcao3('funcao3'))


# def funcao():
#
#     def funcao2():
#
#         def funcao3():
#             return 'funcao3'
#
#         print(funcao3())
#
#     funcao2()
#
# funcao()

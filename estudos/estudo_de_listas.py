# import copy


lista = [[{'a': {'a': 'a', 'b': 'b', 'c': 'c'}}], []]

print(lista[0][0])
print(lista[0][0]['a'])


###########################

# lista = []

# print(lista is None)
# print(lista is True)
# print(lista is False)
# print(lista == [])
# print([] == [[], []])
# print()
# print(len(lista))
# print(len(lista) is 0)
# print(len(lista) == 0)
# print(len(lista) is None)
# print(len(lista) is True)
# print(len(lista) is False)
# print()

# lista = [[], []]
# lista_2 = [['a'], []]

# print(lista == lista_2)
# print([[], []] == [[], []])
# print(len(lista))
# print(len(lista) is 0)
# print(len(lista) == 0)
# print(len(lista) is None)
# print(len(lista) is True)
# print(len(lista) is False)
# print()


# lista.extend('a', 'b', 'c')   # TypeError: list.extend() takes exactly one argument (3 given)

# lista_2 = ['a', 'b', 'c']
# lista.extend(*lista_2)   #	# TypeError: list.extend() takes exactly one argument (3 given)

# lista.extend(lista_2)   # ['a', 'b', 'c']
# lista = []
# lista = [lista_2]   # [['a', 'b', 'c']]
# lista = []

# lista = [*lista_2]   # ['a', 'b', 'c']
# print(lista)


###########################

# a = ['a']
# b = ['b']
# c = []
# # c.append(a, b)   # TypeError: list.append() takes exactly one argument (2 given)
# c = [a, b]
# print(c)

###########################

# lista = ['a', 'b', 'c']   # TypeError: 'str' object is not callable

# def a():
#	 print('a', type(a))   # a <class 'function'>

# def b():
#	 print('b')

# def c():
#	 print('c')

# lista = [a, b, c]
# for l in lista:
#	 l()
#	 print(l, type(l))	

###########################

# lista = ['a', 'b']


# for i in enumerate(lista):
#	 print(i)

# for i, n in enumerate(lista):
#	 print(i, n)


###########################

# lista = ['a', 'b']

# print(*lista)
# x, y = lista

# print(x, y)

###########################

# lista = ['a', 'b', 'c', 'd']
# print(len(lista))

# del lista[1]
# print(lista)

# for n, p in enumerate(lista, 1):
#	 print(n, type(n), p, type(p))

# for n in enumerate(lista, 1):
#	 print(n)

###########################

# a = None
# b = 'c'
# lista = []
# lista.append(a)
# print(lista)
# lista.append(b)
# print(lista)


# lista = []   # IndexError: list index out of range
# print(len(lista))
# lista1 = []
#
# # lista1.append(lista[0])
# print(lista1)


# lista = [1, 2, 3, 4, 5]
# a = []
# a.append(lista[0])
# print(a)
# a.pop(0)
# print(a)
# lista = [1, 2, 3, 4, 5]
# print(lista[:-2])
# print(*lista[:-2])
# print(lista[-1])
# # print(lista.pop())   # print(lista.pop()) executa
# lista.pop(0)
# print(*lista, sep='\n')

# from functools import partial


# def printer_iter(iterator):
#	 print(*list(iterator), sep='\n')
#	 print()
#
# produtos = [
#	 {'nome': 'Produto 5', 'preco': 10.00},
#	 {'nome': 'Produto 1', 'preco': 22.32},
#	 {'nome': 'Produto 3', 'preco': 10.11},
#	 {'nome': 'Produto 2', 'preco': 105.87},
#	 {'nome': 'Produto 4', 'preco': 69.90},
# ]
#
# def aumentar_porcentagem(valor, porcentagem):
#	 return round(valor * porcentagem, 2)
#
# aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)
#
# novos_produtos = []
# for p in produtos:
#	 novos_produtos.append({**p, 'preco': aumentar_dez_porcento(p['preco'])})


# novos_produtos = [
#	 {**p, 'preco': aumentar_dez_porcento(p['preco'])}
#	 for p in produtos
# ]
#
# printer_iter(produtos)
# printer_iter(novos_produtos)

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
#
# print(max(l1, l2))   # fatia e retorna a lista com mais caracteres
# print(max(len(l1), len(l2)))
# print(min(l1, l2))
# print(min(len(l1), len(l2)), '\n')
#
# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = [1.6, 2.2, 3.1, 4.5]
#
# print(max(l1, l2))
# print(max(len(l1), len(l2)))
# print(min(l1, l2))
# print(min(len(l1), len(l2)), '\n')


# def funcao_max(l1, l2):
#	 return min(l1, l2)
#
#
# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
#
# print(funcao_max(l1, l2))


# lista = [3, 4]
# print(*lista)
# print(tuple(lista))


# def funcao(x):
#	 return x
#
# def executa(funcao, *args):
#	 return funcao(*args)
#
#
# lista = [3]
# print(executa(funcao,*lista))


# lista = [{'nome': 'Produto 5', 'preco': 10.00}]
# print(lista)
# print([lista[0]['nome']])

# lista = ['a', 'b', 'c', 'l']
# lista2 = copy.deepcopy(lista)
# print(lista.pop())
# print(lista)
# lista.pop()
# print(lista)
# print(lista2)

# lista = list()
# lista = ['a', 'b', 'c']
# lista.remove('a')
# print(lista)

# lista_acao = ''
# lista = []
# acao = 'casa'
# acao2 = ''
# refazer = []

# lista_acao += acao
# print(f'lista_acao = {lista_acao}')
# refazer.extend(lista_acao[-1])
# print(f'refazer = {refazer}')
# print()
# lista += acao
# print(f'lista = {lista}')
#

# lista_acao = []
# lista = []
# acao = 'casa'
# acao2 = ''
# refazer = []
#
# lista_acao += [acao]
# print(f'lista_acao = {lista_acao}')
# refazer.extend(lista_acao[-1])
# print(f'refazer = {refazer}')
# print()
# lista += acao
# print(f'lista = {lista}')

# l = ['a', 'b', 'c']
# l = l[:-1]
# print(l)

# l = ['a', 'b', 'c']
# print(l[:-1])
# m = ['d', 'e', 'f']
# print(l + m)

# a = 'a'
# b = 'b'
# c = a + b
# # print(c, len(c))
# d = [c]
# # d = list(c)
# print(*d)
# print([c])
# print(list(c))
# d = []
# d += a
# print(d)

# lista = ['a', 'b', 'c', 'l']
# lista = []
# print(len(lista))
# print(lista)

# def func(*args):
#	 args = list(args)
#	 print(args)
#	 print(*args)
# func('12345')
#
# def func(*args):
#	 args = (args)
#	 print(args)
#	 print(*args)
# func('12345')

# t1 = [1, 2, 3, 4, 5]
# t1 = print(*t1)
# print(t1)

# t1 = 1, 2, 3, 4, 5
# t1 = list(t1)
# print(t1)
#
# t1 = 1, 2, 3, 4, 5
# t1 = [t1]
# print(t1)
#
# t1 = (1, 2, 3, 4, 5)
# t1 = list(t1)
# print(t1)
# t1 = tuple(t1)
# print(t1)
#
# t1 = (1, 2, 3, 4, 5)
# t1 = [t1]
# print(t1)
# t1 = tuple(t1)
# print(t1)
#
# t1 = '12345'
# t1 = list(t1)
# print(t1)
#
# t1 = '12345'
# t1 = [t1]
# print(t1)


# a = 1, 2, 3, 4, 5
# a = [1, 2, 3, 4, 5]
# a = '1', '2', '3', '4', '5'
# b = ''
# for n in range(len(a)):
#	 b += str(a[n])
#	 print(b)

# a = '12345'
# a = [a]
# print(f'{a}\n')
#
# a = '1', '2', '3', '4', '5'
# b = '12345'
# print(f'{a}\n{b}')
# print(a == b)
# print(f'{list(a)}\n{list(b)}')
# print(list(a) == list(b))

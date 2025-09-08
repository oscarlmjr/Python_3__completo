import copy


lista_pessoas_2 = [[{
    "Oscar": {
        "nome": "Oscar",
        "idade": 45,
        "tipo_pessoa": "Pessoa Física",
        "numero": 768286,
        "tipo_conta": "Conta Corrente"}}], []]

print(lista_pessoas_2)
print()

# lista_contas = [[{}], []]

lista_pessoas_2[0][0] = {lista_pessoas_2[0][0]['Oscar'].get('numero', 'numero'): lista_pessoas_2[0][0]['Oscar']}
# print({lista_pessoas_2[0][0]['Oscar'].get('numero', 'numero'): lista_pessoas_2[0][0]['Oscar']})

# print(lista_contas)
print()
print(lista_pessoas_2)


############################

# lista_pessoas_2 = {
#     "Oscar": {
#         "nome": "Oscar",
#         "idade": 45,
#         "tipo_pessoa": "Pessoa Física",
#         "numero": 768286,
#         "tipo_conta": "Conta Corrente"}}

# print(lista_pessoas_2)
# print()

# lista_contas = {}

# lista_contas.update({lista_pessoas_2['Oscar'].get('numero', 'numero'): lista_pessoas_2['Oscar']})
# # print({lista['Oscar'].get('numero', 'numero'): lista['Oscar']})

# print(lista_contas)
# print()
# print(lista_pessoas_2)


############################

# lista = {"nome": "Oscar", "idade": 45}
# print(lista)
# print()

# lista.setdefault("tipo_conta", "Conta Corrente")
# print(lista)
# print()

# lista.update(tipo_conta="Conta Corrente")
# print(lista)
# print()


# lista_2 = {
#         "nome": "Oscar",
#         "idade": 45,
#         "tipo_pessoa": "Pessoa Física",
#         "numero": 768286,
#         }

# lista.update(lista_2)
# print(lista)


############################

# class Dicionario():

#     def __init__(self, dicionario):
#         self.dicionario = dicionario

#         print(f'{dicionario.keys()}')
#         print(f'{dicionario.values()}')
#         print(f'{dicionario.items()}')
#         print()
#         print(f'{self.__dict__}')
#         print(f'{self.__dict__.keys()}')
#         print(f'{self.__dict__.values()}')
#         print(f'{self.__dict__.items()}')


# dicionario = {'nome': 'oscar', 'idade': 45}
# dic = Dicionario(dicionario)


############################

# class Dicionario():

#     def __init__(self):
        # dicionario = {'nome': 'oscar', 'idade': 45}
        
#         print(f'{dicionario}')
#         print(f'{dicionario.keys()}')
        # print(f'{dicionario.values()}')
        # print(f'{dicionario.items()}')
        # print()
        # print(f'{self.__dict__}')
        # print(f'{self.__dict__.keys()}')
        # print(f'{self.__dict__.values()}')
        # print(f'{self.__dict__.items()}')


# Dicionario()


############################

# class Dicionario():

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.dicionario = {'nome': self.nome, 'idade': self.idade}

#         print(f'{self.dicionario.keys()}')
#         print(f'{self.dicionario.values()}')
#         print(f'{self.dicionario.items()}')


# nome = 'oscar'
# idade = 45

# dic = Dicionario(nome, idade)


############################

# dicionario = {'nome': 'oscar', 'idade': 45}

# # print(dicionario)
# print(*dicionario.items())
# print()

# dicionario_novo = {}
# dicionario_novo.update(rg=1234, endereco='rua r')

# dicionario.update(dicionario_novo)
# print(dicionario)


############################
# import copy


# lista = [[{'oscar': {'nome': 'oscar', 'idade': 45}}, 
#     {'joão gabriel': {'nome': 'joão gabriel', 'idade': 15}}], 
#     [{'gabriel': {'nome': 'gabriel', 'idade': 15}}]]

# # print(lista)
# # print(lista[0])

# dic = {'rg': 1234, 'endereco': 'rua r'}
# lista_3 = copy.deepcopy(lista)

# nome = 'gabriel'

# c = 0; l = 0
# while True:

#     for dados in lista_3[l]:
#         print(c)
#         if dados.get(nome) is None:
#             c += 1
#         else:
#             dados.get(nome, lista[l][c][nome].update(dic))
#             break
#     l += 1        
#     c = 0
#     if l == len(lista_3):
#         break
        

# print(lista)


############################

# dicionario_novo = {}

# for d in dicionario.items():
#     # print(d, *d)
#     dicionario_novo.setdefault(*d)

# print(dicionario_novo)


############################

# dicionario = {'nome': 'oscar', 'idade': 45}

# print(*dicionario)
# print(dicionario.items())
# print(*dicionario.items())
# print()

# dicionario = {*dicionario.items()}

# print(dicionario)


############################

# lista = [
#     {'oscar': {'nome': 'oscar', 'idade': 45}}, 
#     {'gabriel': {'nome': 'gabriel', 'idade': 15}}
#     ]

# print(lista)
# print(lista[0])
# print(lista[0]['oscar'])
# print(lista[0]['oscar']['nome'])
# print(lista[0].get('oscar', 'oscar'))
# print(lista[1].get('gabriel', 'gabriel'))


############################

# dicionario = {'nome': 'oscar', 'idade': 45}

# print(dicionario.get('oscar', ))
# print(dicionario.get('nome', 'nome'))

# if dicionario.get('nome', 'nome') == 'oscar':
#     print(dicionario['nome'])
#     ...


############################

# dicionario = {'oscar': {'nome': 'oscar', 'idade': 45}}

# print(dicionario.get('oscar', ))
# print(dicionario.get('oscar', 'oscar'))


# lista = [{dicionario.get('nome', 'nome'): dicionario}]

# print(lista)

# print(lista[0]['oscar'])

# print(lista['oscar'])


############################
 
# perguntas = {"nome": "oscar", "sobrenome": "mendes"}

# # print(len(perguntas))
# # print()

# print(perguntas.keys())
# print(*perguntas.keys())
# print(perguntas.values())
# print(*perguntas.values())
# print(perguntas.items())
# print(*perguntas.items())


############################
 

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# print(len(perguntas))

# for n in perguntas[1]['Opções']:
#     print(n)
# print(n for n in perguntas[1]['Opções'])


############################
 

# dicionario = [{"nome": "oscar", "sobrenome": "mendes"}]
# gabriel = {"nome": "gabriel", "sobrenome": "mendes"}

# dicionario.append(gabriel)
# print(dicionario)
# # print(*dicionario)

# for n in dicionario:
#     print(n['nome'])

# print(list(*dicionario))
# print(list(dicionario))


############################
 


# dicionario = {{"nome": "oscar", "sobrenome": "mendes"}}   # TypeError: unhashable type: 'dict'
# dicionario = [{"nome": "oscar", "sobrenome": "mendes"},]
# gabriel = {"nome": "gabriel", "sobrenome": "mendes"}
# print(*gabriel)
# # dicionario = dicionario[gabriel]
# print(*dicionario)
# print(list(*dicionario))
# print(list(dicionario))
# print(dicionario['nome'])

# for n in dicionario:
#     print(n, dicionario[n])


# print(dicionario[0])   # só na dicionario

# print(dicionario.get("nome"))   # só dá get na key
# print(dicionario.get("oscar"), '\n')
#
#
# for n in dicionario.items():
#     print(n)

# dicionario = {
#     {"nome": "oscar", "sobrenome": "mendes"},
#     {"nom": "joão", "sobren": "jose"}
# }   # TypeError: unhashable type: 'dict'
# 
# print(dicionario)

import json

def comeco(lista):
	with open('estudo_de_try.json', 'w', encoding='utf8') as arquivo:
		json.dump(lista, arquivo, ensure_ascii=False, indent=2)
	return lista

try:
	with open('estudo_de_try.json', 'r', encoding='utf8') as arquivo:
		lista = json.load(arquivo)
except FileNotFoundError:
	lista = []
	comeco(lista)

# acao = 'nadar'
# acao = 'sair'
acao = 'correr'
# acao = 'viajar'

lista.append(acao)
variavel = comeco(lista)
print(*variavel, sep='\n')




# try:
#	 with open('estudo_de_try.json', 'r', encoding='utf8') as arquivo:
#		 lista = json.load(arquivo)
# except FileNotFoundError:
#	 lista = []
#	 with open('estudo_de_try.json', 'w', encoding='utf8') as arquivo:
#		 json.dump(lista, arquivo, ensure_ascii=False, indent=2)
#
# acao = 'nada'
# # acao = 'sair'
#
# lista.append(acao)
# print(lista)
# with open('estudo_de_try.json', 'w', encoding='utf8') as arquivo:
#	 json.dump(lista, arquivo, ensure_ascii=False, indent=2)
#	 print(f'LISTA-:', *lista, sep='\n')

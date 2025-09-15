import json, copy


lista = []
lista_1 = []
lista_2 = []
while True:
	letra = input('Digite uma letra: \n')
	lista_1.append(letra)
	lista_2 = copy.deepcopy(lista_1)
	lista_2.append('b')
	lista.append(lista_1)
	lista.append(lista_2)

	with open('est_with.json', 'w+', encoding='utf8') as arquivo:
		json.dump(lista, arquivo, ensure_ascii=False, indent=2)
		print(lista) 
		print(lista[0]) 
		print(lista[1]) 


################

# lista = []
# while True:
#	 letra = input('Digite uma letra: \n')
#	 lista.append(letra)

#	 with open('est_with.json', 'w+', encoding='utf8') as arquivo:
#		 json.dump(lista, arquivo, ensure_ascii=False, indent=2) 
#		 print(lista) 

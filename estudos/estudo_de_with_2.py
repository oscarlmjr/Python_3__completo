import json, copy


try:    
    with open('est_with.json_2.json', 'r+', encoding='utf8') as arquivo:
        lista = json.load(arquivo)
        # lista_1 = lista[0]     
        # lista_2 = lista[1]
        print(lista) 
except:
    lista_1 = []
    lista_2 = []
    lista = [lista_1, lista_2]

    with open('est_with.json_2.json', 'w+', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)    
        # lista_1 = lista[0]     
        # lista_2 = lista[1]
        print(lista) 

while True:

    letra = input('Digite uma letra: \n')

    lista[0].append(letra)
    lista[1] = copy.deepcopy(lista[0])
    lista[1].insert(1, 'b')


    with open('est_with.json_2.json', 'w+', encoding='utf8') as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=2)         
            print(lista)


###############

# with open('est_with.json', 'r+', encoding='utf8') as arquivo:
#     lista = json.load(arquivo)
#     print(lista)    
#     lista.pop(1)
#     print(lista[1])
#     print(lista)    
#     arquivo.seek(0, 0)
#     print(arquivo.read())

# with open('est_with.json', 'w+', encoding='utf8') as arquivo:
#     json.dump(lista, arquivo, ensure_ascii=False, indent=2) 
#     print(lista) 
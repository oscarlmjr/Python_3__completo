

    # p3 = PessoaFisica('Gabriel', 15)
    # p3.lista_pessoa_fisica()

    # p4 = PessoaJuridica('Gaba Game', 37)
    # p4.lista_pessoa_Juridica()

class Pessoa:
    def __init__(self):
        ...

    def lista_tipo_pessoas(self, lista):
        self.lista = lista
        print(self.lista)

class PessoaFisica:
    def __init__(self, nome, idade, tipo_pessoa='Pessoa Física'):
        self.nome = nome
        self.idade = idade
        self.tipo_pessoa = tipo_pessoa
        
    def lista_pessoa_fisica(self):
        lista = self.__dict__
        Pessoa.lista_tipo_pessoas(self, lista)


class PessoaJuridica:    
    def __init__(self, nome, cnpj, tipo_pessoa='Pessoa Jurídica'):
        self.nome = nome
        self.cnpj = cnpj
        self.tipo_pessoa = tipo_pessoa 
        
    def lista_pessoa_Juridica(self):
        lista = self.__dict__
        Pessoa.lista_tipo_pessoas(self, lista)   

while True:

    pessoa_fisica = '1'
    pessoa_juridica = '2'
    tipo_pessoa = input('Tipo de pessoa: \nPessoa Física (1) ou Pessoa Jurídica (2) \n') 

    if tipo_pessoa == '1':
        nome = input('Nome: \n')
        idade = int(input('Idade: \n'))
        pn = PessoaFisica(nome, idade)
        pn.lista_pessoa_fisica()
    else:
        nome = input('Nome: \n')
        cnpj =  int(input('CNPJ: \n'))        
        pn = PessoaJuridica(nome, cnpj)
        pn.lista_pessoa_Juridica()


    # p3 = PessoaFisica('Gabriel', 15)
    # p3.lista_pessoa_fisica()

    # p4 = PessoaJuridica('Gaba Game', 37)
    # p4.lista_pessoa_Juridica()

    




    ...





# while True:

#     for n in range(5):
#         print(n)
#     break


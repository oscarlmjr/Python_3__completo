# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p1.nome = 'EITA'
print(p1.nome)
del p1.nome
# print(p1.nome)   # AttributeError: 'Pessoa' object has no attribute 'nome'
print(p1.idade)

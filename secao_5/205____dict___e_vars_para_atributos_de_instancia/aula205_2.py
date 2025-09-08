# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)

print(p1.__dict__)
print(vars(p1))
p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)
print(p1.outra)

class Pessoa:
    def __init__(self, idade: int) -> None:
        self.idade = idade

    def maior_idade(self):
        return self.idade >= 18

    def adicionar_ano(self):
        self.idade += 1


pessoa = Pessoa(idade=17)
print(pessoa.idade)
print(pessoa.maior_idade())

pessoa.adicionar_ano()

print(pessoa.maior_idade())  # True

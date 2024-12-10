from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dataNascimento(self):
        ano_atual = date.today().year
        ano_nascimento = ano_atual - self.idade
        return ano_nascimento

pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Carlos", 40)

print(pessoa1.dataNascimento())

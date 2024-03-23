class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def _str_(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)
        
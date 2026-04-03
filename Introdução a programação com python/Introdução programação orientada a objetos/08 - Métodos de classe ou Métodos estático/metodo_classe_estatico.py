class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # Método de classe para criar uma instância a partir de uma data de nascimento
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano  # Simulando o cálculo da idade com base no ano de nascimento
        return cls(nome, idade)

    @staticmethod # Método estático para verificar se uma pessoa é maior de idade
    def maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1997, 15, 8, "Bruno")
print(p.nome, p.idade)  # Saída: Bruno 29

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(17))
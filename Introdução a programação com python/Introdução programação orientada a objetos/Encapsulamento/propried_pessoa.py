class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome  # Atributo protegido
        self._ano_nascimento = ano_nascimento  # Atributo protegido


        pass


    @property                   
    def nome(self):
        return self._nome  # Método getter para acessar o nome
    

    @property
    def idade(self): # um bom exemplo de método getter que calcula a idade com base no ano de nascimento usando o @property
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento  # Método getter para calcular a idade com base no ano de nascimento
    

pessoa = Pessoa("Bruno", 1997)
print(f"Nome: {pessoa.nome}\t Idade: {pessoa.idade}")  # Acessando o nome e a idade usando os métodos getters
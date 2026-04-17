class Cachorro:
    def __init__(self, nome, cor, acordado=True): # Método construtor para inicializar os atributos do cachorro
        print("Iniciando a classe cachorro...")

        self.nome = nome  # Atributo para armazenar o nome do cachorro
        self.cor = cor   # Atributo para armazenar a cor do cachorro
        self.acordado = acordado # Atributo para armazenar o estado de acordado do cachorro
        
    def __del__(self): # Método destrutor para realizar ações quando a instância do cachorro for destruída
        print(f"Destruindo a classe cachorro {self.nome}...")

    def latir(self): # Método para simular o latido do cachorro
        if self.acordado:
            print("Au au!")
        else:
            print(f"{self.nome} está dormindo e não pode latir.")




def criar_cachorro():
        c = Cachorro("Rexy", "Preto e Branco")  # Cria uma instância da classe Cachorro com nome "Rex" e cor "Preto e Branco"
        print(c.nome, c.cor)  # Exibe os atributos do cachorro
        c.latir() # Chama o método latir para simular o latido do cachorro

criar_cachorro() # Chama a função para criar o cachorro e exibir seu nome   



class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def ligar_motor(self):
            print("O motor está ligando.")

class motocicleta(Veiculo):
    pass

class carro(Veiculo):
    pass

class caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado): 
        super().__init__(cor, placa, numero_rodas) # super() é usado para chamar o construtor da classe pai (Veiculo) e inicializar os atributos herdados
        self.carregado = carregado   # Atributo específico da classe caminhao para indicar se o caminhão está carregado ou não

    def esta_carregado(self):
         print(f"O caminhão está {'carregado' if self.carregado else 'não carregado'}.")     

    


motocicleta = motocicleta("vermelha", "ABC-1234", 2)



carro = carro("azul", "DEF-5678", 4)



caminhao = caminhao("preto", "GHI-9012", 8, False)


# caminhao.ligar_motor()
# caminhao.esta_carregado()

print(motocicleta)
print(carro)
print(caminhao)

class bicicleta:
    def __init__(self, cor, modelo, ano, valor,): # Método construtor para inicializar os atributos da bicicleta
        self.cor = cor  # Atributo para armazenar a cor da bicicleta
        self.modelo = modelo # Atributo para armazenar o modelo da bicicleta
        self.ano = ano   # Atributo para armazenar o ano da bicicleta
        self.valor = valor # Atributo para armazenar o valor da bicicleta
        

    def buzinar(self): # Método para simular a buzina da bicicleta
        print("plim plim...")
    
    def parar(self): # Método para simular a parada da bicicleta
        print("parando ...")
        print("A bicicleta parou.")
    
    def correr(self): # Método para simular a corrida da bicicleta
        print("Vrummmmm....")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    """ O método __str__ é usado para fornecer uma representação legível da instância da classe bicicleta, 
     mostrando os atributos e seus valores. """

b1 = bicicleta("vermelha", "caloi", 2022, 500, )  
# Cria uma instância da classe bicicleta com os atributos cor, modelo, ano e valor

b1.correr()
b1.buzinar()
b1.parar()
print(b1)

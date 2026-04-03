class Estudante:
    escola = "Escola XYZ"  # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome  # Atributo de instância
        self.matricula = matricula  # Atributo de instância

    def __str__(self) -> str:
        return f"{self.nome} - Matrícula: {self.matricula} - Escola: {Estudante.escola}"
    

def mostrar_informacoes(*objs): # Método de classe para mostrar informações de uma lista de objetos

        for obj in objs:
            print(obj)

# Criando instâncias da classe Estudante
estudante1 = Estudante("Alice", "12345")
estudante2 = Estudante("Bob", "67890")
mostrar_informacoes(estudante1, estudante2)

# Acessando o atributo de classe
Estudante.escola = "Alfa"  # Modificando o atributo de classe
mostrar_informacoes(estudante1, estudante2)

estudante3 = Estudante("Charlie", "54321")  # Criando uma nova instância após modificar o atributo de classe
mostrar_informacoes(estudante1, estudante2, estudante3)
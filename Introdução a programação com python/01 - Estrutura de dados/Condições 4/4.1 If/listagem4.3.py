# Carro Novo ou Velho, dependendo da idade

idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("O carro está novo")

if idade > 3:
    print(f"O carro está velho com {idade} anos de uso.")

""" Embora óbvio que um carro não poderia ter valores negativos como idade, o programa não trata desse problema. 
Vamos alterá-lo mais adiante para verificar valores inválidos. """
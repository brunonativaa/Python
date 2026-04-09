# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

num = int(input("Tabuada de:"))

inicio = int(input("Digite o inicio da tabuada:"))
fim = int(input("Digite o fim da tabuada:"))


while inicio <= fim:
    resul = num * inicio
    print(f"{num} x {inicio} = {resul}")
    inicio += 1

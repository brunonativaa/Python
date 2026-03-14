# Modifiquei o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = int(input("Digite o ultimo número a imprimir: "))

x = 1

while x <= fim:
    print(x)
    x = x + 2   # Aqui está o segredo: 1, 3, 5, 7...



"""
x = 1

while x <= fim:
    if x % 2 != 0: 
        print(x)

    x = x + 1

"""    
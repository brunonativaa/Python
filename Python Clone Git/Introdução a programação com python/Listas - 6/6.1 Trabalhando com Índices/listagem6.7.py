# Vejamos outro exemplo: um programa que lê cinco números, armazena-os em uma lista e depois solicita que o usuário escolha um número a mostrar.
#  O objetivo é, por exemplo, ler 15, 12, 5, 7 e 9 e armazená-los na lista.
#  Depois, se o usuário digitar 2, ele imprimirá o segundo número digitado, 3, o terceiro, e assim sucessivamente.
#  Observe que o índice do primeiro número é 0, e não 1: essa pequena conversão será feita no programa da listagem 6.7

numeros =  [0] * 5
x = 0

while x < 5:
    numeros[x] = int(input(f"Numero {x + 1}: "))  
    x += 1

while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    
    print(f"Você escolheu o número: {numeros[escolhido - 1]}")  ## Tradução de índice: subtraímos 1 para alinhar a contagem humana (1-based) com a do sistema (0-based).
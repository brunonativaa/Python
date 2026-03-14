#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. 
# Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

while True:
    
    lista = input("Escolha uma opção (menu): + , - , * , / , (ou 0 para sair !) " )
    tabuada = 1

    if lista == '0':
        print("Encerrando o programa aguarde ...")
        break

    tabuada = 1

    

    while tabuada <= 10:
        numero = 1
        
        while numero <= 10:
            if lista == '+':
             print(f"{tabuada} + {numero} = {tabuada + numero}")

            elif lista == '-':
               print(f"{tabuada} - {numero} = {tabuada - numero}")

            elif lista == '*':
               print(f"{tabuada} * {numero} = {tabuada * numero}")

            elif lista == '/':
               print(f"{tabuada} / {numero} = {tabuada / numero}")

            else:
               print("opção invalida!")            
            
            numero += 1

        tabuada += 1


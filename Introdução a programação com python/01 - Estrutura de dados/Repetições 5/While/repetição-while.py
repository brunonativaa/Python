opcao = -1 # Inicializa a variável opcao com um valor diferente de 0 para entrar no loop while.

while opcao != 0: # O loop while continua a ser executado enquanto a variável opcao for diferente de 0.
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n")) 

    if opcao == 1: # Verifica se a opçao escolhida pelo usuário é 1.
        print("Sacando...")
    elif opcao == 2: # Verifica se a opçao escolhida pelo usuário é 2.
        print("Exibindo extrato...")


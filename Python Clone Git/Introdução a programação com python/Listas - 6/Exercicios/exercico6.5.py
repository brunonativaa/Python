ultimo = 10
fila = list(range(1, ultimo + 1))  # Cria uma fila com os números de 1 a 10
#print(fila)  # Imprime a fila original
operacao = "" # incializa a variável operacao com os valores possíveis


while True:
    
    print(f"\nExistem {len(fila)} clientes na fila.")
    print("Fila atual:", fila)  
    print("Comandos: F (Adicionar), A (Atender), S (Sair)")

    comando = str(input("Operação: F, A ou S: ")).upper()
    
    for operacao in comando:

        if operacao == "A":
            if (len(fila)) > 0:
                atendimento = fila.pop(0)  # Remove o primeiro cliente da fila
                print(f"Cliente {atendimento} foi atendido.")
            else:
                print("A fila está vazia. Nenhum cliente para atender.")
        elif operacao == "F":
            ultimo += 1
            fila.append(ultimo)  # Adiciona um novo cliente ao final da fila
            
        elif operacao == "S":
            print("Encerrando o atendimento. Tenha um bom dia!")
            exit()
    else:
        print("Operação inválida. Por favor, digite F, A ou S.")
                
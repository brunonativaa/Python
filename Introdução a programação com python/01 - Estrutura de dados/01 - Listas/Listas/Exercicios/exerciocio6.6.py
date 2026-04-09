# Modifique o programa para trabalhar com duas filas. 
# Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. 
# O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

ultimo = 10
fila = list(range(1, ultimo + 1))  # Cria uma fila com os números de 1 a 10

fila2 = fila.copy() # Cria a segunda fila com os mesmos clientes da primeira fila


while True:
    print("Comandos: F (Adicionar), A (Atender), S (Sair)")
    print(f"\nExistem {len(fila)} clientes na fila 1.")
    print(f"Existem {len(fila2)} clientes na fila 2.")
    print("Fila 1 atual:", fila)
    print("Fila 2 atual:", fila2)

    

    comando = str(input("Operação: A (Atender Fila 1), B (Atender Fila 2), F (Adicionar Fila1) G (Adicionar Fila2) ou S (sair): ")).upper()
    
    for operacao in comando:

        if operacao == "A":
            if (len(fila)) > 0:
                atendimento = fila.pop(0)  # Remove o primeiro cliente da fila
                print(f"Cliente {atendimento} foi atendido.")
            else:
                print("A fila está vazia. Nenhum cliente para atender.")
        if operacao == "B":
            if (len(fila2)) > 0:
                atendimento = fila2.pop(0)  # Remove o primeiro cliente da fila 2
                print(f"Cliente {atendimento} foi atendido.")
            else:
                print("A fila está vazia. Nenhum cliente para atender.")
        
        elif operacao == "F":
            ultimo += 1
            fila.append(ultimo)  # Adiciona um novo cliente ao final da fila

        elif operacao == "G":
            ultimo += 1 # Incrementa o número do cliente para a fila 2
            fila2.append(ultimo)  # Adiciona um novo cliente ao final da fila 2

        elif operacao == "S":
            print("Encerrando o atendimento. Tenha um bom dia!")
            exit()
    else:
        print("Operação inválida. Por favor, digite F, A ou S.")
                
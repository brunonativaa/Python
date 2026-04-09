ultimo = 10
fila = list(range(1, ultimo + 1))  # Cria uma fila com os números de 1 a 10
#print(fila)  # Imprime a fila original

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print("Fila atual:", fila)  
    print("Digite F para chamar o proximo cliente ao fim da fila,")
    print("ou A para chamar o proximo cliente. Digite S para sair.")
    operacao = input("Operação: F, A ou S: ").upper()

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
        break
    else:
        print("Operação inválida. Por favor, digite F, A ou S.")
            
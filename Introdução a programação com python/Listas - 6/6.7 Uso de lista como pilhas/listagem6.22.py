prato = 5
pilha = list(range(1, prato + 1))  # Cria uma pilha com os números de 1 a 5

while True:
    print(f"\nExistem {len(pilha)} pratos na pilha.")
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um prato,")
    print("ou D para desempilhar um prato. Digite S para sair.")
    operacao = input("Operação: E, D ou S: ").upper()

    if operacao == "D":
        if (len(pilha)) > 0:
            lavado = pilha.pop(-1)  # Remove o último prato da pilha
            print(f"Prato {lavado} foi lavado.")
        else:
            print("A pilha está vazia. Nenhum prato para lavar.")

    elif operacao == "E":
        prato += 1
        pilha.append(prato)  # Adiciona um novo prato ao topo da pilha
    
    elif operacao == "S":
        print("Encerrando a lavagem. Tenha um bom dia!")
        break

    else:
        print("Operação inválida. Por favor, digite E, D ou S.")
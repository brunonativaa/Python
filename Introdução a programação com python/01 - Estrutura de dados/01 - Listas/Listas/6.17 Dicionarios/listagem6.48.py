# Verificação da existência de uma chave em um dicionário

tabela = {"Alface": 0.45, 
        "Batata": 1.20,
        "Tomate": 2.30,
        "Feijão": 1.50}

while True: 
    produto = input("Digite o nome do produto (ou fim para encerrar): ")
    if produto == "fim":
        print("Programa encerrado ... ") # verifica se o usuário digitou "fim" para encerrar o programa
        break # sai do loop

    if produto in tabela: # verifica se a chave "produto" existe no dicionário "tabela"
        print(f"O preço do {produto} é {tabela[produto]}") # acessa o valor associado à chave "produto" e imprime o preço

    else:  # se a chave "produto" não existe no dicionário "tabela", imprime uma mensagem informando que o produto não está na tabela
        print(f"O produto {produto} não está na tabela.")
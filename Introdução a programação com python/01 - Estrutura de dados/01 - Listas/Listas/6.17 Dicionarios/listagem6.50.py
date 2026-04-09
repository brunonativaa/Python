# Obtenção de preço com um dicionario

tabela = {"Alface": 0.45,
          "Batata": 1.20,
           "Tomate": 2.30,
            "Feijão": 1.50 }

while True:

    produto = input("Digite um produto (ou fim para terminar:)")
    if produto == "fim":
        print("Programa encerrado...")
        break
    if produto in tabela:
        print(f"Preço: {tabela[produto]}")

    else:
        print("Produto não encontrado! ")
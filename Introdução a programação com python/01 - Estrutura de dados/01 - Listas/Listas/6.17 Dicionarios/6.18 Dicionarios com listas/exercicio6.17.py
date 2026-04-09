"""Altere o programa da listagem 6.53 de forma a solicitar ao usuário o produto e a quantidade vendida.
 Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.
 """

estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
            "batata": [2001, 1.20],
             "feijao": [100, 1.50],
             "coca-cola": [158, 9.80]}


total = 0 



while True:

        produto = input("Digite um produto (ou 'sair' para terminar:)")
        

        if produto == "sair": 
        
            print("Programa encerrado... \n")
            break

        if produto in estoque:
            
            quantidade = input("Digite a quantidade (ou 'sair' para terminar): ")

        else:
            print("Produto não está no estoque! ")
        

        if quantidade == "sair":

            print("Programa encerrando...")
            break

        quantidade = int(quantidade)

        preco = estoque[produto][1]
        custo = preco * quantidade

        print("--- RESUMO DA COMPRA ---")

        print(f"Vendido: {produto} | Qtd: {quantidade} | Preço Un: R${preco:.2f} | Custo: R${custo:.2f}" )

        estoque[produto][0] -= quantidade

        total += custo
    
        print("--- ESTOQUE ATUALIZADO ---")

        for chave, dados in estoque.items():
                print(f"Produto: {chave} | Qtd restante: {dados} | Preço: R${dados[0]:.2f}")
  









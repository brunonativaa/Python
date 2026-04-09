# Criação e impressão de uma lista de compras

compras = []

while True: # enquanto for verdade
    produto = input("Digite o nome do produto: ")
    if produto == "fim":
        break # sai do loop

    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    compras.append([produto, quantidade, preco]) # adiciona uma lista com o produto, quantidade e preço à lista de compras

soma = 0.0

for e in compras: # para cada elemento e na lista de compras
    
    print(f"Produto: {e[0]}") 
    print(f"Quantidade: {e[1]}") 
    print(f"Preço: {e[2]}")
    
    soma += e[1] * e[2] # adiciona o produto do preço pela quantidade à soma

print()
print(f"Total: {soma:6.2f}") # imprime o total da compra, que é a soma dos produtos do preço pela quantidade de cada item

# Impressão das compras

produto1 = ["maça", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]

compras = [produto1, produto2, produto3] # Lista de listas, onde cada elemento é uma lista

for e in compras: # para cada elemento e na lista compras
    print(f"Produto: {e[0]}") # imprime o primeiro elemento da lista e, que é o nome do produto
    print(f"Quantidade: {e[1]}") # imprime o segundo elemento da lista e, que é a quantidade do produto
    print(f"Preço: {e[2]}") # imprime o terceiro elemento da lista e, que é o preço do produto
    print() # imprime uma linha em branco para separar as informações de cada produto

""" Da mesma forma, poderíamos ter acessado o preço do segundo elemento com compras[1][2]. 
Vejamos agora um programa completo, capaz de perguntar nome do produto, quantidade e preço e, no final,
 imprimir uma lista de compras completa.
"""
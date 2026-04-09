""" Um programa que lê uma linha contendo nomes de produtos separados por espaço.
 O programa identifica qual produto aparece mais vezes na lista. 
Se houver empate, retorna o que aparece primeiro na lista """



entrada  = input("Digite os produtos separados por espaço: ")
produtos = entrada.split().strip()  # Remove espaços em branco extras


mais_frequente = None # Variável para armazenar o produto mais frequente
maior_contagem = -1 # Variável para armazenar a maior contagem encontrada


for produto in produtos:
    contagem = produtos.count(produto)  # Conta quantas vezes o produto aparece na lista
   
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto  

print(mais_frequente) # Imprime o produto mais frequente encontrado na lista de produtos
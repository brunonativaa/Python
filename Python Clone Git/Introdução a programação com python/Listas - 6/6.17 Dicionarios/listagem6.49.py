# Obtenção de uma lista de chaves de valores

tabela = { "alface": 0.45,
           "Batata": 1.20,
           "Tomate": 2.30,
           "Feijão": 1.50}

print(tabela.keys())
print(tabela.values())

"""Observe que os métodos keys() e values() retornam geradores. 
Você pode utilizá-los diretamente dentro de um for ou transformá-los em lista usando a função list. 
Vejamos um programa que utiliza dicionários para exibir o preço de um produto na listagem 6.50.
 """
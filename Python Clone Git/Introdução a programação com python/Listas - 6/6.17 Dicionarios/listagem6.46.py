"""Em ❶, acessamos o valor associado à chave “Tomate”. Em ❷, alteramos o valor associado à chave “Tomate” para um novo valor. 
Observe que o valor anterior foi perdido. Em ❸, criamos uma nova chave, “Cebola”, que é adicionada ao dicionário.
 Veja também como Python imprime o dicionário. Outra diferença entre dicionários e listas é que, ao utilizarmos dicionários, 
perdemos a noção de ordem. Observe que, durante a manipulação do dicionário, a ordem das chaves foi alterada.
 """

# Funcionamento do dicionário

tabela = {"Alface": 0.45, 
        "Batata": 1.20,
        "Tomate": 2.30,
        "Feijão": 1.50}

print(tabela["Tomate"]) # 
print(tabela)

tabela["Tomate"] = 2.50 # altera o valor associado à chave "Tomate"
print(tabela)

tabela["Cebola"] = 1.50 # cria uma nova chave "Cebola" e associa o valor 1.50 a ela
print(tabela)


# Quanto ao acesso aos dados, temos que verificar se uma chave existe, antes de acessá-la (Listagem 6.47).


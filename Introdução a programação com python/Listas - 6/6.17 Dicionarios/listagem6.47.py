# Acesso a uma chave inexistente

tabela = {"Alface": 0.45, 
        "Batata": 1.20,
        "Tomate": 2.30,
        "Feijão": 1.50}

#print(tabela["Cebola"]) # tenta acessar a chave "Cebola", que não existe no dicionário, resultando em um erro do tipo KeyError

# Se a chave não existir, uma exceção do tipo KeyError será ativada. Para verificar se uma chave pertence ao dicionário,
#  podemos usar o operador in


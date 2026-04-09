"""Dicionários consistem em uma estrutura de dados similar às listas, mas com propriedades de acesso diferentes. 
Um dicionário é composto por um conjunto de chaves e valores. 
O dicionário em si consiste em relacionar uma chave a um valor específico. 
Em Python, criamos dicionários utilizando chaves ({}).
Cada elemento do dicionário é uma combinação de chave e valor. Vejamos um exemplo onde os preços de 
mercadorias sejam como os da tabela 6.2.
 """


tabela = {"Alface": 0.45, 
        "Batata": 1.20,
        "Tomate": 2.30,
        "Feijão": 1.50}


"""Um dicionário é acessado por suas chaves. Para obter o preço da alface, digite no interpretador, depois de ter criado a tabela, 
tabela["Alface"], onde tabela é o nome da variável do tipo dicionário, e “Alface” é nossa chave.
O valor retornado é o mesmo que associamos na tabela, ou seja, 0,45.
Diferentemente de listas, onde o índice é um número, dicionários utilizam suas chaves como índice.
Quando atribuímos um valor a uma chave, duas coisas podem ocorrer: 
1. Se a chave já existe: o valor associado é alterado
para o novo valor. 2. Se a chave não existe: a nova chave será adicionada ao dicionário. 

Em ❶, acessamos o valor associado à chave “Tomate”. Em ❷, alteramos o valor associado à chave “Tomate” para um novo valor. 
Observe que o valor anterior foi perdido. Em ❸, criamos uma nova chave, “Cebola”, que é adicionada ao dicionário.
 Veja também como Python imprime o dicionário. Outra diferença entre dicionários e listas é que, ao utilizarmos dicionários, 
perdemos a noção de ordem. Observe que, durante a manipulação do dicionário, a ordem das chaves foi alterada.
 """
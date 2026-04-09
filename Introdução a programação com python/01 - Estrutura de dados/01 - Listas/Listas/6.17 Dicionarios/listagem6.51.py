# – Exclusão de uma associação do dicionário, utilizando a instrução del


tabela = { "Alface": 0.45,
           "Batata": 1.20, 
           "Tomate": 2.30, 
           "Feijão": 1.50 }

del tabela["Tomate"] 

print(tabela)


""" Você pode estar-se perguntando quando utilizar listas e quando utilizar dicionários. Tudo depende do que você deseja realizar.
   Se seus dados são facilmente acessados por suas chaves, quase nunca você precisa acessá-los de uma só vez: um dicionário é mais
   interessante. Além disso, você pode acessar os valores associados a uma chave rapidamente sem pesquisar. 
   A implementação interna de dicionários também garante uma boa velocidade de acesso quando temos muitas chaves. 
   Porém, um dicionário não organiza suas chaves, ou seja, as primeiras chaves inseridas nem sempre serão as primeiras na 
   lista de chaves. Se seus dados precisam preservar a ordem de inserção (como em filas ou pilhas, continue a usar listas), 
   dicionários não serão uma opção. """
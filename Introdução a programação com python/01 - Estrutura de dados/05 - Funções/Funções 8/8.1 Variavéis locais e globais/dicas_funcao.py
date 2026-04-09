# Dica Python tem funções para calcular a soma, o maximo e o minimo de uma lista.


L = [5,7,8]

print(sum(L))
print(max(L))
print(min(L))



"""Quando usamos funções, começamos a trabalhar com variáveis internas ou locais e com variáveis externas ou globais. 
A diferença entre elas é a visibilidade ou escopo. Uma variável local a uma função existe apenas dentro dela, 
sendo normalmente inicializada a cada chamada. Assim, não podemos acessar o valor de uma variável local fora da função que a criou e, 
por isso, passamos parâmetros e retornamos valores nas funções, de forma a possibilitar a troca de dados no programa. 
Uma variável global é definida fora de uma função, pode ser vista por todas as funções do módulo e por todos os módulos que
importam o módulo que a definiu.

 """

EMPRESA = "Python Brasil" # Variável global

def imprime_empresa():
    print(EMPRESA) # Variável global acessada dentro da função
    print("-" * len(EMPRESA)) # Variável global acessada dentro da função

imprime_empresa()    


"""A função imprime_cabeçalho não recebe parâmetros nem retorna valores. Ela simplesmente imprime o nome da empresa e traços abaixo dele.
Observe que utilizamos a variável EMPRESA definida fora da função. Nesse caso, EMPRESA é uma variável global,
podendo ser acessada em qualquer função. Variáveis globais devem ser utilizadas o mínimo possível em seus programas,
pois dificultam a leitura e violam o encapsulamento da função. A dificuldade da leitura é em procurar pela definição e conteúdos
fora da função em si, que podem mudar entre diferentes chamadas. Além disso, uma variável global pode ser alterada por qualquer
função, tornando a tarefa de saber quem altera seu valor realmente mais trabalhosa. O encapsulamento é comprometido
"""
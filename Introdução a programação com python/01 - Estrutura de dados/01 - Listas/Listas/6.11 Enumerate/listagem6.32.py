# Impressão de índices utilizando a função enumerate

lista = [5, 9, 13]

for indice, enum in enumerate(lista):
    print(indice, enum)



"""A função enumerate gera uma tupla em que o primeiro valor é o índice e o segundo é o elemento da lista sendo enumerada.
Ao utilizarmos x, e em for, indicamos que o primeiro valor da tupla deve ser colocado em x, e o segundo, em e.
Assim, na primeira iteração teremos a tupla (0,5), onde x=0 e e=5. Isso é possível porque Python permite o desempacotamento de
valores de uma tupla, atribuindo um elemento da tupla a cada variável em for. O que temos a cada iteração de for é
equivalente a x,e = (0,5), em que o gerador enumerate retorna cada vez uma nova tupla.
Os próximos valores retornados são (1,9) e (2,13), respectivamente. Experimente substituir x,e na listagem 6.30 por z. 
Antes de print, faça x,e = z. Adicione mais um print para exibir também o valor de z.
 """
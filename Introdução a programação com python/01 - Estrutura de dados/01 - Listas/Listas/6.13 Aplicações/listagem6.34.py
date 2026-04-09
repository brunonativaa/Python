"""Vejamos uma situação na qual temos que selecionar os elementos de uma lista de forma a copiá-los para outras duas listas. 
Para simplificar o problema, imagine que os valores estejam inicialmente na lista V, mas que devam ser copiados para a P, 
se forem pares; ou para a I, se forem ímpares. Veja o programa que resolve esse problema, na listagem 6.34.
 """


v = [9,8,7,12,0,13,21]

p = []
i = []

for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)

print(f"Lista de números pares: {p}")
print(f"Lista de números ímpares: {i}")

"""Vejamos agora um programa que controla a utilização das salas de um cinema. Imagine que a lista Salas = [10,2,1,3,0] 
contenha o número de lugares vagos nas salas 1, 2, 3, 4 e 5, respectivamente. 
Esse programa lerá o número da sala e a quantidade de lugares solicitados. 
Ele deve informar se é possível vender o número de lugares solicitados, ou seja, se ainda há lugares livres. 
Caso seja possível vender os bilhetes, atualizará o número de lugares livres. 
A saída ocorre quando se digita 0 no número da sala (Listagem 6.35).
 """
    
# Python apresenta uma estrutura de repetição especialmente projetada para percorrer listas.
#  A instrução for funciona de forma parecida a while, mas a cada repetição utiliza um elemento diferente da lista. 
# A cada repetição, o próximo elemento da lista é utilizado, o que se repete até o fim da lista.
#  Vamos escrever um programa que utilize for para imprimir todos os elementos de uma lista (Listagem 6.24).

lista = [8, 9, 15]  

for elemento in lista:
    print(elemento)


# Quando começamos a executar o for em ❶, temos e igual ao primeiro elemento da lista, no caso, 8, ou seja, L[0]. 
# Em ❷ imprimimos 8, e a execução do programa volta para ❶, onde e passa a valer 9, ou seja, L[1].
#  Na próxima repetição e valerá 15, ou seja, L[2]. 
# Depois de imprimir o último número, a repetição é concluída, pois não temos mais elementos a substituir. 
# Se tivéssemos que fazer a mesma tarefa com while, teríamos que escrever um programa como o da listagem 6.25.


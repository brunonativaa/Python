"""
Modifique o programa da listagem 6.44 para ordenar a lista em ordem decrescente. 
L=[1,2,3,4,5] deve ser ordenada como L=[5,4,3,2,1].

"""

L = [1, 2, 3, 4, 5]

fim = 5

while fim > 1: # equanto o marcador for maior que 1
    trocou = False # marcador para saber se houve troca de elementos    
    
    x = 0 # marcador para percorrer a lista

    while x  < (fim - 1):
        if L[x] < L[x + 1]: 

            L[x], L[x + 1] = L[x + 1], L[x] # troca os elementos de posição
            trocou = True # houve troca de elementos

        x += 1 # incrementa o marcador x para percorrer a lista


    if not trocou: # se não houve troca de elementos  
        break # sai do loop
    fim -= 1 # decrementa o marcador fim para eliminar o último elemento da lista, que já está na posição correta

    print(f"Lista após a passagem {L}") # imprime a lista a cada passagem completa para mostrar o processo de ordenação
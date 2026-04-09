# O que acontece quando a lista já está ordenada? Rastreie o programa da listagem 6.44, mas com a lista L=[1,2,3,4,5].

""" Até agora, os elementos de nossas listas apresentam a mesma ordem em que foram digitados, sem qualquer ordenação. 
Para ordenar uma lista, realizaremos uma operação semelhante à da pesquisa, mas trocando a ordem dos elementos quando necessário. 
Um algoritmo muito simples de ordenação é o “Bubble Sort”, ou método de bolhas, fácil de entender e aprender. 
Por ser lento, você não deve utilizá-lo com listas grandes. 
A ordenação pelo método de bolhas consiste em comparar dois elementos a cada vez. 
Se o valor do primeiro elemento for maior que o do segundo, eles trocarão de posição. 
Essa operação é então repetida para o próximo elemento até o fim da lista. 
O método de bolhas exige que percorramos a lista várias vezes.
Por isso, utilizaremos um marcador para saber se chegamos ao fim da lista trocando ou não algum elemento. 
Esse método tem outra propriedade, que é posicionar o maior elemento na última posição da lista, ou seja, sua posição correta.
Isso permite eliminar um elemento do fim da lista a cada passagem completa.
Vejamos o programa da listagem 6.44.
 """

# Ordenação de uma lista pelo método de bolhas

L = [7, 4, 3, 12, 8]

fim = 5

while fim > 1: # equanto o marcador for maior que 1
    trocou = False # marcador para saber se houve troca de elementos
    x = 0 # marcador para percorrer a lista

    while x < (fim - 1): # enquanto o marcador x for menor que o marcador fim menos 1
        if L[x] > L[x + 1]: # se o elemento na posiçaõ x for maior que o elemento na posição x mais 1
            trocou = True # houve troca de elementos

            temp = L[x] # guarda o valor do elemento na posição x em uma variável temporária
            L[x] = L[x + 1] # o elemento na posição x recebe o valor do elemento na posição x mais 1
            L[x + 1] = temp # o elemento na posição x mais 1 recebe o valor guardado na variável temporária
        
        x += 1 # incrementa o marcador x para percorrer a lista

    if not trocou: # se não houve troca de elementos
        break # sai do loop

    fim -= 1 # decrementa o marcador fim para eliminar o último elemento da lista, que já está na posição correta

for e in L: # para cada elemento e na lista L
    print(e) # imprime o elemento e, que está na posição correta da lista    
# – Impressão de todos os elementos da lista com while

lista = [8, 9, 15]

contador = 0

while contador < len(lista):
    exe = lista[contador]
    print(exe)
    contador += 1


# Embora a instrução for facilite nosso trabalho, ela não substitui completamente while. 
# Dependendo do problema, utilizaremos for ou while.
#  Normalmente utilizaremos for quando quisermos processar os elementos de uma lista, um a um. 
# while é indicado para repetições nas quais não sabemos ainda quantas vezes vamos repetir ou onde manipulamos os
#  índices de forma não sequencial. Vale lembrar que a instrução break também interrompe o for. 
# Vejamos a pesquisa, escrita usando for, na listagem 6.26.


# Cálculo da média de uma lista

def soma(L):
    total = 0

    for e in L:
        total += e

    return total

def media(L):
    return(soma(L)/len(L))

""" Definir as funções dessa forma é mais interessante, pois uma função deve resolver apenas um problema. """


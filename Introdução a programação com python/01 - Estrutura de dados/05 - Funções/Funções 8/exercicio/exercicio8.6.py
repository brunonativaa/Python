# Reescreva o programa da listagem 8.8 de forma a utilizar for em vez de while.

def soma(L):
    total = 0

    for r in L: # "r" percorre até o final da Lista ("L")
    
     total += r # Armazena o valor na variavél 

    
    return total # Retorna o valor

 # A grande mágica do laço for em Python é que ele foi projetado exatamente para saber qaundo parar 
    

L = [1,7,2,9,40]

print(soma(L))

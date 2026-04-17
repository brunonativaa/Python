# Pesquisa em uma lista

def pesquisa(lista, valor): # Recebe dois parâmetros 
    for x,e in enumerate(lista): 
        if e == valor:
            return x # se o valor for encontado renorna sua posição
    return None # Caso não seja encontrado, retornaremos None

 # Dizemos que return marca o fim da execução da função
    
L = [10,20,25,30]

print(pesquisa(L, 25))
print(pesquisa(L, 27))
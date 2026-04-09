# Reescreva a função da listagem 8.5 de forma a utilizar os métodos de pesquisa em lista, vistos no capítulo 7.


def pesquisa(lista, valor):
    
    if valor in lista:
      return  lista.index(valor) # o retorno em uma unica chamada do metodo
    
    else:
        return None
        

L = [10,20,25,30,]

print(pesquisa(L,30))
"""Para pesquisar se uma string está dentro de outra e obter a posição da primeira ocorrência, 
você pode utilizar o método find (Listagem 7.9).
"""

s = "Alo mundo"

encontrada = s.find("mun")
print(encontrada)

encontrada = s.find("ok")
print(encontrada)


"""Caso a string seja encontrada, você obterá um valor maior ou igual a zero, ou -1, em caso contrário.
Observe que o valor retornado, quando maior ou igual a zero, é igual ao índice que pode ser utilizado para obter o primeiro
caractere da string procurada. Se o objetivo for pesquisar, mas da direita para a esquerda, utilize o método rfind, 
que realiza essa tarefa (Listagem 7.10).
 """
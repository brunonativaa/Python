""" Python também traz métodos que ajudam a apresentar strings de formas mais interessantes. Vejamos o método center, 
que centraliza a string em um número de posições passado como parâmetro, preenchendo com espaços à direita e à esquerda até que a string esteja 
centralizada """

# Centralização de tesxto em uma String

s = "tigre"

print("X"+s.center(10)+"X")

print("X"+s.center(10,".")+"X")

# Se, além do tamanho, você também passar o caractere de preenchimento, este será utilizado no lugar de espaços em branco.


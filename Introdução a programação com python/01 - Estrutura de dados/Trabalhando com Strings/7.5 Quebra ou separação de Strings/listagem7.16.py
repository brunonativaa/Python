# O método split quebra uma string a partir de um caractere passado como parâmetro, retornando uma lista com as substrings já separadas

# Separação de Strings

s = "um tigre, dois tigres, três tigres"

print(s.split(","))
print(s.split(" "))
print(s.split())

""" Observe que o caractere que utilizamos para dividir a string não é retornado na lista, ou seja, ele é utilizado para separar a string 
 e depois descartado."""
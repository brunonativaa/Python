s = "um tigre, dois tigres, três tigres"

word = s.find("tigres")
print(word)

word = s.rfind("tigres")
print(word)

# Podemos usar o valor retornado por find e rfind para achar todas as ocorrências da string. Por exemplo,
#  o programa da listagem 7.12 produz a saída da listagem 7.13.


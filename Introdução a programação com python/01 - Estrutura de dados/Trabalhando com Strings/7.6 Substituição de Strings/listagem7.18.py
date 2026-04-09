""" Para substituir trechos de uma string por outros, utilize o método replace. Com o método replace, o primeiro parâmetro é a string a substituir;
e o segundo, o conteúdo que a substituirá. Opcionalmente, podemos passar um terceiro parâ- metro que limita quantas vezes queremos realizar a repetição.
 """

# Substituição de strings

s = "um tigre, dois tigres, três tigres"

print(s.replace("tigre", "gato"))
print(s.replace("tigre", "gato", 1))
print(s.replace("tigre", "gato", 2))
print(s.replace("tigre", ""))
print(s.replace("", "-"))

""" Se você passar uma string vazia no segundo parâmetro, o trecho será apagado. Se o primeiro parâmetro for uma string vazia,
 o segundo será inserido antes de cada caractere da string. """
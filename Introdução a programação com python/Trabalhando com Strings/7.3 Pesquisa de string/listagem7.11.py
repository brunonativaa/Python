# Pesquisa de strings, limitando o início ou o fim

s = "um tigre, dois tigres, três tigres"

print(s.find('tigres'))
print(s.rfind('tigres'))
print(s.find('tigres',7)) # inicio = 7
print(s.find('tigres', 30)) # inicio = 30
print(s.find('tigres',0,10)) # incio = 0 fim = 10

# Podemos usar o valor retornado por find e rfind para achar todas as ocorrências da string.


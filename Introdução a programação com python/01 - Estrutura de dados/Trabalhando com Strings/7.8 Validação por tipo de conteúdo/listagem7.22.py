"""O método isdigit verifica se o valor consiste em números, retornando True se a string não estiver vazia e contiver apenas números. 
Se a string contiver espaços, pontos, vírgulas ou sinais (+ ou -), retorna falso """

umterco = "\u2153" 
novetibetano = "\u0f29"

print(umterco.isdigit())
print(umterco.isnumeric())

print(novetibetano.isdigit())
print(novetibetano.isnumeric())


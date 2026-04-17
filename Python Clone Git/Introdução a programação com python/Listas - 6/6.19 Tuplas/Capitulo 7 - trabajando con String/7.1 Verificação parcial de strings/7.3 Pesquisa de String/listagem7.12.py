# Pesquisa de todas ocorrencias!

s = "um tigre, dois tigres, três tigres"

p = 0 

while (p > -1):
    p = s.find("tigre", p)

    if p >= 0: 
        print(f"Posição: {p}")

        p += 1


"""Podemos usar o valor retornado por find e rfind para achar todas as ocorrências da string.
 Por exemplo, o programa da listagem 7.12 produz a saída da listagem 7.13.
 """        
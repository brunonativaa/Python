"""Usando 5 como início e 8 como fim, vamos imprimir os números 5, 6 e 7.
#  A nota- ção aqui para o fim é a mesma utilizada com fatias, ou seja, o fim é um intervalo aberto, isto é, 
# não incluso na faixa de valores.
"""

for v in range(5, 8):
    print(v)


"""Se acrescentarmos um terceiro parâmetro à função range, teremos como saltar entre os valores gerados, por exemplo,
 range(0,10,2) gera os pares entre 0 e 10, pois começa de 0 e adiciona 2 a cada elemento.
   Vejamos um exemplo onde geramos os 10 primeiros múltiplos de 3 (Listagem 6.29).
 """
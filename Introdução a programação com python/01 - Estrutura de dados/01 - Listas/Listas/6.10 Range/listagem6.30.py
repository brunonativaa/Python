# – Transformação do resultado de range em uma lista

lista = list(range(100, 1100, 50))

for x, e  in enumerate(lista):
    z = (x, e)
    print(z)
    print(x, e)

""" Voltando à listagem 6.29, observe que utilizamos uma construção especial com a função print, onde t é o valor que queremos imprimir,
 mas com end=" ", que indica a função para não pular de linha após a impressão. end é, na realidade, um parâmetro opcional da função 
 print. Veremos mais sobre isso quando estudarmos funções no capítulo 8. Veja também que, para saltar a linha no final do programa, 
 fizemos uma chamada a print() sem qualquer parâmetro.
 """

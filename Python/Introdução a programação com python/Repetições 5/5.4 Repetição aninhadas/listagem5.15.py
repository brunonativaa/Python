#5.4 Repetições aninhadas
#  Podemos combinar vários while de forma a obter resultados mais interessantes, como a repetição com incremento de duas variáveis.
#  Imagine imprimir as tabuadas de multiplicação de 1 a 10.
#  Vejamos como fazer isso, lendo a listagem do programa 5.15.

#Impressão de Tabuada

tabuada = 1

while tabuada <= 10:
    numero = 1
    
    while numero <= 10:
        print("%d x %d = %d " % (tabuada, numero, tabuada * numero))

        numero += 1
    
    tabuada += 1
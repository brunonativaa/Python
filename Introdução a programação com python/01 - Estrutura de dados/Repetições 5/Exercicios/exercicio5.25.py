#Escreva um programa que calcule a raiz quadrada de um número.
#  Utilize o método de Newton para obter um resultado aproximado.
#  Sendo n o nú- mero a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p.
#  A cada passo, faça b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

n = float(input("Digite um numero: "))
b = 2.0

while abs(n - b**2) >= 0.0001: # Dica de Analista: Enquanto a diferença absoluta entre (n) e (b*b) for MAIOR ou IGUAL a 0.0001...
    p = (b + (n / b)) / 2
    b = p   # Atualizei o 'b' para ser o novo 'p' para a próxima rodada

    print(f"Tentativa: {b}") #  Print para ver o computador "pensando"

print(f"A raiz quadrada aproximada é {b}")    
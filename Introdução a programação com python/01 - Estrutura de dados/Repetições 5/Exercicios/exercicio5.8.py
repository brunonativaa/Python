# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
#  Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender
#  a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
# Variáveis de controle
x = 1   # Contador (vai contar quantas vezes já somamos)
resultado = 0 # Acumulador (onde o valor vai "crescer")

while x <= numero1: # Enquanto não atingir a quantidade de vezes...
    resultado = resultado + numero2
    x = x + 1   # Incrementamos o contador para não virar loop infinito

print(f"{numero1} x {numero2} = {resultado}")

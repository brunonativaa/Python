# Escreva um programa que leia três números e que imprima o maior e o menor

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Assumimos inicialmente que o primeiro número é tanto o maior quanto o menor
maior = num2
menor = num1        

if num2 > maior:
    maior = num2
                    #  Vamos testar os outros números para ver se superam o "maior" atual
if num3 > maior:
    maior = num3  

if num2 < menor:
    menor = num2
                    #  Vamos testar os outros números para ver se são inferiores ao "menor" atual
if num3 < menor:         
    menor = num3

print(f"O maior número é 🔝 {maior}")
print(f"O menor número é ⬇️  {menor}") 
# 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

num = int(input("digite um numero para ver os 10 primeiros multiplos: "))

print(f"Os 10 primeiros multiplos de {num} são:")



# usar repetição para calcular e exibir

for i in range(1,11):
    multiplo = num * i
    print(f"{num} x {i} = {multiplo}")
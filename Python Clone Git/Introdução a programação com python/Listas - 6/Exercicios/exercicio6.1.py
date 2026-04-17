notas = [0, 0, 0, 0, 0, 0, 0,]

soma = 0
x = 0

while x < 7:
    notas[x] = float(input(f"Digite a suas nota: {x + 1}: "))
    soma += notas[x]

    x += 1
print("-" * 20)

x = 0 

while x < 7:
    print(f"✅Nota  {x + 1}:  {notas[x]:.2f}")
    x += 1

media = soma / 7

print("-" * 20)
print(f"📶 Média Final: {media:.2f}")

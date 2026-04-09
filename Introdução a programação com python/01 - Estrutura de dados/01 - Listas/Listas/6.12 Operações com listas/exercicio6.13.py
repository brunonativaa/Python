T = [-10, -8, 0, 1, 2, 5, -2, -4]
# Imprima o maior valor da lista T.
maximo = T[0]
minimo = T[0]   # Inicialização profissional do mínimo, para evitar erros caso a lista seja composta por números negativos.
soma_total = 0


for e in T:
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e

    # Acumulador para a média aritmética
    soma_total += e

    # Cálculo da média aritmética correta
# Média = (Soma de todos os elementos) / (Quantidade de elementos)

media = soma_total / len(T)

print(f"A temperatura máxima é:🌞 {maximo}")
print(f"A temperatura mínima é:❄️ {minimo}")
print(f"A temperatura média é:🌡️ {media:.2f}°C")

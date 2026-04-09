# Calculo do imposto de Renda

salario = float(input("Digite o seu salário para calculo do imposto: "))

base = salario 
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f"Salario: R${salario:.2f}. Imposto a pagar: R${imposto}")
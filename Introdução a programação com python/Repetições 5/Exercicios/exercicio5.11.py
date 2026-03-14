# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
#  Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito = float(input("Qual o deposito inicial: " ))
taxa = float(input("Qual a taxa de juros: "  ))

x = 1
saldo = deposito


while x <= 24:
    juros = (saldo*(taxa/100)) 
    saldo = saldo + juros
    print(f"Mês {x:02d} R$:{saldo:2f}")
    x = x + 1
total_ganho = saldo - deposito

print("-" * 30)
print(f"Investimento inicial R$ {deposito:.2f}")
print(f"Saldo Final:        R$ {saldo:.2f} ")
print(f"Total Ganho em Juros: R$ {total_ganho:.2f}")
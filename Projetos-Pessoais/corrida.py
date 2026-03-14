"""
    Desafio A: A Corrida das Startups (Financeiro/Business)
Cenário: Você está analisando duas Startups para investimento.

Startup X: Vale R$ 50.000,00 hoje, mas fatura e reinveste, crescendo 10% ao mês.

Startup Y: Vale R$ 200.000,00 hoje (já está consolidada), mas cresce apenas 2% ao mês.

Requisito: Crie um programa que calcule quantos meses levará para o valor de mercado ("Valuation") da Startup X ultrapassar a Startup Y.

Diferencial: Imprima o valor de ambas mês a mês formatado como moeda (ex: R$ 55.000,00).

"""


startupX = 50000.00
tax_crescimento_X = 10.0
startupY = 200000.00
tax_crescimento_Y = 2.0
mes = 0

while startupX < startupY:
    mes += 1
    startupX = (1 + (tax_crescimento_X/100)) * startupX
    startupY = (1 + (tax_crescimento_Y/100)) * startupY
    print(f"Mês: {mes}:")
    print(f"voluation Mercado startup X: R$ {startupX:.2f}")
    print(f"(voluation) Mercado startup Y: R${startupY:.2f}")
    print("-" * 30 )


print(f"\nRESULTADO: A Startup X ultrapassa a Y no mês {mes}.")    
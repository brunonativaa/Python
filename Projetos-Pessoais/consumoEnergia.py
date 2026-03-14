comsumo_energia = float(input("Qual a quantidade de kWh consumida: "))
tipo = input("Qual o tipo de consumo: 'R' residencial, 'C' comercial, 'I' industrial? ").upper()
valor = 0

if tipo == 'R':
    if comsumo_energia <= 500:
        valor = comsumo_energia * 0.40
    else:
        valor = comsumo_energia * 0.65

elif tipo == 'C':
    if comsumo_energia <= 1000:
        valor = comsumo_energia * 0.55
    else:
        valor = comsumo_energia * 0.60

elif tipo == 'I':            
    if comsumo_energia <= 5000:
        valor = comsumo_energia * 0.55
    else:
        valor = comsumo_energia * 0.60
else:
    print("Opção Invalida ! ")
4

print(f"/n processando ... ")
print(f"O valor do seu consumo de energia foi de: {valor:.2f}R$, e o tipo de consumo foi {tipo}... ")                

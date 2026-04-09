saldo = 2500
valor_saque = float(input("Digite o valor do saque: "))

status = "Saque autorizado." if valor_saque <= saldo else "Saldo insuficiente!" 
# Utiliza o operador ternário para verificar se o valor do saque é menor ou igual ao saldo disponível e atribui a mensagem  
# correspondente à variável status.


print(f"Agência 1234 - aguardando... {status}")
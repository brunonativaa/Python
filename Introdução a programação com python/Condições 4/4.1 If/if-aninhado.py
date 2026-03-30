conta_corrente = False 
conta_universitaria = True
conta_especial = False

saque = float(input("Digite o valor do saque: "))
saldo = 2000.00 # Saldo disponível na conta
cheque_especial = 500.00 # Valor do cheque especial disponível para saque

if conta_corrente: # Verifica se a conta é do tipo corrente.
    print("Conta corrente")
   
    if saque <= saldo: # Verifica se o valor do saque é menor ou igual ao saldo disponível.
        print("Saque autorizado. Tenha um bom dia!")
   
    elif saque <= saldo + cheque_especial: # Verifica se o valor do saque é menor ou igual ao saldo mais o valor do cheque especial.
        print("Saque autorizado utilizando cheque especial. Tenha um bom dia!")
    
    else:
        print("Saldo insuficiente! Tente um valor menor.") # caso o valor do saque seja maior que o saldo.

elif conta_universitaria:
    print("Conta universitária")
    
    if saque <= saldo:
        print("Saque autorizado. Tenha um bom dia!")
    
    elif saque <= saldo + cheque_especial:
        print("Saque autorizado utilizando cheque especial. Tenha um bom dia!")
    
    else:
        print("Saldo insuficiente! Tente um valor menor.")

elif conta_especial:
    print("Conta especial")
   
    if saque <= saldo:
        print("Saque autorizado. Tenha um bom dia!")
   
    elif saque <= saldo + cheque_especial:
        print("Saque autorizado utilizando cheque especial. Tenha um bom dia!")
    
    else:
        print("Saldo insuficiente! Tente um valor menor.")

else:
    print("Tipo de conta não reconhecido")

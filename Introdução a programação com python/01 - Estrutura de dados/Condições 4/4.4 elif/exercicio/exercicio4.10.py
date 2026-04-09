# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
#  Calcule o preço a pagar de acordo com a tabela a seguir.

consumo = int(input("Qual a quantidade de consumo kwh para calculo: "))
tipo = input("Tipo de instação: (R)esidencia,  (C)omerico: e (i)ndustria").lower() # Função para padronizar a entrada de dado pelo usuario



if tipo == 'r':    
    if consumo <= 500: # condiçao exigida pelo enunciado regras apenas para Residência 
        preco = 0.40 
    
    else:      # caso a condição seja falsa, ela cai nesse else         
        preco = 0.65

elif tipo == 'c':   # avaliação de regras apenas para Comércio
    if consumo <= 1000:
        preco = 0.55
   
    else:   # caso a condição seja falsa, ela cai nesse else
        preco = 0.60

elif tipo == 'i':   # avaliação de regras apenas para Industria
    if consumo == 5000:
        preco = 0.55
   
    else: # caso a condição seja falsa, ela cai nesse else
        preco = 0.60          


else: # Se o usuário não digitar R, C ou I, o tipo é inválido
    preco = 0
    print("Tipo de instalação Inválido!")

total = consumo * preco    

print(f"O preço do consumo foi de: R${total:.2f}")
          

        
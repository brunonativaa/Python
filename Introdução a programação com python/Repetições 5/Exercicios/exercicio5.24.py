# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

while True:
        try:

                numero = int(input("Quantos numeros primos você quer? "))
                break
    
        except ValueError:
            print("Erro digite numeros inteiros. ")

qtd_encontrado = 0
numero_atual = 2


while qtd_encontrado < numero:
        
    eh_primo = True


    if numero_atual == 2:
        eh_primo = True

    elif numero_atual % 2 == 0:
     eh_primo = False
    
    else:
        divisor = 3

        while divisor < numero_atual:
            if numero_atual % divisor == 0:
                 eh_primo = False
                 break 
            divisor += 2
        
    if eh_primo == True:
        print(f"{numero_atual} é primo!")
        qtd_encontrado += 1

    numero_atual += 1
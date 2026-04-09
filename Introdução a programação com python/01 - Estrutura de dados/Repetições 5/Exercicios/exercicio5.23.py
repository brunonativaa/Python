# Escreva um programa que leia um número e verifique se é ou não um número primo.
#  Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. 
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
#  Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
while True:


    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break

    if numero == 2:
        print("È primo (O unico par!)")
        continue

    elif numero == 0 or numero == 1:
        print("Não é primo")
        continue

    elif numero % 2 == 0:
        print("Não é primo (é par) ")
        continue


    eh_primo = True
    contador = 3

    while contador < numero:
        if numero % contador == 0:
            eh_primo = False
            break

        contador += 2

    if eh_primo:
        print("È primo!")

    else:
        print("Não é primo")
# Calculo do fatorial

def fatorial(n):
    fat = 1

    while n > 1: #  calculamos o fatorial multiplicando o valor de n pelo valor anterior (fat)

        
        fat *= n # calculamos o fatorial multiplicando o valor de n pelo valor anterior (fat)
 

        n -= 1

    return fat

print(fatorial(4)) 
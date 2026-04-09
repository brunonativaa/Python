# Outra forma de calcular o fatorial

def fatorial(n):
    fat = 1

    x = 1

    while x <= n:       # Existem várias formas de resolver o problema, todas podem estar corretas.
            # Para decidir se a implementação está correta temos que observa os valores retornados com os valores de referência
        fat *= x 

        x += 1

    return fat

print(fatorial(6))



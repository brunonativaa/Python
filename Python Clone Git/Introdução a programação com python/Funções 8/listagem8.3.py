# uma função que retorne verdadeiro ou falso, dependendo se o número é par ou ímpar

def epar(x):
    return(x % 2 == 0)

print(epar(2))
print(epar(3))
print(epar(10))

# Imagine agora que precisamos definir uma função para retornar a palavra par ou ímpar. Podemos reutilizar épar em outra função

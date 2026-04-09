# Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

def eh_multiplo(a , b):
    if a % b == 0: # usando o resto da divisão 
        return f"{a} é multiplo de {b} true"
    else:
        return f"{a} não é multiplo de {b} false"
    
print(eh_multiplo(10,5))
print(eh_multiplo(10,3))
print(eh_multiplo(8,4))
print(eh_multiplo(7,3))
print(eh_multiplo(5,5))
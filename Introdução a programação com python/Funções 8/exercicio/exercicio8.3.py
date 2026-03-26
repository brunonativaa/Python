""" Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado2 ). 
Valores esperados: área_quadrado(4) == 16 área_quadrado(9) == 81
 """
def calculo_quadrado(lado):
    
    A = lado ** 2

    return A

print(calculo_quadrado(4))
print(calculo_quadrado(9))
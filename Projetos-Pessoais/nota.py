nota = float(input("Digite uma nota entre 0 e 10: "))
while (nota < 0) or (nota > 10):
    nota = float(input("Não pode ser menor que 0 e maior que 10 my friend! \n \
                       Tente novamente: "))
print('Nota valida!')
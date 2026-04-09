# Uso da função range com saltos

for t in range(3, 33, 3):
    print(t, end=" ")
print(type(t))


"""Observe que um gerador como o retornado pela função range não é exatamente uma lista.
Embora seja usado de forma parecida, é, na realidade, um objeto de outro tipo. Para transformar um gerador em lista,
utilize a função list (Listagem 6.30).
 """
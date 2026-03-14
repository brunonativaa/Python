lista = []

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    lista.append(num)

x = 0

while x < len(lista):
    print(lista[x])
    x += 1
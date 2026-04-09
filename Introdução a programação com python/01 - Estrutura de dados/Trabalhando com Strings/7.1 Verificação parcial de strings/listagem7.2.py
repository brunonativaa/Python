# Convertendo uma string em lista

L = list("Alò Mundo")
                        # A função list transeforma cada carectere da string em um elemento da lista
L[0] = "a"

print(L)


s = "".join(L)          # O elemento join faz a operação inversa trasnformando os elementos da lista em string

print(s)

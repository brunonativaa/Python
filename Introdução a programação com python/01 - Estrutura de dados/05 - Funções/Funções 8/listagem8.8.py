# Como não escrever uma função

def soma(L):
    total = 0
    x = 0

    while x < 5:
    
        total += L[x]

        x +=1 
    return total

L = [1,7,2,9,15]

print(soma(L))
print(soma([7,9,13,3,100,20,4]))



""" A forma como definimos a função soma não é genérica, ou melhor, só funciona em casos onde devemos somar listas com cinco elementos.
É para esse tipo de erro que você deve ficar atento. Se a função deve somar todos os elementos de qualquer lista passada como 
parâmetro, devemos ao menos presumir que podemos passar listas com tamanhos diferentes. Explicaremos mais sobre isso quando 
falarmos de testes. Um problema clássico de programação é o cálculo do fatorial. O fatorial de um número é utilizado em estatística
para calcular o número de combinações e permutações de conjuntos. Seu cálculo é simples, por isso, é muito utilizado como 
exemplo em cursos de programação. Para calcular o fatorial, multiplicamos o número por todos os números que o precedem até 
chegarmos em 1.
 
Por exemplo:
• fatorial de 3: 3 x 2 x 1 = 6. 
• fatorial de 4: 4 x 3 x 2 x 1 = 24

   """
""" Embora devamos utilizar variáveis globais com cuidado, isso não significa que elas não tenham uso ou que possam simplesmente ser 
classificadas como má prática. Um bom uso de variáveis globais é guardar valores constantes e que devem ser acessíveis a todas as funções
do programa, como o nome da empresa. Elas também são utilizadas em nosso programa principal e para inicializar o mó- dulo com valores 
iniciais. Tente utilizar variáveis globais apenas para configuração e com valores constantes. Por exemplo, se na função 
imprime_cabeçalho o nome da empresa mudasse entre uma chamada e outra, ele não deveria ser armazenado em uma variável global,
mas passado por parâmetro. Devido à capacidade da linguagem Python de declarar variáveis à medida que precisarmos, 
devemos tomar cuidado quando alteramos uma variável global dentro de uma função.
 """


a = 5 

def muda_e_imprime():
    a = 7 # A variável a é local a função muda_e_imprime, ou seja, ela existe apenas dentro da função.
    print(f"A variável a dentro da função = {a}")

print(f"A variável a fora da função = {a}")
muda_e_imprime()
print(f"A variável a depois de mudar  dentro da função = {a}") 
# A variável a continua com o valor 5, pois a variável a dentro da função é local e não altera o valor da variável global a.
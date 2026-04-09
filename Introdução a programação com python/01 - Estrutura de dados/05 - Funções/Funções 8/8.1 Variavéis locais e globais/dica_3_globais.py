""" Se quisermos modificar uma variável global dentro de uma função, devemos informar que estamos usando uma variável global antes de 
inicializá-la, na primeira linha de nossa função. Essa definição é feita com a instrução global.
"""

a = 5 

def muda_e_imprime():
    global a # A variável a é global, ou seja, ela existe em todo o programa.
    a = 7 # A variável a é global, ou seja, ela existe em todo o programa.
    print(f"A variável a dentro da função = {a}")

print(f"A variável a fora da função = {a}")
muda_e_imprime()
print(f"A variável a depois de mudar  dentro da função = {a}") 


"""limitar o uso de variáveis globais. A utilização da instrução global pode sinalizar um problema de construção no programa. 
Lembre-se de utilizar variáveis globais apenas para configuração e, de preferência, como constantes. Dessa forma, 
você utilizará global apenas nas funções que alteram a configuração de seu programa ou módulo.
A instrução global facilita a escolha de nomes de variáveis locais nos programas, pois deixa claro que estamos usando uma variável
preexistente e não criando uma nova. Tente definir variáveis globais de forma a facilitar a leitura de seu programa, como usar apenas
letras maiúsculas em seus nomes ou um prefixo, por exemplo, EMPRESA ou G_EMPRESA.

(Página 166). """
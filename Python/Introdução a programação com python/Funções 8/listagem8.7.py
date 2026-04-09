# Soma e cálculo da média de uma lista

def media(L):
    total = 0

    for e in L:
        total += e
    
    return total/len(L)


""" Qual das duas formas escolher depende do tipo de problema que se quer resolver. Se você não precisa do valor da soma dos elementos
de uma lista em nenhuma parte do programa, a segunda forma é interessante. A primeira (soma e média definidas em duas funções separadas)
é mais interessante em longo prazo e é também uma boa prática de programação. Conforme formos criando funções, podemos armazená-las 
para uso em outros programas. Com o tempo, você vai colecionar essas funções, criando uma biblioteca ou módulo. Veremos mais sobre isso quando falarmos de importação e módulos. Por enquanto, tente fixar duas regras: 
uma função deve resolver apenas um problema e, quanto mais genérica for sua solução, melhor ela será em longo prazo. Para saber se sua
função resolve apenas um problema, tente defini-la sem utilizar a conjunção “e”. Se ela faz isso e aquilo, já é um sinal que efetua 
mais de uma tarefa e que talvez tenha que ser desmembrada em outras funções. Não se preocupe agora em definir funções perfeitas,
pois à medida que você for ganhando experiência na programação esses conceitos se tornarão mais claros.

O fato de a função só poder ser utilizada no mesmo programa que a definiu não é um grande problema, pois à medida que os programas
se tornam mais complexos eles exigem soluções próprias e detalhadas. No entanto, se todas as suas funções servirem apenas a um
programa, considere isso como um sinal de alerta. 

 """
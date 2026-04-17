# Exemplos de conversão em maiscula e minuscula

"""Observe a listagem 7.3. Veja que comparamos “João da Silva” com “joão” e obtivemos False. Esse é um detalhe pequeno,
 mas importante, pois startswith e endswith consideram letras maiúsculas e minúsculas como letras diferentes. 
 Você pode resolver esse tipo de problema convertendo a string para maiúsculas ou minúsculas antes de realizar a comparação. 
 O método lower retorna uma cópia da string com todos os caracteres minúsculos, e o método upper retorna uma cópia com
todos os caracteres maiúsculos. Veja os exemplos na listagem 7.4.

(Página 134). """

s = "O Rato roeu a roupa do Rei de Roma"
print(s.lower())
print(s.upper())


print(s.lower().startswith("o rato"))
print(s.upper().startswith("O RATO"))

# Não se esqueça de comparar com uma string onde todos os caracteres são maiúsculos ou minúsculos, 
# dependendo se você utilizou upper ou lower, respectivamente.


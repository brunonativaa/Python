""" Strings em Python podem ter seu conteúdo analisado e verificado utilizando- -se métodos especiais.
 Esses métodos verificam se todos os caracteres são letras, números ou uma combinação deles. """

s = "125"
p = "alo mundo"

print(s.isalnum())
print(p.isalnum())
print(s.isalpha())
print(p.isalpha())

""" O método isalnum retorna verdadeiro se a string não estiver vazia, e se todos os seus caracteres são letras e/ou números.
 Se a string contiver outros tipos de caracteres, como espaços, vírgula, exclamação, interrogação ou caracteres de controle, retorna False.
   Já isalpha é mais restritivo, retornando verdadeiro apenas se todos os caracteres forem letras, incluindo vogais acentuadas. 
   Retorna falso se algum outro tipo de caractere for encontrado na string ou se estiver vazia. """
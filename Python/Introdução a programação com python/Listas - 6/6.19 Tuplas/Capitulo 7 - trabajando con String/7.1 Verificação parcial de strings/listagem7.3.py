"""Quando você precisar verificar se uma string começa ou termina com alguns caracteres, você pode usar os métodos startswith e endswith.
 Esses métodos verificam apenas os primeiros (startswith) ou os últimos (endswith) caracteres da string,
   retornando True caso sejam iguais ou False em caso contrário.
 """

nome = "João da Silva"

print(nome.startswith("João"))
print(nome.startswith("joão"))
print(nome.endswith("Silva"))

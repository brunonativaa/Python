#Faça um programa que leia uma expressão com parênteses.
#  Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. 
# Exemplo: (()) OK ()()(()()) OK ()) Erro

expressao = input("Digite uma expressão com parênteses: ")
pilha = []
erro = False


for caractere in expressao:
   if caractere == "(":
      pilha.append("(")  # Adiciona um parêntese de abertura à pilha (Push)"

   elif caractere == ")":
      if len(pilha) > 0:
         pilha.pop() # Remove o último parêntese de abertura da pilha (Pop)

      else:
         erro = True # Tentou Fechar um parêntese sem ter um correspondente de abertura
         break  

if not erro and len(pilha) == 0:
   print("Ok - Parêntses Corretos!")

else:
   print("Erro - Parênteses Incorretos!")
         
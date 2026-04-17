nome = input("Nome com no minimo [4 caracteres] : ")
idade = int(input("Sua idade: " ))
salario = float(input("Salario: " ))
sexo = input("Sexo ('F' para feminino or 'M'para masculino) : ")
estado_civil = input("Estado civil ('s', 'c', 'v', 'd'):")

while len(nome) <=3:
    nome = input(" Seu nome deve ter mais que 3 caracterer, Tente novamente: ")

while (idade < 0) or (idade > 150): 
    idade = int(input("Sua idade deve estar entre 0 and 150 years:"))

while (salario < 0):
    salario = float(input("Seu salario deve ser maior que (Zero): "))

while (sexo != 'F') and (sexo != 'M'): 
    sexo = input("Biologicamente você deve ser 'F' or 'M': ")

while (estado_civil!='s')and(estado_civil!='c')and(estado_civil!='v')and(estado_civil!='d'):
    print("Nao tem estado civil 'confuso'")
    estado_civil = input("Deve ser s, c, v ou d: ")    

print("teste...")

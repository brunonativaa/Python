
nome_usuario = input("Nome de usuario: ")
senha_usuario = input("Senha: ")
    
while nome_usuario == senha_usuario:    
    print("Erro, sua senha deve ser diferente do nome de usuario: ")
    senha_usuario = input("Senha: ")
print("OK, Você está logado! ")
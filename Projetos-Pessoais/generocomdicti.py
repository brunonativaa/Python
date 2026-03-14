opcao = {
    '1': 'Você é Mulher.',
    '2': 'Você é Homem.',
   
}

sexo = input('Escolha um genero.\n[1] Mulher\n[2] Homem\n ')

resultados = opcao.get(sexo, 'Opção invalida')
print(resultados)
opcao = {
    '1': 'Você é Mulher.',
    '2': 'Você é Homem.',
    '3': 'Você é outro',
}

sexo = input('Escolha um genero.\n[1] Mulher\n[2] Homem\n[3] Outro \n ')

resultados = opcao.get(sexo, 'Opção invalida')
print(resultados)
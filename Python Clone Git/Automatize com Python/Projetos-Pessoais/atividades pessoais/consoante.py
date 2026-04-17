def consoante_vogal():
    letra = input('Digite um caracter:' ).lower()

    if letra in 'aeiou':
        print('È vogal')

    else:
        print('È uma consoante!')

consoante_vogal()
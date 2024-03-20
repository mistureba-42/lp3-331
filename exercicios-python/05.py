palavra = str(input('digite uma palavra'))

if palavra == palavra[::-1]:
    print('a palavra é um palindromo')
else:
    print('a palavra não é um palindromo')
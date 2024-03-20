pontuacao = float(input('digite a pontuacao entre 1 e 100'))

if pontuacao < 25:
    print('sua nota é E')
elif pontuacao < 50:
    print('sua nota é D')
elif pontuacao < 75:
    print('sua nota é C')
elif pontuacao < 90 :
    print('sua nota é B')
else:
    print('sua nota é A')
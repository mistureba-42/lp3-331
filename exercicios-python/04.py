votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

contador = 0
while contador < 10:
    voto = int(input('registre seu voto'))
    match voto:
        case 1:
            votos_candidato1 +=1
        case 2:
            votos_candidato2 +=1
        case 3:
            votos_candidato3 +=1
    contador += 1

print ('candidato1: votos=', votos_candidato1)
print ('candidato2: votos=', votos_candidato2)
print ('candidato3: votos=', votos_candidato3)

if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
    print('candidato 1 venceu a eleição')
elif votos_candidato2 > votos_candidato3:
    print('candidato 2 venceu a eleição')
else:
    print('candidato 3 venceu a eleição')
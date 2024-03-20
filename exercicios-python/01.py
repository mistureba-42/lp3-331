import random

numero_escolhido = random.randint(1,100)

numero = int(input('digite um numero'))

while True:

    if numero_escolhido - numero <= 5 or numero - numero_escolhido <= 5:
        print('esta muito perto')   
             
    elif numero_escolhido - numero <= 10 or numero - numero_escolhido <= 10:
        print('esta perto')    
            
    elif numero_escolhido - numero <= 25 or numero - numero_escolhido <= 25:
        print('esta chegando')    
            
    elif numero_escolhido - numero <= 50 or numero - numero_escolhido <= 50:
        print('esta longe')
        
    elif numero_escolhido - numero > 50 or numero - numero_escolhido > 50:
        print('esta muito longe')
        
    elif numero == numero_escolhido:
        print('voce acertou')
        break
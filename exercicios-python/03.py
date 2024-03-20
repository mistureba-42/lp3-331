frase = str(input('digite uma frase ou palavra'))

Consoantes =['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
Vogais = ['a','e','i','o','u']
vogais = 0
consoantes = 0

for letra in frase:
    if letra in Vogais:
        vogais += 1
    elif letra in Consoantes:
        consoantes +=1
    
print('total de vogais',vogais, 'total de consoantes', consoantes)
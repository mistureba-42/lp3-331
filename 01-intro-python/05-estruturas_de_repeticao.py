# for, while, (break/continue)

for letra in "Ola Mundo":
    print(letra)

prontuarios = ["SP001", "SP002", "SP003"]
for prontuario in prontuarios:
    print (prontuario)

#range(5) ==> 0, 1, 2, 3, 4
for i in  range(5):
    print(i)

#range(start,stop,step)
for i in range (0, 12, 2):
    print(i)

lista = list(range(1,101))
print (lista)

#while
contador = 0
while contador < 5:
    print(contador)
    contador +=1

#break
comando = " "
while True:
    comando = input("Digite um comando")

    if comando == "sair":
        break

    if comando == "1":
        print("UM")
    if comando == "2":
        print("DOIS")

#continue
numeros = [3, -1, 2, 0, -4, 5]

for numero in numeros:
    if numero <=0:
        continue
    print(numero)

for numero in numeros:
    if numero >0:
        print(numero)

# compreensao de listas

numeros = [3, -1, 2, 0, -4, 5]
positivos = []

for numero in numeros:
    if numero >0:
        positivos.append(numero)

# [expressao for item in lista if condicao]
positivos = [numero for numero in numeros if numero>0]
quadrado = [numero**2 for numero in numeros]


#1. numeros

#int; float; complex
#int: numeros inteiros
#float: numeros com casas decimais
#complex: calculos com numeros complexos

#2. booleano
verdade= True
falso = False

#3. sequencias
#str; list; tuple; set; dict

#str
#conjunto de caracteres
#pode usar "" ou ''

#str com quebra de linha
frase = """
a
b
c
"""

#interpolação de str

# f-strings
nome = 'maria'
idade = 83
mensagem = f'minha vo se chama {nome}, ela tem {idade} anos'

#char nao existe

#como acessar os caracteres de uma str
nome = 'Silvio Santos'

print(nome[2])

#metodos do str
print(nome.upper())

#list
#lista de valores
#permite diferentes tipos de dados na mesma lista
letras =[ 'a', 'b', 'c']

print(letras[2])

for letra in letras:
    print(letra)

#adicionar a uma lista (no final)
letras.append('d')

#insert (adiciona numa posicao especifica e empurra o resto pra +1)

#remove: remove itens da lista

#tuple
#"lista" de valores
#nao pode ser alterada
opcoes = ('sim', 'nao', 'talvez')

#set
#conjunto de valores
#nao indexado, nao permite elementos duplicados

jogos ={'mario', 'gta'}

#dict
#palavra -> definicao
#chave -> valor

#none
#variaveis que serao inicializadas em tempo de execuução
#retorno ou parametros de funçao 
nulo = None
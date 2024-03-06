# operadores aritimeticos
# +, -, *, /, %, **

nota1 = 3.0
nota2 = 5.0
madia = (nota1 + nota2)/2

#2², 2³
potencia = 2 ** 2
potencia2 = 2 ** 3

#operadores de atribuição
# = += -=

idade = 10

idade += 10

#operadores logicos
# and, or, not

print( True or True)

# and - true se todos forem true
# or - false se todos forem false
# not - oposto (true -> false)

#operadores de comparação
# == != > < >= <= 

idade = 21
maio_de_idade = idade >= 18

if  maio_de_idade:
    print("maior de idade")

else:
    print("menor de idade")

#operador is
# os valores do objeto e se ocupam o mesmo espaço de memoria
a = [1,2,3]
b = [1,2,3]

print(a is b)

z = [1,2,3]
x = z
print (z is x)

#operador in e not in
#verifica se um objeto esta ou nao dentro de uma sequencia
# str, list, turple

print("a" in java)

print("Maria" in ("pedro", "ana"))

alunos = ["pedro", "ana"]
aluno = "Maria"
print (aluno in alunos)
print (aluno not in alunos)

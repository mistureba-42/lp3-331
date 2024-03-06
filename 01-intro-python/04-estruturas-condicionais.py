# if, if/else, if/elif/else, ternario, match

#if
#if condicao:
#   corpo
#   corpo
#   corpo

idade = 20
if idade >= 18:
    print("maior de idade")

print ("fim do IF")

#if/else
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

print("fim do IF/ELSE")

#elif
#criança(0-12), adolescente(13-17), adulto(18-59), idoso(60+)
if idade <=12:
    print("Criança")
elif idade <=17:
    print("Adolescente")
elif idade <=59:
    print("Adulto")
else:
    print("idoso")

#if alinhado (evitar)
email = "algo@gmail.com"
senha = ("123456789")

if email == "algo@gmail.com":
    if senha == "123456789":
        print ("acesso liberado")
    else:
        print("email ou senha incorretos")
else:
    print("email ou senha incorretos")

#desalinhamento
if email == "algo@gmail.com" and senha == "123456789":
    print ("acesso liberado")
else:
    print("email ou senha incorretos")

#condicao complexa dentro do if
#permitir entrada se
#o usuario nao estiver bloqueado e 
#o usuario for um funcionario
#o hora atual entre 08 e 18
#OU
#o usuario e admin

usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 19
usuario_admin = False

if (not usuario_bloqueado and usuario_funcionario and hora_atual >=8 and hora_atual <=18) or usuario_admin:
    print("liberado")
else:
    print("nao liberado")


horario_comercial = hora_atual >=8 and hora_atual <=18
funcionario_ativo = not usuario_bloqueado and usuario_funcionario
liberado = funcionario_ativo and horario_comercial or usuario_admin

if liberado:
    print("liberado")
else:
    print("nao liberado")


def dentro_horario_comercial(hora_atual):
    return hora_atual >=8 and hora_atual <=18

#operador ternario
if idade >= 18:
    status = "maior"
else:
    status = "menor"

status = "maior" if idade <= 18 else "menor"

#usuario passa o dia (int)
# devolve str nome
#1- dom ...
#7- sab
dia = 4

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sabado",
}

if dia in dias:
    print (dias (dia))

# match
#python 3.10
# 'switch case' mais poderoso

dia = 2
match dia:
    case 1:
        print ("Domingo")
    case 2:
        print ("Segunda")
    case 3 :
        print ("Terça")
    case 4:
        print ("Quarta")
    case 5:
        print ("Quinta")
    case 6:
        print ("Sexta")
    case 7:
        print ("Sabado")

match dia:
    case 1|7:
        print("Fim de semana")
    case 1|2|3|4|5|6:
        print("dia util")
    case _:
        print("invalido")


#crie uma lista com 4 perguntas para uma pessoa sobre um crime.
#conhece a vitima?
#
#2 resposta positivas = "suspeita"
#3 resposta positivas = "cumplice"
#4 resposta positivas = "você é um assassino"
#1 ou nenhuma resposta positiva = "Inocente"

perguntas = ["Você conhece a vítima? \n:", "Esteve no local do Crime? \n:", "Se encontrou com a Vítima? \n:", "Trabalha com a Vítima? \n:"]
cont = 0
for x in range(0,4):
    print("responda sim ou nao")
    a = input(perguntas[x]).upper()
    if a == "SIM":
        cont += 1
    else:
        cont += 0

if cont == 2:
    print("Você é considrado Suspeito!")
elif cont == 3:
    print("Você é considerado Cumplíce!")
elif cont == 4:
    print("Você é o Assassino!!")
elif cont == 1 or cont == 0:
    print("Você é considerado Inocente!")

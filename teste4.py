#crie uma lista com 4 perguntas para uma pessoa sobre um crime.
#conhece a vitima?
#
#2 resposta positivas = "suspeita"
#3 resposta positivas = "cumplice"
#4 resposta positivas = "você é um assassino"
#1 ou nenhuma resposta positiva = "Inocente"

perguntas = ["Você conhecia a vítima? \n:", "Você esteve com a vítima nesses ultimos tempos? \n:", "Você já trabalhou com a vítima? \n:", "Você ja se encontrou com a vítima? \n:"]
cont = 0
for x in range(0,4): #O x vai rodar o for 4 vezes
    while True: #estrutura caso o usuário não escreva corretamente
        print("Responda sim/n ou nao/n \n")
        a = input(perguntas[x]).upper() #transforma o resultado da pergunta em maiúsculo
        if a == "SIM" or a == "S":
            print("ok")
            cont += 1 #adiciona + 1 ao contador 
            break
        elif a == "NAO" or a == "N":
            print("ok")
            cont += 0 #adiciona + 0 ao contador 
            break
        else:
            print("por favor inserir corretamente!")
            continue
if cont == 2:
    print("SUSPEITO")
elif cont == 3:
    print("CÚMPLICE")
elif cont == 4:
    print("VOCÊ É O ASSASSINO")
elif cont == 1 or cont == 0:
    print("INOCENTE")

#HORA DA VERDADE
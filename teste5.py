#Faça uma função que receba um valor para imprimir no formato abaixo:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5 5

def escada():
    numero = input("Digite um número!! \n:")
    str_numero = numero + " "
    int_numero = int(numero)
    print(int_numero * str_numero)

escada()
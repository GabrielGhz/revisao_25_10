import time


nome = input ("Digite seu nome: ")
cont = 1
for i in nome:
    time.sleep(1)
    print(nome[0:cont])
    cont = cont+1

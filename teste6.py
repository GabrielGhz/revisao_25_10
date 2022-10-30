#Faça uma função que imprima a quantidade de digitos em um 
# numero inteiro recebido e imprima o reverso desse mesmo numero e a
#soma dele com ele mesmo

num = input("digite uma quantidade de números! \n:")
num_int = int(num)
print("a numeração tem {} caracteres" .format(len(num)))
num = list(num)
print("E lendo ele de trás pra frente fica assim", num[::-1])
print("A soma do seu número {} mais ele mesmo é : {}" .format(num_int, num_int+num_int))
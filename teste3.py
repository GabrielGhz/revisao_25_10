#leia duas listas cada uma com 5 elementos. forme uma terceira lista
#de 10 elementos, onde os valores debem estar
#intercalados (valor da primeira, valor da segunda.)

l1 = []
l2 = []
l3 = []
for x in range(0,5):
    x = (input("adicione um valor a sua lista: "))
    y = (input("adicione uma letra a sua lista: "))
    l1.append(x)
    l1.append(y)
    l3.append(x)
    l3.append(y)

print(l3)


    

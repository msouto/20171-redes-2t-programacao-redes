import random
nomes = open("nome.txt").readlines()
random.shuffle(nomes)
for i in nomes:
    print(i) #imprimir sorteio de vários elementos de uma única vez

import random
nomes = open("nome.txt").readlines()
random.shuffle(nomes)
print(nomes.pop() )

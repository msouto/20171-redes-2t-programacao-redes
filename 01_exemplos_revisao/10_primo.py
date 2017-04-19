y=11
x = y // 2
while x > 1:
    if y % x == 0:
        print(y,"tem o fator",x)
        break
    x-=1
else:
    print(y,'eh primo.')

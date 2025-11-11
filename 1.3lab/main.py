import math
x = float(input("x:"))
n = int(input("n:"))
k = 0
for st in range(1,1+n):
    k += math.sin(x ** st)
    print('summ =',k)

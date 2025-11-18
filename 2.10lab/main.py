a) try:
    n = int(input('число:'))
    if n < 0 : raise ValueError('отрицательное число')
    fac = 1
    for i in range(1,n + 1 ): fac *= i
    print('факториал = ', fac)
except ValueError as e: print (e)
b) try:
    n = int(input('число:'))
    if n <= 0: raise ValueError('число не является положительным')
    print('число является положительным')
except ValueError as e:
    print(e)
c) try:
    n = int(input('число:'))
    assert n>=0, 'отрицательное число'
    fac = 1
    for i in range(1,n + 1):
        fac *= i
    print('факториал = ',fac)
except ValueError as e:
    print(e)

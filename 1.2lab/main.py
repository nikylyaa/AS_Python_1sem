# задание 6 из егэ-  профиль [https://math-ege.sdamgia.ru/problem?id=77370]
# Решите уравнение (2 * x + 7)**2 == (2**x-1)**2
'''
x = -10
while x <= 10:
    if (2 * x + 7)**2 == (2 * x - 1)**2:
        print(x)
    x += 0.5

# комментарий:  этои примере задача решена с помощью расчетов поформулам и нахождения неизвестног. К решению приложена ссылка на источник, а расчеты можно проверить вручную
#num 1:
K, N = map(int, input().split())
for i in range(N):
    print(K, end='')
#num 1
k = int(input('ввод k:'))
n = int(input('ввод n:'))
for i in range(n):
    print(k)
#num2
a = int(input('ввод a:'))
b = int(input('ввод b:'))
for i in range (a,b+1):
    print(i)
n = b - a + 1
print('количество этих чисел n =',n)
#num3
a = int(input('ввод a:'))
b = int(input('ввод b:'))
for i in range (b-1,a,-1):
    print(i)
n = b - a - 1
print('количество этих чисел n =',n)
#num4
for i in range(1,2):
    print(i, 'shtyka=', 20.4 * i,'pyb')
for i in range(2,5):
    print(i, 'shtyki=', 20.4 * i, 'pyb')
for i in range(5, 11):
    print(i, 'shtyk=', 20.4 * i, 'pyb')
#num5
a = int(input())
b = int(input())
h = int(input())
for i in range(a,b+1,h):
    print(i,'v kvadr =',i * i)
#num6
a = int(input())
b = int(input())
h = int(input())
for i in range(a,b+1,h):
    if i > 0:
        print(i)'''
#num7
a = int(input())
b = int(input())

summ = 0
for i in range(a,b+1):
    summ+=i
    print('сумма =',summ)

num = list(map(int,input().split()))
a = int(input())
for i in range (len(num)):
    if num[i] % 2== 0:
        num[i] += a
print(num)


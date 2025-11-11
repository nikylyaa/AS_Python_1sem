num = list(map(int,input().split()))
res = sorted ([x for x in num if x < 15], reverse = True)
print(res)

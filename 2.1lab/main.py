d = {'a':1, 'b':2, 'c':3, 'd':4}
lst = [{'a':1}, {'a':2}, {'a':3}, {'b':1}]
students = {'Иван':{'рост':170,'вес':70}, 'Михаил':{'рост':180,'вес':75}}
print('а)')
# а)
for k, v in d.items():
    print(f"key: {k}, value: {v}")
# б)
print('б)')
print("Сумма по 'a':", sum(x.get('a',0) for x in lst))
# в)
print('в)')
print({n:{'рост':info['рост']} for n,info in students.items()})

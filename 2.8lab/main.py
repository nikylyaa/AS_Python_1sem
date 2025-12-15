r = open("f.txt", "r")
text = r.read()
r.close()
numbers = text.split()
for i in range(len(numbers)):
    numbers[i] = float(numbers[i])
max_value = 0
for i in range(0, len(numbers), 2):
    if abs(numbers[i]) > max_value:
        max_value = abs(numbers[i])
print("Максимальный модуль среди нечётных номеров:", max_value)

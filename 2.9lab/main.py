f = open("input.txt")
s = open("symmetric.txt", "w")
o = open("other.txt", "w")

for _ in range(int(f.readline())):
    n = int(f.readline())
    m = [list(map(int, f.readline().split())) for _ in range(n)]
    out = s if all(m[i][j] == m[j][i] for i in range(n) for j in range(n)) else o
    out.write(str(n) + "\n")
    for row in m:
        out.write(" ".join(map(str, row)) + "\n")

f.close()
s.close()
o.close()

print("Исходный файл:\n", open("input.txt").read())
print("Симметрические матрицы:\n", open("symmetric.txt").read())
print("Остальные матрицы:\n", open("other.txt").read())

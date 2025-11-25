import math
def TypeTrl(x1, y1, x2, y2, x3, y3):
    a = math.dist((x1, y1), (x2, y2))
    b = math.dist((x2, y2), (x3, y3))
    c = math.dist((x3, y3), (x1, y1))
    if a + b <= c or a + c <= b or b + c <= a:
        return "не существует"
    if a == b == c:
        return "pавносторонний"
    if a == b or b == c or a == c:
        return "pавнобедренный"
    sides = sorted([a, b, c])
    if abs(sides[2] ** 2 - (sides[0] ** 2 + sides[1] ** 2)) < 1e-6:
        return "прямоугольный"
    return "обычный"

file = open("q13.txt").read().splitlines()

p1, p2 = 0, 0
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
for line in file:
    if line.startswith("Button A:"):
        temp = line.split(',')
        a = int(temp[0][12:])
        d = int(temp[1][3:])
    elif line.startswith("Button B:"):
        temp = line.split(',')
        b = int(temp[0][12:])
        e = int(temp[1][3:])
    elif line.startswith("Prize: "):
        temp = line.split(',')
        c = int(temp[0][9:])
        f = int(temp[1][3:])
    elif line == '':
        x1 = (b * f - e * c) / (d * b - e * a)
        y1 = (c - a * x1) / b
        if int(x1) == x1:
            p1 += int(3 * x1 + y1)
        x2 = (b * (f + 10000000000000) - e * (c + 10000000000000)) / (d * b - e * a)
        y2 = (c + 10000000000000 - a * x2) / b
        if int(x2) == x2:
            p2 += int(3 * x2 + y2)

print(p1, p2)

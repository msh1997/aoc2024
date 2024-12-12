from collections import defaultdict

file = open('q12.txt').read().splitlines()

plot = defaultdict(str)
for i, a in enumerate(file):
    for j, b in enumerate(a):
        plot[(i, j)] = b

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def search(i, j, cur, visited):
    if plot[(i, j)] != cur:
        return 0, 0
    if visited.__contains__((i, j)):
        return 0, 0
    visited.add((i, j))
    perimeter = 0
    area = 1
    for dir in dirs:
        if plot[(i + dir[0], j + dir[1])] == cur:
            res = search(i + dir[0], j + dir[1], cur, visited)
            perimeter += res[0]
            area += res[1]
        else:
            perimeter += 1
    return perimeter, area



corners = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def search2(i, j, cur, visited):
    if plot[(i, j)] != cur:
        return (0, 0)
    if visited.__contains__((i, j)):
        return (0, 0)
    visited.add((i, j))
    vertex = 0
    area = 1
    for c in corners:
        if plot[(i + c[0], j)] == cur == plot[(i, j + c[1])] and plot[(i + c[0], j + c[1])] != cur:
            vertex += 1
        if plot[(i + c[0], j)] != cur and plot[(i, j + c[1])] != cur:
            vertex += 1
    for dir in dirs:
        res = search2(i + dir[0], j + dir[1], cur, visited)
        area += res[0]
        vertex += res[1]
    return area, vertex


visited1 = set()
visited2 = set()
p1 = 0
p2 = 0
for i in range(len(file)):
    for j in range(len(file[0])):
        if not visited1.__contains__((i, j)):
            res1 = search(i, j, plot[(i, j)], visited1)
            p1 += res1[0] * res1[1]
            res2 = search2(i, j, plot[(i, j)], visited2)
            p2 += res2[0] * res2[1]

print(p1, p2)
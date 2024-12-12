file = open("q10.txt").read().splitlines()

topo_map = list(map(lambda x: list(map(lambda y: int(y), x)), file))

def search(x, y, cur, m, travelled):
    if not 0 <= x < len(topo_map) or not 0 <= y < len(topo_map[0]):
        return 0
    if travelled is not None and travelled.__contains__((x, y)):
        return 0
    if m[x][y] != cur:
        return 0
    if travelled is not None:
        travelled.add((x, y))
    if m[x][y] == 9:
        return 1
    return search(x + 1, y, cur + 1, m, travelled) + search(x, y + 1, cur + 1, m, travelled) + search(x - 1, y, cur + 1, m, travelled) + search(x, y - 1, cur + 1, m, travelled)

p1 = 0
p2 = 0
for i in range(len(topo_map)):
    for j in range(len(topo_map[0])):
        if topo_map[i][j] == 0:
            p1 += search(i, j, 0, topo_map, set())
            p2 += search(i, j, 0, topo_map, None)
print(p1, p2)

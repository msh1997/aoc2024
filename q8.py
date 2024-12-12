from collections import defaultdict
from itertools import combinations

file = open('q8.txt').read().splitlines()

arr = list(map(list, file))
nodes = defaultdict(list)
nodes2 = []

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] != '.':
            nodes[arr[i][j]].append((i, j))
            nodes2.append((i, j))


antinodes = set()
antinodes2 = set()
for n in nodes.keys():
    pairs = list(combinations(nodes[n], 2))
    for p in pairs:
        x, y = p[0][0] - p[1][0], p[0][1] - p[1][1]
        antinodes.add((p[0][0] + x, p[0][1] + y))
        antinodes.add((p[1][0] - x, p[1][1] - y))
        antinodes2.add(p[0])
        antinodes2.add(p[1])
        a, b = p[0][0] + x, p[0][1] + y
        while 0 <= a < len(arr) and 0 <= b < len(arr[0]):
            antinodes2.add((a, b))
            a += x
            b += y
        a, b = p[0][0] - x, p[0][1] - y
        while 0 <= a < len(arr) and 0 <= b < len(arr[0]):
            antinodes2.add((a, b))
            a -= x
            b -= y

print(len(list(filter(lambda x: 0 <= x[0] < len(arr) and 0 <= x[1] < len(arr[0]), antinodes))))
print(len(antinodes2))
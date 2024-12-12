from collections import defaultdict

file = open("q11.txt").read().splitlines()[0].split(' ')

stones = defaultdict(int, map(lambda x: (int(x), 1), file))

def blink(a):
    temp = str(a)
    if a == 0:
        return 1, None
    if len(temp) % 2 == 0:
        return int(temp[len(temp) // 2:]), int(temp[:len(temp) // 2])
    return a * 2024, None

p1 = 0
p2 = 0
for i in range(75):
    temp = defaultdict(lambda: 0)
    for j in stones.keys():
        a, b = blink(j)
        temp[a] += stones[j]
        if b is not None:
            temp[b] += stones[j]
    stones = temp
    if i == 25:
        p1 = sum(stones.values())

p2 = sum(stones.values())
print(p1, p2)

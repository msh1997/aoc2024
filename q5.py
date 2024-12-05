from collections import defaultdict
from math import floor

file = open('./q5.txt').read().splitlines()

rules = defaultdict(set)
pages = []

a = False

for line in file:
    if line == '':
        a = True
    elif not a:
        b, c = line.split('|')
        rules[b].add(c)
    else:
        pages.append(line.split(','))


def check(p):
    for i in range(len(p) - 1):
        for j in range(i + 1, len(p)):
            if not rules[p[i]].__contains__(p[j]):
                return False
    return True


def swap(p):
    i, j = 0, 1
    while i < len(p) - 1:
        j = i + 1
        while j < len(p):
            if not rules[p[i]].__contains__(p[j]):
                temp = p[j]
                p[j] = p[i]
                p[i] = temp
            else:
                j += 1
        i += 1


p1 = p2 = 0
for p in pages:
    if not check(p):
        swap(p)
        p2 += int(p[floor(len(p) / 2)])
    else:
        p1 += int(p[floor(len(p) / 2)])

print(p1, p2)

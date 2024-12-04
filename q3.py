import re

file = open('./q3.txt').read().splitlines()

res1 = 0
res2 = 0
disabled = False
for line in file:
    p1 = re.findall('mul\([0-9]+,[0-9]+\)', line)
    p2 = re.findall('(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))', line)
    for i in p1:
        left, right = i.split(',')
        res1 += int(left[4:]) * int(right[:-1])
    for j in p2:
        if j[1] != '':
            disabled = False
        elif j[2] != '':
            disabled = True
        elif not disabled:
            left, right = j[0].split(',')
            res2 += int(left[4:]) * int(right[:-1])

print(res1, res2)

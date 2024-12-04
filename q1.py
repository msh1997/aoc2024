from collections import defaultdict

file = open('./q1.txt').read().splitlines()
a, b = list(), defaultdict(int)

for line in file:
    nums = line.split()
    a.append(int(nums[0]))
    b[int(nums[1])] += 1

total = 0

for i in a:
    total += (i * b[i])

print(total)

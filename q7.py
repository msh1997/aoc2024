file = open('q7.txt').read().splitlines()


def search(cur, l, target):
    if len(l) == 0:
        return cur == target
    if cur > target:
        return False
    temp = l[1:]
    ## p1
    # return search(cur + l[0], temp, target) or search(cur * l[0], temp, target)
    ## p2
    return search(cur + l[0], temp, target) or search(cur * l[0], temp, target) or search(int(str(cur) + str(l[0])), temp, target)


total = 0
for f in file:
    t = f.split(': ')
    v, l = int(t[0]), list(map(int, t[1].split(' ')))
    if search(0, l, v):
        total += v

print(total)
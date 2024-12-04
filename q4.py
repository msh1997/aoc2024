file = open('./q4.txt').read().splitlines()

strs = list(map(list, file))

dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
    (1,1),
    (1,-1),
    (-1,1),
    (-1,-1)
]
chars = 'XMAS'


def check1(dir, i, j):
    for k in range(4):
        a, b = i + dir[0] * k, j + dir[1] * k
        if not 0 <= a < len(strs) or not 0 <= b < len(strs[0]) or not strs[a][b] == chars[k]:
            return False
    return True


def check2(i, j):
    if not 0 < i < len(strs) - 1 or not 0 < j < len(strs[0]) - 1 or strs[i][j] != 'A':
        return False
    chars = [strs[i-1][j-1],strs[i-1][j+1],strs[i+1][j-1],strs[i+1][j+1]]
    m, s = len(list(filter(lambda x: x == 'M', chars))), len(list(filter(lambda x: x == 'S', chars)))
    if m == s == 2:
        return strs[i-1][j-1] != strs[i+1][j+1]


def p1():
    count = 0
    for i in range(len(strs)):
        for j in range(len(strs[0])):
            for k in dirs:
                if check1(k, i, j):
                    count += 1
    print(count)


def p2():
    count = 0
    for i in range(1, len(strs) - 1):
        for j in range(1, len(strs[0]) - 1):
            if check2(i, j):
                count += 1
    print(count)

p1()
p2()

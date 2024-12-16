from collections import deque

file = open("q15.txt").read().split('\n\n')

moves = []
dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1)
}

def get_warehouse():
    warehouse = []
    for line in file[0].split('\n'):
        warehouse.append(list(line))
    return warehouse

moves = list(file[1].replace('\n', ''))

def tick(i, j, d, w):
    a, b = i, j
    c = 0
    while 0 <= a < len(w) and 0 <= b < len(w[0]):
        if w[a][b] == '#':
            return i, j
        elif w[a][b] == '.':
            break
        a += d[0]
        b += d[1]
        c += 1
    i += d[0]
    j += d[1]
    for k in range(c):
        w[a][b] = w[a - d[0]][b - d[1]]
        a -= d[0]
        b -= d[1]
    w[a][b] = '.'
    return i, j

def tick2(i, j, d, w):
    boxes = deque()
    boxes.append((i, j))
    visited = []
    while len(boxes) > 0:
        for k in range(len(boxes)):
            box = boxes.popleft()
            if w[box[0]][box[1]] == '#':
                return i, j
            if w[box[0]][box[1]] == '[':
                boxes.append((box[0] + d[0], box[1]))
                boxes.append((box[0] + d[0], box[1] + 1))
            elif w[box[0]][box[1]] == ']':
                boxes.append((box[0] + d[0], box[1]))
                boxes.append((box[0] + d[0], box[1] - 1))
            elif w[box[0]][box[1]] == '@':
                boxes.append((box[0] + d[0], box[1]))

        boxes = deque(set(boxes))
        for b in boxes:
            visited.append((b[0], b[1]))
    for b in visited[::-1]:
        w[b[0]][b[1]] = w[b[0] - d[0]][b[1]]
        w[b[0] - d[0]][b[1]] = '.'
    return i + d[0], j

def find_start(w):
    i, j = 0, 0
    for a in range(len(w)):
        for b in range(len(w[0])):
            if w[a][b] == '@':
                i, j = a, b
    return i, j

def gps(w):
    gps = 0
    for i in range(len(w)):
        for j in range(len(w[0])):
            if w[i][j] == 'O' or w[i][j] == '[':
                gps += i * 100 + j
    return gps

def p1():
    warehouse = get_warehouse()
    i, j = find_start(warehouse)
    for move in moves:
        i, j = tick(i, j, dirs[move], warehouse)
    res = gps(warehouse)
    print(res)

def p2():
    warehouse = get_warehouse()
    warehouse2 = []
    for i in range(len(warehouse)):
        l = []
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '#' or warehouse[i][j] == '.':
                l.append(warehouse[i][j])
                l.append(warehouse[i][j])
            elif warehouse[i][j] == 'O':
                l.append('[')
                l.append(']')
            elif warehouse[i][j] == '@':
                l.append('@')
                l.append('.')
        warehouse2.append(l)
    i, j = find_start(warehouse2)
    for move in moves:
        if move == '^' or move == 'v':
            i, j = tick2(i, j, dirs[move], warehouse2)
        else:
            i, j = tick(i, j, dirs[move], warehouse2)
    res = gps(warehouse2)
    print(res)

p1()
p2()

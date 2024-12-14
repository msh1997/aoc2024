from collections import defaultdict

file = open('q14.txt').read().splitlines()

pos, vel = list(), list()

length, width = 101, 103

grid = defaultdict(int)
for line in file:
    a = line.split(" ")
    p = a[0].split(',')
    pos.append((int(p[0][2:]), int(p[1])))
    v = a[1].split(',')
    vel.append((int(v[0][2:]), int(v[1])))

q1 = q2 = q3 = q4 = 0

def print_tree(temp):
    with open('out.txt', 'a') as f:
        for i in range(width):
            str = ''
            for j in range(length):
                if temp.__contains__((j, i)):
                    str += '#'
                else:
                    str += '.'
            print(str)
        print('\n\n')

for i in range(10000):
    for j in range(len(pos)):
        x, y = (pos[j][0] + vel[j][0]) % length, (pos[j][1] + vel[j][1]) % width
        pos[j] = (x, y)
        if i == 99:
            if x == int(length / 2) or y == int(width / 2):
                continue
            elif x < length / 2 and y < width / 2:
                q1 += 1
            elif x < length / 2 and y > width / 2:
                q2 += 1
            elif x > length / 2 and y < width / 2:
                q3 += 1
            elif x > length / 2 and y > width / 2:
                q4 += 1
    if len(set(pos)) == len(pos):
        print_tree(set(pos))
        print(i)

print(q1 * q2 * q3 * q4)
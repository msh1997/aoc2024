import itertools

file = list(map(int, open('q9.txt').read().splitlines()[0]))


def get_disk():
    disk = []
    for i, a in enumerate(file):
        if i % 2 == 0:
            disk.append([int(i / 2)] * a)
        else:
            disk.append(['.'] * a)

    disk = list(itertools.chain(*disk))
    return disk


def checksum(disk):
    cs = 0
    for i, a in enumerate(disk):
        if a != '.':
            cs += i * a
    return cs


def p1():
    disk = get_disk()
    start = 0
    end = len(disk) - 1
    while start < end:
        if disk[end] != '.':
            while disk[start] != '.':
                start += 1
            if start > end:
                break
            disk[start] = disk[end]
            disk[end] = '.'
            start += 1
        end -= 1
    print(checksum(disk))


def p2():
    disk = get_disk()
    file_dupe = file.copy()
    end_idx = len(disk) - 1
    for i in range(len(file) - 1, 0, -2):
        for j in range(1, i, 2):
            if file[j] >= file[i]:
                idx = 0
                for k in range(j):
                    idx += file_dupe[k]
                start = idx
                while disk[start] != '.':
                    start += 1
                for k in range(file[i]):
                    disk[start + k] = int(i / 2)
                    disk[end_idx - k] = '.'
                file[j] -= file[i]
                break
        end_idx -= file_dupe[i] + file_dupe[i - 1]
    print(checksum(disk))


p1()
p2()

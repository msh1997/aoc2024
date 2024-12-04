file = open('./q2.txt').read().splitlines()

reports = []
for line in file:
    reports.append(list(map(lambda x: int(x), line.split(' '))))


def check(report):
    diff = []
    for i in range(len(report) - 1):
        diff.append(report[i + 1] - report[i])
    return not ((len(list(filter(lambda x: x > 0, diff))) != len(diff) and len(list(filter(lambda x: x < 0, diff))) != len(diff)) or len(list(filter(lambda x: 1 <= abs(x) <= 3, diff))) != len(diff))


# p1
count = 0
for report in reports:
    if check(report):
        count += 1

print(count)


# p2
count = 0
for report in reports:
    for i in range(len(report)):
        temp = report[:i] + report[i + 1:]
        if check(temp):
            count += 1
            break

print(count)

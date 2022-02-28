import sys

N = int(sys.stdin.readline())
tables = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split(' '))
    tables.append([start, end])

tables = sorted(tables, key=lambda a: a[0])
tables = sorted(tables, key=lambda a: a[1])

counter = 0
end = 0
for i, j in tables:
    if i >= end:
        counter += 1
        end = j
print(counter)
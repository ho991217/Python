"""
5
55 185
58 183
88 186
60 175
46 155
"""
import sys

N = int(sys.stdin.readline().rstrip())

info = []
for _ in range(N):
    indiv = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
    info.append(indiv)

order = []

for i in info:
    counter = 1
    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            counter += 1
    order.append(counter)

for i in order:
    print(i, end=' ')
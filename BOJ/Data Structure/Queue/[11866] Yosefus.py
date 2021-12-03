import sys
from collections import deque
dq = deque()
N, K = map(int, sys.stdin.readline().rstrip().split(' '))

for i in range(1, N + 1):
    dq.append(i)
eleminated = []
while len(dq) != 0:
    count = 1
    while count < K:
        dq.append(dq.popleft())
        count += 1

    eleminated.append(dq.popleft())

print('<', end='')
for e in range(len(eleminated)):
    print(eleminated[e], end='')
    if e < len(eleminated) - 1: print(',',end=' ')

print('>')
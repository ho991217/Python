import sys

N, M, B = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
height = 0
answer = 100000000000000000000000000000

for i in range(257):
    maxH = 0
    minH = 0

    for j in range(N):
        for k in range(M):
            if table[j][k] < i:
                minH += i - table[j][k]
            else:
                maxH += table[j][k] - i
    inven = maxH + B
    if inven < minH: continue
    time = 2 * maxH + minH

    if time <= answer:
        answer = time
        height = i
print(answer, height)
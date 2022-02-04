import sys

M, N = map(int, sys.stdin.readline().split(' '))

dex = [sys.stdin.readline().rstrip() for _ in range(M)]



for i in range(N):
    q = sys.stdin.readline().rstrip()
    if ord(q[0]) < 60:
        print(dex[int(q) - 1])

    elif 65 <= ord(q[0]):
        print(dex.index(q) + 1)
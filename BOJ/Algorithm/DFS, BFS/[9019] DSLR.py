import sys
from collections import deque

T = int(sys.stdin.readline())

def D(n):
    return (n * 2) % 10000

def S(n):
    if n == 0: return 9999
    return n-1

def L(n):
    return (n - n % 1000) // 1000 + (n % 1000) * 10

def R(n):
    return n // 10 + (n % 10) * 1000

def bfs(start, target):
    visited = [False] * 10_000
    q = deque([[start, ""]])

    while q:
        cur, path = q.popleft()
        visited[cur] = True
        if cur == target:
            print(path)
            break

        tmp = D(cur)
        if not visited[tmp]:
            q.append([tmp, path + "D"])
            visited[tmp] = True

        tmp = S(cur)
        if not visited[tmp]:
            q.append([tmp, path + "S"])
            visited[tmp] = True

        tmp = L(cur)
        if not visited[tmp]:
            q.append([tmp, path + "L"])
            visited[tmp] = True

        tmp = R(cur)
        if not visited[tmp]:
            q.append([tmp, path + "R"])
            visited[tmp] = True

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    bfs(A, B)
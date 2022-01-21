import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and field[nx][ny][0] == 1 and field[nx][ny][1] is False:
                field[nx][ny][1] = True
                q.append((nx, ny))

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split(' '))

    field = [[[0, False] for i in range(N)] for j in range(M)]

    for i in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        field[x][y][0] = 1

    counter = 0
    for i in range(M):
        for j in range(N):
            if field[i][j][1] is False and field[i][j][0] == 1:
                BFS(i, j)
                counter += 1

    print(counter)
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
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and field[ny][nx][0] == 1 and field[ny][nx][1] is False:
                field[ny][ny][1] = True
                q.append((nx, ny))

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split(' '))

    field = [[[0, False] for x in range(M)] for j in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        field[x][y][0] = 1

    # counter = 0
    # for x in range(M):
    #     for y in range(N):
    #         if field[y][x][1] is False:
    #             # BFS(x, y)
    #             counter += 1
    # print(counter)

    print(field)

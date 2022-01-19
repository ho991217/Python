import sys
from collections import deque

N = int(sys.stdin.readline())
grid = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]
q = deque()
visited = [[0] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (grid[nx][ny] == grid[x][y]) and (not visited[nx][ny]):
                visited[nx][ny] = 1
                q.append((nx, ny))


counter1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            counter1 += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
counter2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            counter2 += 1

print(counter1, counter2)

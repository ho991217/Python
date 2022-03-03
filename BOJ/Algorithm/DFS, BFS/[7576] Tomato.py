import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())

graph = []
queue = deque()

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < N and 0 <= b < M and graph[a][b] == 0:
                queue.append([a, b])
                graph[a][b] = graph[x][y] + 1


day = 0
bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day-1)
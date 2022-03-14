import sys
from collections import deque

N = int(sys.stdin.readline())
parent = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque([1])
    visited[1] = True
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                parent[i] = cur
                q.append(i)
                visited[i] = True
bfs()
for i in range(2, len(parent)):
    print(parent[i])
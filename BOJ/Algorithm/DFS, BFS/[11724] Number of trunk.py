import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
if M == 0:
    print(N)
    exit(0)
adj = [[] for i in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(graph, visited, index):
    q = deque([index])
    visited[index] = True

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

counter = 0
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if visited[i]: continue
    bfs(adj, visited, i)
    counter += 1

print(counter)

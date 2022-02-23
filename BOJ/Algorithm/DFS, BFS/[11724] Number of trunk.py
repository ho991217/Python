import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adj = dict()

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u in adj:
        adj[u] = adj[u] + [v]
    else:
        adj[u] = [v]

    if v in adj:
        adj[v] = adj[v] + [u]
    else:
        adj[v] = [u]


def bfs(graph, start):
    visited = []
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur not in visited:
            visited.append(cur)
            q.extend(graph[cur])

    for item in visited:
        if item in list(graph.keys()):
            graph.pop(item)

    return graph

counter = 0
while adj:
    counter += 1
    starter = list(adj.keys())[0]
    adj = bfs(adj, starter)

print(counter)
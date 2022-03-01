import sys
from heapq import heappop, heappush
INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1)
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heappop(queue)

        if dist > distance[now]: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(queue, (cost, i[0]))

dijkstra(start)
distance.pop(0)
for i in distance:
    if i >= 1000000000:
        print('INF')
    else:
        print(i)

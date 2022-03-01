import sys
from heapq import heappop, heappush
INF = int(1e9)

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N + 1)]
students = [0 for i in range(N + 1)]
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight))

def dijkstra(start):
    queue = []
    distance = [INF] * (N + 1)
    heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(queue, (cost, i[0]))

    return distance

for i in range(1, N + 1):
    time = dijkstra(i)[X] + dijkstra(X)[i]
    students[i] = time

students.pop(0)
print(max(students))

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9);

N, E = map(int, input().rstrip().split())

graph = [[] for i in range(N + 1)]
graph[0] = None

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().rstrip().split())

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        dist, now, = heapq.heappop(heap)

        for newn, neww in graph[now]:
            weight = neww + dist
            if distance[newn] > weight:
                distance[newn] = weight
                heapq.heappush(heap, [weight, newn])

    return distance

first = dijkstra(1)
_v1 = dijkstra(v1)
_v2 = dijkstra(v2)

count = min(first[v1] + _v1[v2] + _v2[N], first[v2] + _v2[v1] + _v1[N])
print(count if count < INF else -1)
import sys
import heapq

INF = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj = {i + 1: {} for i in range(N)}
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().rstrip().split())
    if end in adj[start].keys():
        weight = min(adj[start][end], weight)
    adj[start].update({end: weight})

# print(adj)

distances = [INF] * (N+1)
start, target = map(int, sys.stdin.readline().rstrip().split())

def dijkstra(start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in adj[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

dijkstra(start)
print(distances[target])
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())

box = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]
graph = dict()
apart = False
roast = []
for i in range(N):
    for j in range(M):
        # 토마토가 칸에 들어 있는 경우
        if box[i][j] >= 0:
            if box[i][j] == 1: roast.append((i, j))

            graph[(i, j)] = []
            if i-1 >= 0 and box[i-1][j] >= 0:
                graph[(i, j)].append((i-1, j))

            if j-1 >= 0 and box[i][j-1] >= 0:
                graph[(i, j)].append((i, j-1))

            if i+1 < N and box[i+1][j] >= 0:
                graph[(i, j)].append((i+1, j))

            if j+1 < M and box[i][j+1] >= 0:
                graph[(i, j)].append((i, j+1))

            # 인접 노드가 하나도 없을 경우
            if graph[(i, j)] == []:
                apart = True


def bfs(graph, roasted):
    if len(roasted) == len(list(graph.keys())):
        return 0
    elif apart:
        return -1

    day = 0
    visited = roasted
    queue = deque()
    queue.append(roasted)
    while queue:
        nodes = queue.popleft()
        if nodes == []: break
        today_tomatoes = []
        for cur in nodes:
            for i in graph[cur]:
                if i not in visited:
                    today_tomatoes.append(i)

        for u in today_tomatoes:
            visited.append(u)
        queue.append(today_tomatoes)
        day += 1


    return day-1

print(bfs(graph, roast))

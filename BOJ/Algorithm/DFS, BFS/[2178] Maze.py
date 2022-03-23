import sys

"""
4 6
101111
101010
101011
111011
"""

N, M = [int(x) for x in input().split()]

maze = [[int(i) for i in sys.stdin.readline().rstrip()] for j in range(N)]

adj = dict()

dx = [0, 1, 0 ,-1]
dy = [-1, 0, 1, 0]

for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            adj[(i, j)] = []
            for k in range(4):
                if 0 <= i + dx[k] < N and 0 <= j + dy[k] < M:
                    if maze[i + dx[k]][j + dy[k]] == 1:
                        adj[(i, j)].append((i + dx[k], j + dy[k]))
                else:
                    pass

visited = []
target = (N - 1, M - 1)

def dfs():
    minCount = 0
    s = [(0, 0)]
    count = 1
    while s:
        cur = s.pop()
        if cur == target:
            if minCount > count:
                minCount = count
            else:


        else:
            count += 1
            if cur not in visited:
                s.extend(adj[cur])
                visited.append(cur)
            # else:
            #     count -= 1

    return minCount

print(dfs())

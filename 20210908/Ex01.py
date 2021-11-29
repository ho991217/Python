from collections import deque

# DFS, BFS (Depth First Search)
def DFS(graph, start):

    visited = []
    stack = [start]

    while stack:
        pop = stack.pop()
        if pop not in visited:
            visited.append(pop)
            if pop in graph:
                tmp = list(set(graph[pop]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp

    return " ".join(str(i) for i in visited)

# BFS (Breath First Search)
def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        pop = queue.popleft()
        if pop not in visited:
            visited.append(pop)
            if pop in graph:
                tmp = list(set(graph[pop]) - set(visited))
                tmp.sort()
                queue += tmp
    return " ".join(str(i) for i in visited)


# Graph
vertex, edge, start = [int(i) for i in input().split()]

graph = {}
for i in range(edge):
    n1, n2 = [int(i) for i in input().split()]
    if n1 not in graph:
        graph[n1] = [int(n2)]
    elif n2 not in graph[n1]:
        graph[n1].append(int(n2))

    if n2 not in graph:
        graph[n2] = [int(n1)]
    elif n1 not in graph[n2]:
        graph[n2].append(int(n1))

print(DFS(graph, start))
print(BFS(graph, start))

# Stack을 이용한 DFS
def DFS_stack(graph, start):
    visited = []
    stack = [start]
    while stack:
        pop = stack.pop()
        if pop not in visited:
            visited.append(pop)
            if pop in graph:
                # set의 차집합 이용하여 pop key의 value 중 방문한 곳을 제거, 방문 안한 값들을 push
                tmp = list(set(graph[pop]) - set(visited))
                # stack에 push 하기 위해서는 list를 내림차순으로 정렬해야함
                tmp.sort(reverse=True)
                stack += tmp
    return visited

# 재귀를 이용한 DFS
def DFS_recursive(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            DFS_recursive(graph, node, visited)

    return visited



# Queue를 이용한 BFS
from collections import deque

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
    return  visited



graph = {1:[2, 3, 4], 2:[1, 5], 3:[1, 6], 4:[1], 5:[2], 6:[3]}
print(DFS_stack(graph, 1))
print(DFS_recursive(graph, 1))
print(BFS(graph, 1))


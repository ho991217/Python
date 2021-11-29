"""
input :
4 5 1
1 2
1 3
1 4
2 4
3 4
"""
"""
output :
1 2 4 3
1 2 3 4
"""
# class Empty(Exception):
#     pass
#
# class Node:
#     def __init__(self, data):
#         self.val = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def isEmpty(self):
#         return self.stack == []
#
#     def push(self, data):
#         self.stack.append(data)
#
#     def pop(self):
#         if self.isEmpty():
#             raise Empty('EmptyStack!')
#         return self.stack.pop()
#
#     def peek(self):
#         return self.stack[len(self.stack) - 1]
#
#
#
# vertexCount, EdgeCount, Starter = input().split()
# vertexCount, EdgeCount, Starter = int(vertexCount), int(EdgeCount), int(Starter)
#
# vertexList = [str(x) for x in range(1, vertexCount + 1)]
# edgeList = [[int(x) for x in input().split()] for x in range(EdgeCount)]
#
# graphs = (vertexList, edgeList)
#
# def DFS, BFS(graph, start):
#     vertexList, edgeList = graph
#     visitedList = []
#     s = Stack()
#     s.push(start)
#
#     adjacencyList = [[] for vertex in vertexList]
#
#     for edge in edgeList:
#         adjacencyList[edge[0] - 1].append(edge[1])
#         adjacencyList[edge[1] - 1].append(edge[0])
#
#     print(adjacencyList)
#
#     while not s.isEmpty():
#         pop = s.pop() - 1
#         for neighbor in adjacencyList[pop]:
#             if pop + 1 not in visitedList:
#                 s.push(neighbor)
#
#         if pop + 1 not in visitedList:
#             visitedList.append(pop + 1)
#
#     return visitedList
#
#
#
# print(DFS, BFS(graphs, Starter))

from collections import deque

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))
"""
BOJ 2606
[입력]
첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

[출력]
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

[입력예제]              [출력예제]
7                     4
6
1 2
2 3
1 5
5 2
5 6
4 7
"""
# DFS, BFS 사용
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
    return visited


# 입력
vertex = int(input())
edge = int(input())

graph = {}
for i in range(edge):
    n1, n2 = [int(i) for i in input().split()]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)


print(len(DFS(graph, 1)) - 1)
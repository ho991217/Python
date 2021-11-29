# dfs (깊이우선탐색)
# 루트 노드다 임의의 노드에서 시작하여 최대로 진입할 수 있는 깇이 까지 탐색
# Stack 을 사용하여 데이터를 탐색
# 경로상의 노드들만 기억하면 되므로 저장공간 수요가 적다

class Flow(Exception):
    pass

class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.is_empty():
           raise Flow('StackUnderflow!')
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise  Flow('StackUnderflow!')
        return self.data[len(self.data) - 1]

    def is_empty(self):
        return self.data == []

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0), (1,3), (2,0), (2,4),
            (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]

graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    s = Stack()
    s.push(start)

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    print(adjacencyList)

    while not s.is_empty():
        pop = s.pop()
        for neighbor in adjacencyList[pop]:
            if pop not in visitedList:
                s.push(neighbor)

        if pop not in visitedList:
            visitedList.append(pop)

    return visitedList



print(dfs(graphs, 0))
# 정답 : 0, 2, 5, 4, 6, 1, 3
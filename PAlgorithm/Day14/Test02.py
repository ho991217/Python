# BFS Algorithm (너비우선 탐색)
# 그래프에서 가까운 노드부터 탐색하는 알고리즘
# - 모든 간선의 비용이 동일한 조건에서 최단거리를 구하는 문제
# - 미로를 빠져나가는 최단 경로

# BFS 알고리즘은 그래프에서 가장 가장 가까운 노드부터 탐색하는 방식이기 때문에,
# FIFO 방식의 Queue 자료구조를 사용


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.val
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

    def is_empty(self):
        if not self.head:
            return True

        return False

    def print_Queue(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end = ' ')
            cur = cur.next
        print()

q = Queue()
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.print_Queue()

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]

graphs = (vertexList, edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    print(adjacencyList)

    while queue:
        pop = queue.pop()
        for neighbor in adjacencyList[pop]:
            if neighbor not in visitedList:
                queue.insert(0, neighbor)

        visitedList.append(pop)

    print(visitedList)


bfs(graphs, 0)

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = self.tail.next

    def dequeue(self):
        self.checkEmpty()
        data = self.head.val
        self.head = self.head.next
        return data

    def peek(self):
        return self.head.val

    def checkEmpty(self):
        if self.isEmpty():
            raise Empty('EmptyQueue!')

    def isEmpty(self):
        return self.head == None

    def printQueue(self):
        self.checkEmpty()

        cur = self.head
        while cur is not None:
            print(cur.val,end=' ')
            cur = cur.next
        print()

q = LinkedQueue()

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (1, 6), (1, 0)]

graphs = (vertexList, edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = LinkedQueue()
    queue.enqueue(start)

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    print(adjacencyList)

    while not queue.isEmpty():
        pop = queue.dequeue()
        for neighbor in adjacencyList[pop]:
            if neighbor not in visitedList:
                queue.enqueue(neighbor)
        visitedList.append(pop)

    print(visitedList)

bfs(graphs, 0)
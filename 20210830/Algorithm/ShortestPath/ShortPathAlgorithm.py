class AdjacencyMatrix:

    def __init__(self, vertex):
        self.adj = [vertex][vertex]
        for i in range(0, len(self.adj)):
            for j in range(0, len(self.adj[i])):
                if i == j:
                    self.adj[i][j] = 0
                else:
                    self.adj[i][j] = 9999

    def addEdge(self, v1, v2, weight):
        self.adj[v1][v2] = weight
        self.adj[v2][v1] = weight

    def deleteEdge(self, v1, v2):
        self.adj[v1][v2] = 9999
        self.adj[v2][v1] = 9999

    def showMatrix(self):
        for i in range(0, len(self.adj)):
            for j in range(0, len(self.adj[i])):
                print(self.adj[i][j], end = '\t')
            print()



adj = AdjacencyMatrix(7)
adj.addEdge(0, 1, 7);
adj.addEdge(0, 4, 3);
adj.addEdge(0, 5, 10);

adj.addEdge(1, 2, 4);
adj.addEdge(1, 3, 10);
adj.addEdge(1, 4, 2);
adj.addEdge(1, 5, 6);

adj.addEdge(2, 3, 2);

adj.addEdge(3, 5, 9);
adj.addEdge(3, 6, 4);

adj.addEdge(4, 6, 5);

adj.showMatrix()
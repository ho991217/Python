# BFS 이용
def solution(n, wires):
    adj = [[] for i in range(n)]

    for wire in wires:
        adj[wire[0] - 1].append(wire[1] - 1)
        adj[wire[1] - 1].append(wire[0] - 1)

    def bfs(adj, start):
        visited = []
        queue = []

        queue.append(start)

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(adj[node])

        return len(visited)

    def detach(adj, wire):
        v1 = wire[0] - 1
        v2 = wire[1] - 1

        adj[v1].remove(v2)
        adj[v2].remove(v1)
        absoluteNum = abs(bfs(adj, v1) - bfs(adj, v2))

        adj[v1].append(v2)
        adj[v2].append(v1)

        return absoluteNum

    return min([detach(adj, i) for i in wires])


# n = 9
# wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

n = 4
wires = [[1, 2], [2, 3], [3, 4]]

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))
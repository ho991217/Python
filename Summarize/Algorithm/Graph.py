# Dict 타입을 이용한 graph 표현

# 정점
VertexList = [1, 2, 3, 4, 5, 6]

# 간선 (튜플 리스트로 표현)
EdgeList = [(1, 2), (1, 3), (2, 1), (2, 4), (2, 6), (3, 1), (3, 5), (4, 2), (5, 3), (6, 2)]       # -> 양방향

# Adjacency Graph
adj = {}

for i in EdgeList:
    n1, n2 = i[0], i[1]

    if n1 not in adj:
        adj[n1] = [n2]
    elif n2 not in adj[n1]:
        adj[n1].append(n2)

    # 양방향이기 때문에 양쪽 추가
    if n2 not in adj:
        adj[n2] = [n1]
    elif n1 not in adj[n2]:
        adj[n2].append(n1)

print(adj)
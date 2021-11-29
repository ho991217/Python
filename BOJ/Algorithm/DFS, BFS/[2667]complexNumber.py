"""
단지번호 붙이기
1 : 집이 있는 곳
0 : 집이 없는 곳

[입력예제]
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

[출력예제]
3   -> 총 단지 수
7   -> 단지내 집 수를 오름차순 정렬
8
9
"""

"""
8
01111011
00110110
00100100
00001000
00011000
00100000
11110000
01100000
"""

"""
mapSize = int(input())
c_map = [[] for i in range(mapSize)]
for i in range(mapSize):
    line = input()
    for j in line:
        c_map[i].append(int(j))

def findComplex(c_map):

    # vertexList 생성
    vertexList = {}
    count = 1
    for i in range(len(c_map)):
        for j in range(len(c_map)):
            vertexList[count] = c_map[i][j]
            count += 1


    # graph 생성
    graph = {}
    for n1 in list(vertexList.keys()):
        for n2 in list(vertexList.keys()):
            if n1 == n2: pass

            minus = n1 - n2
            if (vertexList[n1] == 1 and vertexList[n2] == 1) and (minus == 1 or minus == -1 or minus == 7 or minus == -7 ):
                if n1 not in graph:
                    graph[n1] = [n2]
                elif n2 not in graph[n1]:
                    graph[n1].append(n2)

                if n2 not in graph:
                    graph[n2] = [n1] 
                elif n1 not in graph[n2]:
                    graph[n2].append(n1)

    print(graph)

    # DFS 정의
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

    buildingList = []
    for i in list(vertexList.keys()):
        if vertexList[i] == 1:
            house = DFS(graph, i)
            house.sort()
            print('house : ',house)
            buildingList.append(len(house))

            for j in house:
                vertexList.pop(j, None)

    print(buildingList)

findComplex(c_map)
"""

# 입력단
N = int(input())
complexMap = [[] for _ in range(N)]
for i in range(N):
    line = input()
    for j in line:
        complexMap[i].append(int(j))

# graph 만들기

# 간선 찾기
adj = {}
edgeList = []
def addDict(dict, n1, n2):
    if n1 not in adj:
        adj[n1] = [n2]
    elif n2 not in adj[n1]:
        adj[n1].append(n2)

for i in range(len(complexMap)):
    for j in range(len(complexMap[i])):
        if complexMap[i][j] == 1:
            n1 = 7 * i + j

            if j + 1 < len(complexMap[i]) and complexMap[i][j + 1] == 1:
                    n2 = 7 * i + (j + 1)
                    addDict(adj, n1, n2)

            elif j - 1 >= 0 and complexMap[i][j - 1] == 1:
                    n2 = 7 * i + (j - 1)
                    addDict(adj, n1, n2)

            elif i + 1 < len(complexMap) and complexMap[i + 1][j] == 1:
                    n2 = 7 * (i + 1) + j
                    addDict(adj, n1, n2)

            elif i - 1 >= 0 and complexMap[i - 1][j] == 1:
                    n2 = 7 * (i - 1) + j
                    addDict(adj, n1, n2)


for i in range(N**2):
    if i in adj:
        adj[i].sort()

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


buildings = []
for i in range(len(complexMap)):
    for j in range(len(complexMap[i])):
        if complexMap[i][j] == 1:
            if 7 * i + j not in adj:
                buildings.append(1)

for i in range(len(complexMap)):
    for j in range(len(complexMap[i])):
        if complexMap[i][j] == 1:
            num = 7 * i + j
            if num in adj:
                tmp = DFS(adj, num)
                buildings.append(len(tmp))
                for k in tmp:
                    adj.pop(k)

buildings.sort()
print(len(buildings))
for i in buildings:
    print(i)


def printField(field):
    for x in field:
        for y in x:
            print(y, end= ' ')
        print()

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [0 for i in range(M * N)]

    for __ in range(K):
        x, y = map(int, input().split())
        field[x * N + y] = 1

    graph = [0 for i in range(len(field))]

    for i in range(len(field)):
        if field[i] == 1:
            # 좌측 끝
            if i % N == 0:
                if field[i + 1] == 1:
                    graph[i] = i + 1

            # 우측 끝
            elif i % N == N - 1:
                if field[i - 1] == :
                    graph[i] = i - 1

            # 최상단
            if i < N:
                if field[N * ]

            # 최하단
            elif i >= N * (M - 1):



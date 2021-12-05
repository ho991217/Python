import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [[x + y for x in range(2**N)] for y in range(2**N)]

def printGraph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(graph[i][j], end=' ')
        print()


def search(target, r = 0, c = 0, counter = 0):
    if target == [r, c]: return counter

    for i in range(0, 3):
        if i == 0:
            c += 1
        elif i == 1:
            c -= 1
            r += 1
        else:
            c += 1

        counter += 1
        print(f'[{r}, {c}] counter: {counter}')

        if target == [r, c]: return counter

    return search(target, r, c, counter)



print(search([r, c]))
import sys

M, N = map(int, sys.stdin.readline().split(' '))
dex = dict()

pokemons = []

for i in range(M):
    pokemon = sys.stdin.readline().rstrip()
    dex[pokemon] = i
    pokemons.append(pokemon)

for i in range(N):
    q = sys.stdin.readline().rstrip()
    isNumber = (ord(q[0]) < 60)

    if isNumber:
        print(pokemons[int(q) - 1])
    else:
        print(dex[q] + 1)
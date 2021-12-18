sets = [int(i) for i in input().split()]
com = [1, 1, 2, 2, 2, 8]
for i in range(6):
    sets[i] = com[i] - sets[i]
print(' '.join(str(i) for i in sets))
T = int(input())

for _ in range(T):
    result = [i for i in input()]
    point = 0

    for i in range(len(result)):
        if i == 0:
            combo = 0

        if result[i] == 'O':
            point += 1 + combo
            combo += 1
        else:
            combo = 0

    print(point)

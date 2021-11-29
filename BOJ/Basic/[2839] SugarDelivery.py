from itertools import product

n = int(input())
minimum = [-1]
psb = [[x for x in range(n // 3 + 1)], [y for y in range(n // 5 + 1)]]
for (x, y) in list(product(*psb)):
    if 3 * x + 5 * y == n:
        minimum.append(x + y)

minimum.remove(-1)
if minimum == []:
    print(-1)
else:
    print(min(minimum))
import sys

matrix = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    matrix.append([x, y])

def matrixSort(matrix):
    if len(matrix) <= 1:
        return matrix
    left, mid, right = [], [], []
    pivot = matrix[len(matrix) // 2]

    for el in matrix:
        if el[1] > pivot[1]:
            right.append(el)
        elif el[1] < pivot[1]:
            left.append(el)
        else:
            if el[0] > pivot[0]:
                right.append(el)
            elif el[0] < pivot[0]:
                left.append(el)
            else:
                 mid.append(el)

    return matrixSort(left) + mid + matrixSort(right)

print('\n'.join(str(i) for i in [' '.join([str(x), str(y)]) for x, y in matrixSort(matrix)]))

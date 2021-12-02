import sys

N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    x, y = sys.stdin.readline().rstrip().split(' ')
    matrix.append([int(x), int(y)])

def ss(arr):
    if len(arr) <= 1: return arr

    mid = arr[len(arr) // 2]
    left = []
    pivot = []
    right = []

    for point in arr:
        if point[0] < mid[0]:
            left.append(point)
        elif point[0] > mid[0]:
            right.append(point)
        else:
            if point[1] < mid[1]:
                left.append(point)
            elif point[1] > mid[1]:
                right.append(point)
            else:
                pivot.append(point)

    return ss(left) + pivot + ss(right)

for [x, y] in ss(matrix):
    print(x, y)
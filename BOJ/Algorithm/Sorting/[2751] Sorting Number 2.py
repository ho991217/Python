import sys

N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]

def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, mid, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)

    return quick(left) + mid + quick(right)

for i in quick(numbers):
    print(i)
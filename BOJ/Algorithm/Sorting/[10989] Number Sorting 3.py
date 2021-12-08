import sys

arr = []

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())

    for i in arr:
        if i[0] == n:
            i[1] += 1
            break
    arr.append([n, 1])

print(arr)

# def quick(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# quick(arr)
# for i in arr:
#     print(i)
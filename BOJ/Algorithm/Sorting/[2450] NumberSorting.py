n = int(input())

unsorted = []
for _ in range(n):
    unsorted.append(int(input()))

# Insertion Sorting
def InsertionSorting(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr

print(InsertionSorting(unsorted))
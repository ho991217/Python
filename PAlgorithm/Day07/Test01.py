# bubble 정렬 최적화

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    print(arr)

bubble_sort([1, 2, 3, 4, 5, 6, 7, 8])

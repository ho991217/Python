def BubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def SelectionSort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return  arr


unsorted = [5, 3, 6, 1, 7, 2, 4]
print('unsorted : ', unsorted)
print('BubbleSort : ', BubbleSort(unsorted))
print('SelectionSort : ', SelectionSort(unsorted))

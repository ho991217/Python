import random
import time

# 난수 생성
def genRandNum(size):
    arr = []
    i = 0
    for i in range(0, size):
        n = int(random.randrange(0, size) + 1)

        if n in arr:
            pass
        else:
            arr.append(n)

    return arr

# print(genRandNum(1))

# unsortedArray = genRandNum(20000)
unsortedArray = [x for x in range(10001)]
random.shuffle(unsortedArray)
print('Unsorted Array : ', unsortedArray)
# unsortedArray = [8, 10, 9, 14, 2, 7, 13, 3, 12, 1, 15, 4, 6, 11, 5]

# Select Sort Algorithm
# O(n^2)
def SelectSort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
start = time.time()
print('\nSelect Sort : ', SelectSort(unsortedArray))
print('time : ', time.time() - start)

# Bubble Sort Algorithm
# O(n^2)
def BubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                Swap = True
            if not swap:
                break
        return arr
start = time.time()
print('\nBubble Sort : ', BubbleSort(unsortedArray))
print('time : ', time.time() - start)

# Insert Sort Algorithm
# O(n^2)
def InsertSort(arr):
    for i in range(1, len(arr) - 1, 1):
        swap = False
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        if not swap:
            break
    return arr
start = time.time()
print('\nInsert Sort : ', InsertSort(unsortedArray))
print('time : ', time.time() - start)

# Quick Sort Algorithm
# O(nlogn)

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    left, mid, right = [], [], []
    pivot = arr[len(arr) // 2]

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)

    return QuickSort(left) + mid + QuickSort(right)

start = time.time()
print('\nQuick Sort : ', QuickSort(unsortedArray))
print('time : ', time.time()- start)

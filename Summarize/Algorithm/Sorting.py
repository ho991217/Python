import time
import random

arr = []
while len(arr) < 5:
    randNum = int(random.random() * 5 + 1)
    if randNum not in arr:
        arr.append(randNum)

print(arr, '\n')

# Bubble Sorting : 최선의 경우 = O(n^2), 평균의 경우 = O(n^2), 최악의 경우 = O(n^2)
# 두개씩 비교하면서 Swap하는 방식
def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

start = time.time_ns()
print('Bubble Sort : ', bubble(arr))
end = time.time_ns()
print('Time Took : ', end - start, '\n')


# Selection Sorting : 최선의 경우 = O(n^2), 평균의 경우 = O(n^2), 최악의 경우 = O(n^2)
# 최솟값을 찾아서 앞에서부터 바꾸는 방식
def selection(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

start = time.time_ns()
print('Selection Sort : ', selection(arr))
end = time.time_ns()
print('Time Took : ', end - start, '\n')

# Insertion Sorting : 최선의 경우 = O(n), 평균의 경우 = O(n^2), 최악의 경우 = O(n^2)
# 뒤에서부터 key 값의 위치로 swap
def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

start = time.time_ns()
print('Insertion Sort : ', insertion(arr))
end = time.time_ns()
print('Time Took : ', end - start, '\n')

# Quick Sorting : 최선의 경우 = O(nlog₂n), 평균의 경우 = O(nlog₂n), 최악의 경우 = O(n^2)
# 분할정복기법을 이용하여 pivot보다 작은 수는 앞에, 큰 수는 뒤에 둠
def quick(arr):
    if len(arr) <= 1: return arr

    left = []
    right = []
    pivot = []
    mid = arr[len(arr) // 2]    # 중간값

    for num in arr:
        if num > mid:
            right.append(num)
        elif num < mid:
            left.append(num)
        else:
            pivot.append(num)

    return quick(left) + pivot + quick(right)

start = time.time_ns()
print('Quick Sort : ', quick(arr))
end = time.time_ns()
print('Time Took : ', end - start, '\n')



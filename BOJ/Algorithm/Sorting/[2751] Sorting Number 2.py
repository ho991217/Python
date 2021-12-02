import sys
from collections import deque

N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

# def nRecQsort(arr, size = 5):
#     stack = deque()
#     leftIdx = 0
#     rightIdx = size - 1
#
#     stack.append(rightIdx)
#     stack.append(leftIdx)
#
#
#     while (stack):
#             leftIdx = stack.pop()
#             rightIdx = stack.pop()
#
#             if (rightIdx - leftIdx + 1 > 1):
#                 pivot = arr[rightIdx]
#                 i = leftIdx - 1
#                 j = rightIdx
#
#                 while True:
#                     i += 1
#                     while (arr[i] < pivot):
#                         i += 1
#
#                     j -= 1
#                     while (arr[j] > pivot):
#                         j -= 1
#
#                     if i >= j:
#                         break
#
#                     arr[i], arr[j] = arr[j], arr[i]
#
#
#                 arr[i], arr[rightIdx] = arr[rightIdx], arr[i]
#
#                 stack.append(rightIdx)
#                 stack.append(i + 1)
#                 stack.append(i - 1)
#                 stack.append(leftIdx)
#
#     return arr
#
# numbers = nRecQsort(numbers, N)

for i in numbers:
    print(i)
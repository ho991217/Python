import sys
from collections import deque

N = int(sys.stdin.readline())


numbers = [int(sys.stdin.readline()) for _ in range(N)]

# def merge(arr):
#     if len(arr) <= 1:
#         return arr
#
#     left, right = [], []
#     mid = arr[len(arr) // 2]
#
#     for num in arr:
#         if num <= mid:
#             left.append(num)
#         else:
#             right.append(num)
#
#     return merge(left) + merge(right)






for i in numbers:
    print(i)
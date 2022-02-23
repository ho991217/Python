# import sys
# from collections import deque
#
# K, N = map(int, sys.stdin.readline().split())
#
# if K >= N:
#     print(K - N)
#     exit(0)
#
# def bfs(root, goal):
#     visited = []
#     counter = []
#     nextEl = 0
#     curEl = 1
#     depth = 0
#     q = deque([root])
#
#     while q:
#         cur = q.popleft()
#         curEl -= 1
#
#         if cur == goal:
#             return depth
#
#         if cur not in visited:
#             visited.append(cur)
#             if cur + 1 < goal:
#                 q.append(cur + 1)
#                 nextEl += 1
#             elif cur + 1 == goal:
#                 return depth + 1
#
#             if cur - 1 >= 0 and cur - 1 not in visited and cur - 1 != goal:
#                 q.append(cur - 1)
#                 nextEl += 1
#             elif cur - 1 == goal:
#                 return depth + 1
#
#
#             if cur * 2 <= goal:
#                 q.append(cur * 2)
#                 nextEl += 1
#             elif cur * 2 == goal:
#                 return depth + 1
#
#         if curEl <= 0:
#             curEl = nextEl
#             nextEl = 0
#             depth += 1
#
#     return counter
#
# print(bfs(K, N))
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
# N, K = 5, 17

def bfs(root, target):
    visited = []
    q = deque([[root, 0]])

    while q:
        node = q.popleft()
        data = node[0]
        depth = node[1]

        if data not in visited:
            if data == target:
                return depth

            visited.append(data)

            if data + 1 == target or data - 1 == target or data * 2 == target:
                return depth + 1

            else:
                if data + 1 <= 100000:
                    q.append([data + 1, depth + 1])
                if data - 1 >= 0:
                    q.append([data - 1, depth + 1])
                if data * 2 <= 100000:
                    q.append([data * 2, depth + 1])

print(bfs(N, K))
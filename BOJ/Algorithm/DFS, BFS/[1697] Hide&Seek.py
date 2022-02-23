import sys
from collections import deque

# K, N = map(int, sys.stdin.readline().split())


def bfs(root, goal):
    visited = []
    counter = []
    depth = 0
    q = deque([root])

    while q:
        cur = q.popleft()
        if cur == goal:
            counter.append(depth)

        if not q:
            depth += 1

        if cur not in visited:
            visited.append(cur)
            if cur + 1 <= goal:
                q.append(cur + 1)
            if cur * 2 <= goal:
                q.append(cur * 2)
            if cur - 1 not in visited:
               q.append(cur - 1)

    return counter

bfs(5,17)
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (end + start) // 2
    total = 0
    for treeheight in trees:
        if treeheight >= mid:
            total += treeheight - mid
        if total >= M:
            break

    if total >= M:
        start = mid + 1
    elif total < M:
        end = mid - 1
print(end)
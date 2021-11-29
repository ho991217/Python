import sys

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

left, right = 1, max(lan)

while left <= right:
    mid = (left + right) // 2
    amount = sum(map(lambda x : x // mid, lan))

    if amount >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)

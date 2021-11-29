N = int(input())
A = sorted([int(i) for i in input().split()])
M = int(input())
P = [int(i) for i in input().split()]

def bs(A, num, lft, rght):
    if lft > rght:
        return 0

    mid = (lft + rght) // 2

    if num > A[mid]:
        return bs(A, num, mid + 1, rght)
    elif num < A[mid]:
        return bs(A, num, lft, mid - 1)
    else:
        return 1

for i in P:
    print(bs(A, i, 0, len(A) - 1))
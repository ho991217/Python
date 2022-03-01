import sys

A, B, C = map(int, sys.stdin.readline().split())

def pow(A, B, C):
    if B == 0:
        return 1
    tmp = pow(A, B // 2, C)
    tmp = tmp * tmp % C
    if B % 2 == 0:
        return tmp
    return A * tmp % C

print(pow(A, B, C))
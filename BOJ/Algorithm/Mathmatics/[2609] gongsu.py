import sys

def GCD(A, B):
    if A%B == 0: return B
    else: return GCD(B, A%B)


def LCM(A, B):
    return (A * B) // GCD(A, B)

A, B = map(int, sys.stdin.readline().rstrip().split(' '))

print(GCD(A, B))
print(LCM(A, B))
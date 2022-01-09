import sys

T = int(sys.stdin.readline().rstrip())

def fact(n):
    if n <= 1: return 1
    return n * fact(n-1)

def combi(n, k):
    return (fact(n)) // (fact(k) * fact(n-k))

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split(' '))
    print(combi(M,N))
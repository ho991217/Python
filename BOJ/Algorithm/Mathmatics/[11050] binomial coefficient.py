import sys

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

if 0 <= K and K <= N:
    print(fact(N) // (fact(K) * fact(N - K)))
else:
    print(0)



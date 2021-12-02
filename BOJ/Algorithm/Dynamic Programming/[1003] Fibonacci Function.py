import sys

T = int(sys.stdin.readline().rstrip())
nums = (int(input()) for _ in range(T))

cache = [0, 1]

def fib(n):
    if n == 0:
        return 0
    elif n <= 1:
        return 1
    else:
        if len(cache) > n:
            return cache[n]
        else:
            newFib = fib(n - 1) + fib(n - 2)
            cache.append(newFib)
            return newFib

for n in nums:
    print(fib(n - 1), fib(n))

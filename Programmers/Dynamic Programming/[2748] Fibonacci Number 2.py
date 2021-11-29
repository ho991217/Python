"""def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 2) + fibonacci(n - 1)
print(fibonacci(int(input())))"""
# recursive로 풀게되면 시간초과가 뜸

def fibonacci(cache, n):
    if n == 1:
        cache[n] = 1
        return 1
    elif n == 0:
        cache[n] = 0
        return 0
    if cache[n] == -1:
        cache[n] = fibonacci(cache, n - 1) + fibonacci(cache, n - 2)
    return cache[n]

n = int(input())
cache = [-1 for _ in range(n + 1)]
print(fibonacci(cache, n))
# 3 ~ n 까지의 곱

# 재귀함수 사용 - 1번
# 재귀함수 미사용 - 2번

def func1(n):
    if n == 3:
        return n
    else:
        return n * func1(n - 1)

def func2(n):
    for i in range(3, n):
        n *= i
    return n

print(func1(5))
print(func2(5))
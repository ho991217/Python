# 시간복잡도
# - 알고리즘 문제를 해결하기 위한 시간(연산)의 횟수를 말한다.
# - 알고리즘을 평가하는데 있어 수행시간과 메모리 사용량을 평가 기준으로 나누는데
# 수행시간에 해당되는것이 시간 복잡도
# 메모리 사용량에 해당되는 것이 공간복잡도

# 연산 횟수를 카운팅 할 때 3가지의 경우
# 1. 최선의 경우 - Best Case
# 2. 최악의 경우 - Worst Case
# 3. 평균적인 경우 - Average Case

# 시간 복잡도는 주로 Big-O 표기법으로 나타낸다

# 산술연산 + - * / - 0(1) 즉각 결과가 나타나는것
# 길이가 n 만큼인 리스트를 처음부터 끝까지 요소를 출력
# print를 n만큼 쓰기 때문에 O(n)
# 이중 for문 O(n^2)
# 삼중 for문 O(n^3)

# 복잡한 정도
# O(1) < O(log(n)) < O(nlog(n)) < O(n^2) ... < O(n^n)

# 1 부터 n 까지 합을 구하는 알고리즘

def sum(n):     # 시간복잡도 O(n)
    total = 0
    for i in range (n + 1):
        total += i
    return total
print(sum(100))
# 덧셈을 n번 반복하기 때문에 O(n)

def sum1(n):    # O(1)
    return int(n * (n + 1) / 2)

print(sum1(100))
# 입력이 n 이어도 곱셈/ 나눗셈/ 덧셈하면 되기 때문에 시간 복잡도는 O(1)
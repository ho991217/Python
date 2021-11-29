class Number:
    n = 0
    def __init__(self, n):
        self.n = n

    def __lt__(self, other):
        return self.n < other.n

    def __le__(self, other):
        return self.n <= other.n

    def __gt__(self, other):
        return self.n > other.n

    def __ge__(self, other):
        return self.n >= other.n

    def __eq__(self, other):
        return self.m == other.n

n1 = Number(3)
n2 = Number(4)

print(n1.__lt__(n2))
print(n1 < n2)  # 파이썬에서 객체안의 값들의 비교를 알아서 연산자를 불러온다.


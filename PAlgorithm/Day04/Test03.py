# class Info:
#     def disp(self, name):
#         print(self.name)
#
#     def disp(self, name, age):
#         print(self.name, self.age)
#
# info = Info()
# info.disp("홍길동", 20)

# 파이썬 - 오버로딩 불가능

class Number:
    n = 0
    def __init__(self, n):
        self.n = n

    def __add__(self, n1, n2):
        return (n1 + n2) * 100

    def __더하기__ (self, n1, n2):
        return n1 + n2

a = 10
print(a.__add__(3))
number = Number(5)
print(number.__add__(a, 3))
print(number.__더하기__(1, 2))

# 연산자의 오버로딩



# 오버로딩가능한 연산자 메소드 종류
# __add__(self, other) : ( A + B )
# __sub__(self, other) : ( A - B )
# __mul__(self, other) : ( A * B )
# __truediv__(self, other) : ( A / B )
# __floordiv__(self, other) : ( A // B )
# __mod__(self, other) : ( A % B )


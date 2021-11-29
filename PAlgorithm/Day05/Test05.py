# 정적 메소드 (@classmethod @staticmethod)

# - 클래스에서 직접 접근할 수 있는 메소드
# - 파이썬에서는 다른 언어와 다르게 정적 메소드 임에도 불구하고 인스턴스(객체)에서도 접근이 가능함

class Test:
    def instance_method(self, a, b):
        return a + b

    @classmethod
    def class_method(cls, a, b):
        return a + b

    @staticmethod
    def static_method(a, b):
        return a + b



a = Test.class_method(1, 2)         # 객체를 만들지 않아도 사용 가능

# b = Test.instance_method(1, 2)    # 객체를 만들어야 사용 가능
t = Test()
b = t.instance_method(1, 2)

c = Test.static_method(1, 2)        # 정적 메소드

print(a)
print(b)
print(c)



class Language:
    la = "English"

    def __init__(self):
        self.show = "나의 언어는 " + self.la

    @staticmethod
    def static_language():
        return Language()

    @classmethod
    def class_language(cls):
        return cls()

    def print_language(self):
        print(self.show)

class Korean(Language):
    la = "힌국어"

a = Korean.static_language()
b = Korean.class_language()
a.print_language()
b.print_language()
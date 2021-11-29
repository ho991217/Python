# 추상클래스
# abc 모듈을 import 해야 사용 하능
# - 미구현 추상 메소드를 한개 이상 가지며, 자식 클래스에 해당 메소드를 반드시 구현해야함

from abc import *

class Test(metaclass = ABCMeta):
    @abstractmethod
    def disp(self):
        pass

class Test1(Test):
    name = "홍길동"

    def getName(self):
        return self.name

    def disp(self):
        print(self.name)

a = Test1()
print(a.getName())
a.disp()
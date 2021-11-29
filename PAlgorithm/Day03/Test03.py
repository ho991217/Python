# 클래스 구성 요소
# 1) 멤버필드
# 2) 메소드 (함수)

# 기존 함수와의 차이점(메소드 특징)
# 1) 매개변수 자리에 항상 self를 추가해야 한다
# 2) 메소드 밖에서 선언한 변수 사용시, 변수 명 앞에 self.를 붙여준다

# def func():
#     print('함수 호출')
#
# func()

class Test():
    num = 0 # -> 클래스 멤버필드 -> 클래스 영역
    def func(self, num): # 클래스 메소드
        self.num = 10 # self. -> 클래스 안에 있는 변수(멤버 필드)
        print('메소드 호출')

t = Test()
# print(f'num = {t.num}')
print(f'number = {t.num}')
t.func(10)
print(f'num = {t.num}')
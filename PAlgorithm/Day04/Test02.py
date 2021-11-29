# 생성자
# - 객체가 생성이 될 때, 무조건 처음으로 실행되며, 한번은 실행되는 메소드

class Info:
    name = ""
    age = 0
    def __init__(self,name , age):
        self.name = name
        self.age = age
        print('생성자 입니다.')

    def showData(self):
        print("이름 : {}".format(self.name))
        print("나이 : {}".format(self.age))

info = Info("홍길동", 20)
info.showData()
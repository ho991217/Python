# 클래스 정의
# 1) class : 키워드
# 2) Student : 클래스 이름
# 3) 들여쓰기 : 클래스 안의 종속문장

# 클래스 사용법
# 1) 변수명 = Student() -> 사용자 정의 클래스만의 객체

class Student:
    # 멤버 필드
    name = ""
    hakbun = 0
    score = 0


st1 = Student()

st1.name = "홍키"
st1.hakbun = 32183741
st1.score = 86

print(st1.name)
print(st1.hakbun)
print(st1.score)

st2 = Student()
st2.name = "이호연"
st2.hakbun = 10002
st2.score = 99

print(st2.name)
print(st2.hakbun)
print(st2.score)
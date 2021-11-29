# 상속
class Country:
    # 부모 클래스
    name = "국가명"
    population = "인구"
    capital = "수도"

    def show(self):
        print("국가 클래스의 메소드 입니다,")

class Korea(Country):
    # 자식 클래스
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("국가 이름은 ", self.name)

kor = Korea("대한민국")
kor.show()
kor.show_name()

print(kor.name)
print(kor.population)
print(kor.capital)
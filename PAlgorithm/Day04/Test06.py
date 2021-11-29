#
class Country:
    # 부모 클래스
    name = "국가명"
    population = "인구"
    capital = "수도"

    def __init__(self):
        print("부모 생성자")

    def show(self):
        print("국가 클래스의 메소드 입니다.")


class Korea(Country):
    def __init__(self, name, population, capital):
        super().__init__() # super를 이용하면 부모클래스의 메소드를 접할 수 있다.
        print("자식생성자")
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print("""
국가 이름은 {} 입니다.
국가 인구는 {} 입니다.
국가 수도는 {} 입니다.
        """.format(self.name, self.population, self.capital))

kor = Korea("대한민국", 50000000, "서울")
kor.show()
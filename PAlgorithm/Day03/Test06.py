# 구성 항목 - id, atk, hp, target(객체)

#   id      atk     hp      target
#   뽀로로    10      100     타요
#   타요     15      80       뽀로로

# 뽀로로와 타요 객체 생성 후 정보 출력한 뒤
# 서로 2번싞 구현ㅇ하면 어떻게 되는데

class Monster:
    def __init__(self, id, atk, hp):
        self.id = id
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        target.hp = target.hp - self.atk

    def showStatus(self):
        print('{}\t{}\t{}\t'.format(self.id, self.atk, self.hp))

pororo = Monster("뽀로로", 10, 100)
tayo = Monster("타요", 15, 80)

for i in range(2):
    pororo.attack(tayo)
    tayo.attack(pororo)

pororo.showStatus()
tayo.showStatus()

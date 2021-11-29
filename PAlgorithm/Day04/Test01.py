class Player:
    userId = ""
    atk = 0
    hp = 0
    target = None

    def __init__(self, userId, atk, hp):
        self.userId = userId
        self.atk = atk
        self.hp = hp

    # def setData(self, userId, atk, hp):
    #     self.userId = userId
    #     self.atk = atk
    #     self.hp = hp

    def setTarget(self, target):
        self.target = target

    def attack(self):
        self.target.hp -= self.atk

    def disp(self):
        print(self.userId, self.atk, self.hp, self.target.userId, sep="\t")

p1 = Player("뽀로로", 10, 100)
p2 = Player("타요", 15, 80)


p1.setTarget(p2)
p2.setTarget(p1)

p1.attack()
p2.attack()

p1.disp()
p2.disp()
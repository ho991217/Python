class SharpPencil:
    width = 0  # 펜의 굵기
    amount = 0  # 남은 수량

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount


class Ballpen:
    amount = 0  # 남은 수량
    color = ""  # 볼펜의 색

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


class FontainPen:
    amount = 0  # 남은 수량
    color = ""  # 색

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def refill(self, n):
        self.setAmount(n)






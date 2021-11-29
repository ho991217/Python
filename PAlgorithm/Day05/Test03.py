class Pen:
    amount = 0

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount


class SharpPencil(Pen):
    width = 0  # 펜의 굵기

class Ballpen(Pen):
    color = ""  # 볼펜의 색

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

class FontainPen(Ballpen):

    def refill(self, n):
        super().setAmount(n)





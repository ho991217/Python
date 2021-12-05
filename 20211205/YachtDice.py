import random


class Dice:
    def __init__(self):
        self.dice = [1, 2, 3, 4, 5, 6]
        self.curDice = self.dice[int(random.random() * 6)]

    def roll(self):
        self.curDice = self.dice[int(random.random() * 6)]

    def getDice(self):
        return self.curDice

    def setDice(self, num):
        self.curDice = num


class DiceSet:
    def __init__(self):
        self.dices = []
        self.d1 = Dice()
        self.dices.append(self.d1)
        self.d2 = Dice()
        self.dices.append(self.d2)
        self.d3 = Dice()
        self.dices.append(self.d3)
        self.d4 = Dice()
        self.dices.append(self.d4)
        self.d5 = Dice()
        self.dices.append(self.d5)


    def roll(self, select=[True, True, True, True, True]):
        for i in range(0, 5):
            if select[i] == True:
                self.dices[i].roll()
            else:
                pass

        return self.dices

    def showDices(self):
        for dice in self.dices:
            print(dice.getDice(), end=' ')
        print()

    def getDices(self):
        return self.dices

    def debugDice(self, arr):
        counter = 0
        for i in self.dices:
            i.setDice(arr[counter])
            counter += 1


class scoreBoard():
    def __init__(self):
        self.playerScore = [0 for _ in range(14)]
        self.scoreBoard = [0 for _ in range(14)]
        """
        index별 점수:
        0: 에이스
        1: 투
        2: 쓰리
        3: 포
        4: 파이브
        5: 식스
        6: 보너스(+35)
        7: X3
        8: X4
        9: 풀하우스
        10: 스몰스트레이트
        11: 라지스트레이트
        12: 조커
        13: 야추
        """

    def eval(self, diceSet):
        di = []
        for dice in diceSet:
            di.append(dice.getDice())

        # 1부터 6까지
        self.scoreBoard[0] = di.count(1)
        self.scoreBoard[1] = di.count(2)
        self.scoreBoard[2] = di.count(3)
        self.scoreBoard[3] = di.count(4)
        self.scoreBoard[4] = di.count(5)
        self.scoreBoard[5] = di.count(6)
        # bonus
        self.scoreBoard[6] = 35 if self.scoreBoard[0] + self.scoreBoard[1] + self.scoreBoard[2] + self.scoreBoard[3] + self.scoreBoard[4] + self.scoreBoard[5] >= 63 else 0

        tmp = dict()
        for d in di:
            if d in tmp:
                tmp[d] += 1
            else:
                tmp[d] = 1
        tmp = list(tmp.values())

        # 중복 3개
        if 3 in tmp: self.scoreBoard[7] = sum(di)
        # 중복 4개
        if 4 in tmp: self.scoreBoard[8] = sum(di)
        # 풀하우스
        if (tmp == [2, 3] or tmp == [3, 2]):
            self.scoreBoard[9] = 25
        else:
            self.scoreBoard[9] = 0
        # 스몰스트레이트
        if (1 in di and 2 in di and 3 in di and 4 in di) or (2 in di and 3 in di and 4 in di and 5 in di) or ( 3 in di and 4 in di and 5 in di and 6 in di):
            self.scoreBoard[10] = 30
        else:
            self.scoreBoard[10] = 0
        #라지스트레이트
        if (1 in di and 2 in di and 3 in di and 4 in di and 5 in di) or (2 in di and 3 in di and 4 in di and 5 in di and 6 in di):
            self.scoreBoard[11] = 40
        else:
            self.scoreBoard[11] = 0
        #조커
        self.scoreBoard[12] = sum(di)

        # 야추
        if (len(set(di)) == 1): self.scoreBoard[13] = 50
        else: self.scoreBoard[13] = 0

    def setScore(self, index = 0):
        self.playerScore = self.scoreBoard

    def showCurPlayerScore(self):
        print(f'1: {self.playerScore[0]}')
        print(f'2: {self.playerScore[1]}')
        print(f'3: {self.playerScore[2]}')
        print(f'4: {self.playerScore[3]}')
        print(f'5: {self.playerScore[4]}')
        print(f'6: {self.playerScore[5]}')
        print(f'Bonus: {self.playerScore[6]}')
        print(f'X3: {self.playerScore[7]}')
        print(f'X4: {self.playerScore[8]}')
        print(f'Full House: {self.playerScore[9]}')
        print(f'Small Straight: {self.playerScore[10]}')
        print(f'Large Straight: {self.playerScore[11]}')
        print(f'Joker: {self.playerScore[12]}')
        print(f'Yacht: {self.playerScore[13]}')


#
a = DiceSet()
a.debugDice([1, 1, 1, 2, 2])
s = scoreBoard()
s.eval(a.getDices())
s.setScore()
s.showCurPlayerScore()

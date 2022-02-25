import sys

class DoubleQueue:
    def __init__(self):
        self.doubleQueue = dict()

    def add(self, value):
        if value in self.doubleQueue:
            self.doubleQueue[value] += 1
        else:
            self.doubleQueue[value] = 1

    def delMax(self):
        if not self.isEmpty():
            maxNumber = self.max()
            if self.doubleQueue[maxNumber] >= 2:
                self.doubleQueue[maxNumber] -= 1
            else:
                self.doubleQueue.pop(maxNumber)

    def delMin(self):
        if not self.isEmpty():
            minNumber = self.min()
            if self.doubleQueue[minNumber] >= 2:
                self.doubleQueue[minNumber] -= 1
            else:
                self.doubleQueue.pop(minNumber)

    def isEmpty(self):
        return list(self.doubleQueue.keys()) == []

    def max(self):
        return max(list(self.doubleQueue.keys()))

    def min(self):
        return min(list(self.doubleQueue.keys()))


T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    dq = DoubleQueue()

    for i in range(k):
        command, number = sys.stdin.readline().rstrip().split(' ')
        number = int(number)

        if command == 'I':
            dq.add(number)
        elif command == 'D':
            if number == 1:
                dq.delMax()
            elif number == -1:
                dq.delMin()

    if dq.isEmpty():
        print('EMPTY')
    else:
        print(dq.max(), end=' ')
        print(dq.min())






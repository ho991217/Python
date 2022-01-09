#
#
# class minecraft:
#     def __init__(self, N, M, inven, cursec = 0):
#         self.ground = [[int(j) for j in input().split()] for _ in range(N)]
#         self.inven = inven
#         self.cursec = cursec
#
#     def getGround(self):
#         return self.ground
#
#     def getInven(self):
#         return self.inven
#
#     def getSec(self):
#         return self.cursec
#
#     def canPick(self, i, j):
#         if 0 < self.ground[i][j]:
#             return True
#         return False
#
#     def canPut(self, i, j):
#         if (self.ground[i][j] < 256) and (self.inven > 0):
#             return True
#         return False
#
#     def pick(self, i, j):
#         if self.canPick(i, j):
#             self.ground[i][j] -= 1
#             self.inven += 1
#             self.cursec += 1
#         return False
#
#     def put(self, i ,j):
#         if self.canPut(i, j):
#             self.inven -= 1
#             self.ground[i][j] += 1
#             self.cursec += 2
#         return False
#
#     def isFlat(self):
#         if all(pix == self.ground[0][0] for pix in self.ground):
#             return True
#         return False
#
#     def avg(self):
#         return sum([sum(i) for i in self.ground]) // (len(self.ground) * len(self.ground[0]))
#
#
# N, M, B = map(int, input().split())
# m = minecraft(N, M, B)
#
# print(m.getGround())
# print('inven : ', m.inven)
# print('sec :', m.cursec)
# print(m.avg())
import sys

class Minecraft:
    def __init__(self, ground, inven):
        self.ground = ground
        self.time = 0
        self.inven = inven

    def pick(self, x, y):
        if self.ground[x][y] > 0:
            self.ground[x][y] -= 1
            self.time += 2
            self.inven += 1
            return True
        else:
            return False

    def put(self, x, y):
        if self.ground[x][y] < 256 and self.inven > 0:
            self.ground[x][y] += 1
            self.time += 1
            self.inven -= 1
            return True
        else:
             return False

    def analyze(self):
        # True 라면 채우기, False 라면 빼기
        avrg = (len(self.ground[0]) * len(self.ground)) // sum([sum(i) for i in self.ground])
        # case 1: add blocks





N, M, B = map(int, sys.stdin.readline().rstrip().split(' '))
ground = [[int(x) for x in sys.stdin.readline().rstrip().split(' ')] for _ in range(N)]
for i in ground:
    print(''.join(str(j) for j in i))
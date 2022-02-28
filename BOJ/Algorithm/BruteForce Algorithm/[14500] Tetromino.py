import sys

class Tetromino:
    def __init__(self, board, col, row):
        self.board = board
        self.row = row
        self.col = col
        self.maxSum = -1
        self.everything = [
            [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
            [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
            [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
            [(0, 0), (0, 1), (0, 2), (1, 0)],
            [(1, 0), (1, 1), (1, 2), (0, 2)],
            [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
            [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
            [(0, 0), (1, 0), (2, 0), (2, 1)],
            [(2, 0), (2, 1), (1, 1), (0, 1)],
            [(0, 0), (0, 1), (1, 0), (2, 0)],
            [(0, 0), (0, 1), (1, 1), (2, 1)],
            [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
            [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
            [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
            [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
            [(1, 0), (2, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (1, 1), (2, 1)],
            [(1, 0), (0, 1), (1, 1), (0, 2)],
            [(0, 0), (0, 1), (1, 1), (1, 2)]
        ]

    def get(self, x, y):
        for i in range(19):
            tmp = 0
            for j in range(4):
                try:
                    next_x = x + self.everything[i][j][0]
                    next_y = y + self.everything[i][j][1]
                    tmp += self.board[next_x][next_y]
                except IndexError:
                    continue
            self.maxSum = max(self.maxSum, tmp)

    def solve(self):
        for i in range(self.col):
            for j in range(self.row):
                self.get(i, j)
        return self.maxSum


N, M = map(int, sys.stdin.readline().rstrip().split(' '))

board = [[int(i) for i in sys.stdin.readline().rstrip().split(' ')] for j in range(N)]

t = Tetromino(board, N, M)
print(t.solve())
# import sys
# import numpy as np
#
# N, M = map(int, sys.stdin.readline().rstrip().split(' '))
#
# chess = []
# for i in range(N):
#     chess.append([i for i in sys.stdin.readline().rstrip()])
#
# a = np.array(chess)
#
# def ev(board):
#     counterB = 0
#     # B 로 시작 할 경우
#     for i in range(8):
#         for j in range(8):
#             if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)) and board[i][j] == 'W':
#                 counterB += 1
#             if ((i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0)) and board[i][j] == 'B':
#                 counterB += 1
#     counterW = 0
#     # W 로 시작 할 경우
#     for i in range(8):
#         for j in range(8):
#             if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)) and board[i][j] == 'B':
#                 counterW += 1
#             if ((i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0)) and board[i][j] == 'W':
#                 counterW += 1
#
#     return min(counterB, counterW)
#
#
# minCounter = 0
# for i in range(N - 7):
#     for j in range(M - 7):
#         tmp = ev(a[i:i+8, j:j+8])
#         if i == 0 and j == 0:
#             minCounter = tmp
#         elif tmp < minCounter:
#             minCounter = tmp
#
# print(minCounter)

# 백준은 numpy 미지원 -----------------------------------------

import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

chess = []
for i in range(N):
    chess.append([i for i in sys.stdin.readline().rstrip()])

def ev(board):
    counterB = 0
    # B 로 시작 할 경우
    for i in range(8):
        for j in range(8):
            if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)) and board[i][j] == 'W':
                counterB += 1
            if ((i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0)) and board[i][j] == 'B':
                counterB += 1
    counterW = 0
    # W 로 시작 할 경우
    for i in range(8):
        for j in range(8):
            if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)) and board[i][j] == 'B':
                counterW += 1
            if ((i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0)) and board[i][j] == 'W':
                counterW += 1

    return min(counterB, counterW)


minCounter = 0
for i in range(N - 7):
    for j in range(M - 7):
        tmpArr = []
        for k in range(i, i + 8):
            tmpArr.append(chess[k][j:j+8])
        tmp = ev(tmpArr)
        if i == 0 and j == 0:
            minCounter = tmp
        elif tmp < minCounter:
            minCounter = tmp

print(minCounter)
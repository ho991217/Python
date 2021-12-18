# import math
# import sys
#
# # + 또는 - 버튼 만 눌러서 이동하는 경우
# # 숫자 입력후 +, - 입력해서 이동 하는 경우
#
# target = int(sys.stdin.readline().rstrip())
# M = int(sys.stdin.readline().rstrip())
# if M == 0:
#     print(len(str(target)))
#     exit(1)
# brknBtn = list(map(int, sys.stdin.readline().rstrip().split(' ')))
# channel = 100
#
# def clickMove(target):
#     return int(math.fabs(target - 100))
#
# def typeMove(target, brknBtn):
#     counter = 0
#     upper, lower = target, target
#     while True:
#         raised = False
#         downed = False
#         for i in brknBtn:
#             if str(i) in str(upper):
#                 upper += 1
#                 raised = True
#                 break
#
#         for i in brknBtn:
#             if str(i) in str(lower):
#                 lower -= 1
#                 downed = True
#                 break
#
#         if not raised:
#             return len(str(upper)) + counter
#         elif not downed:
#             return len(str(lower)) + counter
#
#         counter += 1
#
#
# print(min(clickMove(target), typeMove(target, brknBtn)))
import sys

target = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
if M == 0:
    print(len(str(target)))
    exit(1)
numbers = [i for i in range(10)]
brknBtn = list(map(int, sys.stdin.readline().rstrip().split(' ')))
for i in brknBtn:
    numbers.remove(i)

closest = [0 for _ in range(len(target))]
for i in range(len(target)):
    for j in range(len(numbers)):
        closest[i] = j
        if j == 0:
            tmpNumber = int(''.join(closest))
        if target - int(''.join(closest)) < target - tmpNumber:
            tmpNumber = int(''.join(closest))
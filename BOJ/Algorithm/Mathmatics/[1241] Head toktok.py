# import sys
#
# students = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
#
# answer = []
# cache = dict()
# for i in range(len(students)):
#     me = students[i]
#     if me == 1:
#         answer.append('0')
#         continue
#     if me in cache:
#         answer.append(str(cache[me]))
#         continue
#
#     arr_without_me = students[:]
#     arr_without_me.pop(i)
#
#     counter = 0
#
#     for other in arr_without_me:
#         if me >= other and me % other == 0:
#             counter += 1
#
#     answer.append(str(counter))
#     cache[me] = counter
#
# print('\n'.join(answer))
# 시간초과 나오는 코드
# import sys
#
# N = int(sys.stdin.readline())
# students = [sys.stdin.readline() for _ in range(N)]
# matrix = [0 for _ in range(max(students) + 1)]
# for num in students:
#     matrix[num] += 1
# 어캐하누..

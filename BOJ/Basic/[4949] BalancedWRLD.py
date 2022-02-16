# lines = []
# answer = []
#
# while True:
#     inp = input()
#     if inp == ".":
#         break
#     lines.append(inp)
#
# for line in lines:
#     stack = []
#     entered = False
#
#     for word in line:
#         if word == "[" or word == "(":
#             stack.append(word)
#
#         if word == "]":
#             if stack == []:
#                 answer.append("no")
#                 entered = True
#
#             elif stack[-1] == "[":
#                 stack.pop()
#
#         elif word == ")":
#             if stack == []:
#                 answer.append("no")
#                 entered = True
#             elif stack[-1] == "(":
#                 stack.pop()
#
#         # if word == ".":
#         #     break
#
#     if not entered:
#         if stack == []:
#             answer.append("yes")
#         else:
#             answer.append("no")
#
#
# for i in range(len(answer)):
#     print(answer[i], end="")
#     if i < len(answer) - 1:
#         print()

import sys

p_dict = {')': '(', ']': '['}

while True:
    s = list(str(sys.stdin.readline()[:-1]))
    if s == ['.']:
        break

    stack = []
    for w in s:
        if w == '(' or w == '[':
            stack.append(w)
        elif w == ')' or w == ']':
            if len(stack) == 0 or stack.pop() != p_dict[w]:
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
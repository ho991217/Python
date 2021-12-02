# 스택 사용, '('가 들어오면 push, ')'가 들어오면 pop. 명령어가 끝났을때 isEmpty(stack) 이 false 이면 NO

import sys

def isVPS(parenthesis):
    stack = []
    for par in parenthesis:
        if par == '(':
            stack.append(par)
        elif par == ')' and stack != []:
            stack.pop()
        elif par == ')' and stack == []:
            return False

    if stack != []:
        return False
    else:
        return True


for _ in range(int(sys.stdin.readline().rstrip())):
    if isVPS(sys.stdin.readline().rstrip()):
        print('YES')
    else:
        print('NO')

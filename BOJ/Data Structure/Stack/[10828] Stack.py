import sys

line = int(input())
stack = []
commands = []
for i in range(line):
    commands.append(sys.stdin.readline().split())

for i in commands:

    if i[0] == 'push':
        stack.append(int(i[1]))

    elif i[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[len(stack) - 1])

    elif i[0] == 'size':
        print(len(stack))

    elif i[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())

    elif i[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)


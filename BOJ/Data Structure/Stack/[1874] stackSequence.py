import sys

stack = []
calulate = []
counter = 1

for i in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())
    while counter <= number:
        stack.append(counter)
        calulate.append('+')
        counter += 1

    if stack[-1] == number:
        stack.pop()
        calulate.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(calulate))
import sys

s = []
command = ''
n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]
number = [i for i in range(n, 0, -1)]

while True:
    if not s:
        s.append(number.pop())
        command += '+\n'

    else:
        if s[-1] < sequence[0]:
            s.append(number.pop())
            command += '+\n'

        elif s[-1] == sequence[0]:
            s.pop()
            command += '-\n'

        else:
            print('NO')
            exit(0)

print(command, end='')

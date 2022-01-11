import sys

T = int(sys.stdin.readline())

for _ in  range(T):
    k = int(sys.stdin.readline())
    cmd = [list(sys.stdin.readline().split()) for _ in range(k)]

    queue = []

    for command in cmd:
        if command[0] == 'I':
            maxV = max(queue)
            minV = min(queue)
            if queue == []:
                queue.append(command[1])
            else:
                if maxV == minV:
                    if maxV < command[1]:
                        queue.append(command[1])
                    else:
                        queue.insert(0, command[1])

                else:
                    if maxV <= command[1]:
                        queue.append(command[1])
                    elif minV <= command[1] and maxV >= command[1]:
                        queue.insert(1)

        elif command[0] == 'D':
            queue.sort()
            if queue != []:
                if command[1] == 1:
                    queue.pop()
                else:
                    queue.pop(0)

        print(queue)

    if queue == []:
        print('EMPTY')
    else:
        print(min(queue), max(queue))
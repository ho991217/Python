import sys

commands = [sys.stdin.readline().rstrip() for i in range(int(sys.stdin.readline().rstrip()))]
for i in range(len(commands)):
    if commands[i][1] == "u":
        commands[i] = commands[i].split(' ')

class deque:
    def __init__(self):
        self.deque = []

    def append(self, value, fOrB):
        if fOrB == 'push_front':
            self.deque.insert(0, value)
        elif fOrB == 'push_back':
            self.deque.append(value)

    def front(self):
        if self.deque == []: print(-1)
        else: print(self.deque[0])

    def back(self):
        if self.deque == []: print(-1)
        else: print(self.deque[-1])

    def size(self):
        print(len(self.deque))

    def empty(self):
        if self.deque == []:
            print(1)
        else:
            print(0)

    def pop_front(self):
        if self.deque == []: print(-1)
        else: print(self.deque.pop(0))

    def pop_back(self):
        if self.deque == []:print(-1)
        else: print(self.deque.pop())


dq = deque()

for command in commands:
    if command[0] == 'push_back' or command[0] == 'push_front':
        dq.append(command[1], command[0])

    else:
        eval(f'dq.{command}()')
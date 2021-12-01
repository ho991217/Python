import sys
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, X):
        self.queue.insert(0, X)

    def pop(self):
        if self.empty(): return -1
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        return self.queue == []

    def front(self):
        if self.empty(): return -1
        return self.queue[len(self.queue) - 1]

    def back(self):
        if self.empty(): return -1
        return self.queue[0]

q = Queue()
T = int(sys.stdin.readline().rstrip())
cmd = [sys.stdin.readline().rstrip() for _ in range(T)]
for i in range(len(cmd)):
    if 'push' in cmd[i]:
        cmd[i] = cmd[i].split(' ')


for command in cmd:
    if command[0] == 'push':
        q.push(int(command[1]))
    elif command == 'front':
        print(q.front())
    elif command == 'back':
        print(q.back())
    elif command == 'empty':
        print(int(q.empty()))
    elif command == 'pop':
        print(q.pop())
    elif command == 'size':
        print(q.size())
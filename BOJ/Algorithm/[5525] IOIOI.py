import sys

class Queue:
    def __init__(self):
        self.q = []

    def push(self, data):
        self.q.append(data)

    def flush(self):
        self.q = []

    def peek(self):
        return self.q[-1]

    def isEmpty(self):
        return self.q == []

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = [i for i in sys.stdin.readline().rstrip()]
q = Queue()

counter = 0

for el in S:
    if el =='I':
        # 큐가 비어있는 경우
        if q.isEmpty():
            q.push(el)

        else:
            # 마지막이
            if q.peek() == 'O':


    # 큐에 뭔가가 있는 경우
    else:
        if el == 'I' and q.
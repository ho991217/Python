# LinearQueue

class LinearQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
         self.data.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            return None
        self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def is_empty(self):
        return self.data == []

    def print_Queue(self):
        print(self.data)

LQ = LinearQueue()
for i in range(1, 11):
    LQ.enqueue(i)
LQ.print_Queue()
LQ.dequeue()
LQ.print_Queue()

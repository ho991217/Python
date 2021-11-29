# Queue
# FIF (First In First Out)

# 가장 먼저 쌓인 데이터가 가장 먼저 처리된다

# 값 넣는 함수
# enqueue

# 값 삭제
# dequeue

# 공간이 비어있는지 확인
# is_empty

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.insert(0, data)

    def dequeue(self):
        self.data.pop()

    def print_queue(self):
        print(self.data)

    def is_empty(self):
        return self.data == []


q = Queue()
for i in range(1,11):
    q.enqueue(i)
q.print_queue()
q.dequeue()
q.print_queue()
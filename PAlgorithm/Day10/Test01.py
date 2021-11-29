class Stack:
    def __init__(self):
        self.data = []
        self.max = 6

    def push(self, data):
        if len(self.data) < self.max:
            self.data.append(data)
        else:
            print('StackOverflow!')

    def pop(self):
        if len(self.data) > 0:
            self.data.pop()
        else:
            print('StackUnderflow')

    def peek(self):
        if not self.is_empty():
            return self.data
        else:
            print('Stack에 데이터가 없습니다.')

    def is_empty(self):
        return self.data == []

    def print_Stack(self):
        print(self.data)


def match(string):
    s = Stack()
    for i in string:
        if i == '(':
            s.push(i)

    for i in string:
        if s.is_empty():
            return False
        elif i ==')':
            s.pop()

    if s.is_empty():
        return True
    else:
        return False

print(match('(()))'))
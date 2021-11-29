class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack != []:
            return self.stack.pop()
        return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack == []:
            return 1
        else:
            return 0

    def top(self):
        if self.stack != []:
            return self.stack[len(self.stack) - 1]
        return -1



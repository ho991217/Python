# 스택

class Stack:
    def __init__(self):
        self.data = []
        self.max = 5

    def push(self, data):
        if len(self.data) < self.max:
            self.data.append(data)
        else:
            print('StackOverflow')

    def pop(self):
        if not self.is_empty():
            self.data.pop()
        else:
            print('StackUnderflow')

    def is_empty(self):
        return self.data == []

    def peek(self):
        print(self.data[len(self.data) - 1])

    def printStack(self):
        print(self.data)


st = Stack()
for i in range(1,7):
    st.push(i)
st.printStack()
st.pop()
st.peek()
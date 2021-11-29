class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if not self.is_empty():
            data = self.head.val
            self.head = self.head.next
            return data
        else:
            print('EmptyStack!')
            return None

    def is_empty(self):
        return self.head == None

    def peek(self):
        return self.head.val


    def printStack(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print()


lst = Stack()
print(lst.is_empty())
for i in range(1, 6):
    lst.push(i)
lst.printStack()
lst.pop()
lst.printStack()
lst.pop()
print(lst.peek())
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.max = 5

    def push(self, data):
        if self.length() <= self.max:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

        else:
            print('StackOverflow')

    def pop(self):
        if self.is_empty():
            return None
        data = self.head.val
        self.head = self.head.next

        return data

    def peek(self):
        print(self.head.val)

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def print_Stack(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end = ' ')
            cur = cur.next
        print('')

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count


s = Stack()
s.push(1)
s.push(2)
s.push(3)

s.peek()

s.pop()
s.print_Stack()
print('len :',s.length())
print(s.is_empty())
s.pop()
s.pop()
s.pop()
print(s.is_empty())
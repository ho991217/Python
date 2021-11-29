class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.val
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

    def is_empty(self):
        if not self.head:
            return True

        return False

    def print_Queue(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end = ' ')
            cur = cur.next
        print()

    def reverse(self):
        pass




q = Queue()

q.enqueue(0)
print(q.head.next)
q.enqueue(1)
print(q.head.next.val)
q.enqueue(2)
# q.print_Queue()

# q.dequeue()
#
# q.print_Queue()
#
# q.reverse()

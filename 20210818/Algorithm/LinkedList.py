# 연결리스트

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)

    def remove(self, data):
        cur = self.head
        search = False

        while cur.next is not None:
            if cur.next.val == data:
                cur.next = cur.next.next
                search = True
            cur = cur.next

        if not search:
            print('NodeNotFound!')
            return None

    def reverse(self):
        prev = None
        cur = self.head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev


    def printList(self):
        cur = self.head

        while cur is not None:
            print(cur.val, end = ' ')
            cur = cur.next
        print('')


LL = LinkedList()
for i in range(1, 11):
    LL.add(i)

LL.remove(5)
LL.printList()

LL.reverse()
LL.printList()


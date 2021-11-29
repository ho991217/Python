# LinkedList ( 연결리스트 )

# Node : 관리할 데이터를 보관하는 곳을 노드라고 한다.
# 자료구조에서 관리하고 있는 정보들 중 하나를 저장하고 있는 단위

class Node:

    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)


    def remove(self, data):
        search = False
        cur = self.head
        while cur.next is not None:
            if cur.next.val == data:
                search = True
                cur.next = cur.next.next
                break
            cur = cur.next

        if search == False:
            print('OutOfRange! Remove Head')
            self.head = self.head.next


    # def removeData(self, data):


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
            print(cur.val, end=' - ')
            cur = cur.next
        print('')

a = LinkedList(1)
for i in range(2, 21):
    a.add(i)

print('LinkedList : ',end = '')
a.printList()

print('remove(4) : ',end = '')
a.remove(4)
a.printList()

print('remove(17) : ',end = '')
a.remove(17)
a.printList()

print('remove(99) : ',end = '')
a.remove(99)
a.printList()

print('reverse : ',end = '')
a.reverse()
a.printList()


# Tree
# 계층적인 구조를 표현하기 위한 자료구조
# 여러 노드가 한 노드를 가리킬 수 없는 구조
# 조직도, 디렉토리 구조

# 스택이나 큐 같은 선형구조가 아닌 뒤집힌 나무 모양 같은 계층 구조
# 탐색이나 계층적 구조를 가져야하는 데이터를 다루는 곳에 많이 사용한다.

# 이진트리 (Binary Tree)
# 최대 2개의 자식 노드를 가질 수 있는 노드를 의미한다.
# 한개의 노드가 2개, 1개, 0개의 자식노드를 가질 수 있다

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = Node(None)

    def add(self, data):
        if self.head.val is None:
            self.head.val = data
        else:
            self.add_node(self.head, data)

    def add_node(self, cur, data):
        if cur.val > data:
            if cur.left is not None:
                self.add_node(cur.left, data)
            else:
                cur.left = Node(data)
        else:
            if cur.right is not None:
                self.add_node(cur.right, data)
            else:
                cur.right = Node(data)


    def search(self, data):
        if self.search_node(self.head, data):
            print('True!')
        else:
            print('False ㅠㅠ')

    def search_node(self, cur, data):
        if cur.val == data:
            return True
        else:
            if cur.val > data:
                if cur.left is not None:
                    return self.search_node(cur.left, data)
                else:
                    return False
            elif cur.val < data:
                if cur.right is not None:
                    return self.search_node(cur.right, data)
                else:
                    return False



bt = BinaryTree()
bt.add(10)
bt.add(7)
bt.add(15)
bt.add(5)
bt.add(9)
bt.add(13)
bt.add(17)
print(bt.head.right.val)
bt.search(8)
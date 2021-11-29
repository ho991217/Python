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
            print('False')

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

    def remove(self, data):     # 헤드 확인 remove
        if self.head is None:
            print('None')

        if self.head.val == data:
            if self.head.left == None and self.head.right == None:
                self.head == None
            elif self.head.left == None and self.head.right != None:
                self.head = self.head.right
            elif self.head.left != None and self.head.right == None:
                self.head = self.head.left
            else:
                self.head.val = self.__most_left_val(self.head.right).val
                self.__removedata(self.head, self.head.right, self.head.val)

        else:# 헤드가 아닐 때
            if self.head.val > data:
                self.__remove(self.head, self.head.left, data)
            else:
                self.__remove(self.head, self.head.right, data)


    def __remove(self, parent, cur, data):      # 헤드가 아닐 때 삭제
        if cur == None:
            print('None')

        if cur.val == data:
            if cur.left == None and cur.right != None:  # 큰 노드만 존재
                cur.val = cur.right.val
                cur.right = None
            elif cur.right == None and cur.left != None:  # 작은 노드만 존재
                cur.val = cur.left.val
                cur.left = None
            elif cur.left != None and cur.right != None:  # 둘 다 존재
                cur.val = self.__most_left_val(cur.right).val
                self.__removedata(cur, cur.right, cur.val)

            else:  # 둘 다 없음
                # 현재 노드가 부모노드의 오른쪽 일 때
                if data > parent.val:
                    parent.right = None
                else:
                    parent.left = None
            return

        if data > cur.val:
            self.__remove(cur, cur.right, data)
        else:
            self.__remove(cur, cur.left, data)


    def __most_left_val(self, cur):     # 오른쪽 자식 노드의 가장 왼쪽 값
        while cur.left is not None:
            cur = cur.left
        return cur

    def __removedata(self, parent, cur, data):  # 재귀함수
        if cur.val == data:
            if data > parent.val:
                parent.right = None
            else:
                parent.left = None
            return

        if data > cur.val:
            self.__removedata(cur, cur.right, data)
        else:
            self.__removedata(cur, cur.left, data)

    def printTree(self):
        print('\t\t\t\t', bt.head.val)
        print('\t\t', bt.head.left.val, '\t\t\t', bt.head.right.val)
        print('\t', bt.head.left.left.val, '\t', bt.head.left.right.val, '\t', bt.head.right.left.val, '\t',
              bt.head.right.right.val)




bt = BinaryTree()
bt.add(27)
bt.add(14)
bt.add(35)
bt.add(10)
bt.add(19)
bt.add(31)
bt.add(42)
bt.add(30)
bt.add(40)

bt.remove(35)
bt.search(30)
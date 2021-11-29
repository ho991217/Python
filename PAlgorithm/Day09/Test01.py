# stack

# stack과 queue 는 search 가 없다

# LIFO ( Last Input First Out  선입 후출 )
# 데이터 저장소에서 새로 들어오는 데이터의 위치가 저장소의 끝부분이고,
# 내보내는 데이터 역시 저장소의 끝부분에서 나간다
# 입력은 push, 출력은 pop, peek 는 끝부분 위 ㅣㅊ에 잉ㅆ는 데이터 확ㄴ인


class Stack:
    def __init__(self):
        self.data = []
        self.max = 5

    def push(self, data):
        if len(self.data) < self.max:
            self.data.append(data)
        else:
            print('StackOverflow!')


    def pop(self):
        if not self.is_empty():
            self.data.pop()
        else:
            print('StackOverflow')

    def peek(self):
        if not self.is_empty():
            return self.data
        else:
            print('Stack에 데이터가 없습니다.')

    def is_empty(self):
        return self.data == []

    def print_Stack(self):
        print(self.data)

d = Stack()

d.push(1)
d.push(2)
d.push(3)
d.push(4)
d.push(5)
d.print_Stack()
d.push(6)
print('========')
print(d.peek())
d.pop()
d.peek()
d.pop()
d.print_Stack()
d.pop()
d.pop()
d.print_Stack()
d.pop()
d.pop()
print(d.is_empty())



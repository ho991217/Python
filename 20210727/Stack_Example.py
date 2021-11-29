# Stack 을 파이썬에서 구현 해 보자.

class Stack:
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.top = []

    # Stack의 크기 출력
    def len(self):
        return len(self.top)
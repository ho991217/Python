# 계산기 프로그램

# 메소드  -> 더하기, 빼기, 곱하기, 나누기
#          총 합해진 showInfo ( 더하기, 빼기, 곱하기, 나누기 메소드를 불러오는 메소드 )

class Calculator:
    def sum(self, n1, n2):
        return n1 + n2

    def dif(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

    def showInfo(self):
        print('기능 선택 : ')
        print('1. 더하기')
        print('2. 빼기')
        print('3. 곱하기')
        print('4. 나누기')

        select = int(input('>>> '))

        if select == 1:
            n1 = int(input('숫자 1 : '))
            n2 = int(input('숫자 2 : '))
            print(self.sum(n1, n2))
        elif select == 2:
            n1 = int(input('숫자 1 : '))
            n2 = int(input('숫자 2 : '))
            print(self.dif(n1, n2))
        elif select == 3:
            n1 = int(input('숫자 1 : '))
            n2 = int(input('숫자 2 : '))
            print(self.mul(n1, n2))
        elif select == 4:
            n1 = int(input('숫자 1 : '))
            n2 = int(input('숫자 2 : '))
            if n2 == 0:
                print('0으로 나눌 수 없습니다!')
                return 0
            print(self.div(n1, n2))
        else:
            print('Wrong Selection!')

c = Calculator()
c.showInfo()
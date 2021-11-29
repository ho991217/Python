class Num:
    # 1 ~ n 까지 합을 출력하는 메서드
    def tot(self, n):
        sum = 0
        for i in range(n + 1):
            sum += i
        print(sum)

    # 정수 3개를 입력받아 최대값을 출력하는 메서드
    def maxNum(self, n1, n2, n3):
        print(max(n1, n2, n3))

n = Num()
n.tot(10)
n.maxNum(10, -99, 2)
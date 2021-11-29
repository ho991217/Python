# 재귀함수

# 1 ~ n까지 누적합 구하는 함수

def plus(num):
    totNum = 0
    for i in range(num + 1):
        totNum += i

    print(totNum)

def dsp(num):
    for i in range(num):
        print(i + 1)


plus(10)
dsp(10)

print('======================')
# 재귀함수
# - 어떤 함수에서 자신을 다시 호출하여 작업을 수행하는 방식의 함수
# - 반복문을 사용하는 코드에 대부분 적용가능
# - 재귀함수 작성할 때, 함수 내에 자신 호출 뒤에 무한반복이 되지않도록 종료지점 서정해야함
# - 무한루프돌지 않게 방지

def disp1(n):
    if  n == 0:
        return 0
    else:
        print(n)
        disp1(n - 1)
disp1(5)

def tot1(n):
    if n == 1:
        return n
    else:
        r = n + tot1(n - 1)
        return r

print(tot1(10))
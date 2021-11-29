def isHansu(num):
    num = str(num)
    diff = int(num[0]) - int(num[1])
    hansu = False
    for i in range(1, len(num) - 1):
        if int(num[i]) - int(num[i + 1]) != diff:
            hansu = False
        else:
            hansu = True

    return hansu

def findHansu(num):
    hansuCount = 0
    for i in range(1, num + 1):
        if i <= 99:
            hansuCount += 1
        else:
            if isHansu(i):
                hansuCount += 1

    return hansuCount

n = int(input())
print(findHansu(n))
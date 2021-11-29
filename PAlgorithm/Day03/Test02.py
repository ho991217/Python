class School:
    score = [87, 100, 11, 72, 92]

mega = School()

# 전체 합 출력
def tot(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    return sum

print(tot(mega.score))


# 4의 배수의 합 출력
def tot4(data):
    sum = 0
    for i in range(len(data)):
        if data[i] % 4 == 0:
            sum += data[i]
    return sum

print(tot4(mega.score))


# 4의 배수의 개수 출력
def num4(data):
    count = 0
    for i in range(len(data)):
        if data[i] % 4 == 0:
            count += 1
    return count

print(num4(mega.score))



# 짝수의 개수 출력
def evenNum(data):
    count = 0
    for i in range(len(data)):
        if data[i] % 2 == 0:
            count += 1
    return count

print(evenNum(mega.score))
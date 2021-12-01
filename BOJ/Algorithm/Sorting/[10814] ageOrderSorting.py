import sys
N = int(sys.stdin.readline())
list = []

for index in range(N):
    age, name = map(str, sys.stdin.readline().rstrip().split(' '))
    list.append([int(age), name, index])

def age(element):
    return element[0]
def name(element):
    return element[1]
def regOrder(element):
    return element[2]

def quick(arr):
    if len(arr) <= 1: return arr

    left = []
    right = []
    pivot = []
    mid = arr[len(arr) // 2]
    mid_age = age(mid)
    mid_reg = regOrder(mid)

    for num in arr:
        num_age = age(num)
        if num_age > mid_age:
            right.append(num)
        elif num_age < mid_age:
            left.append(num)
        else:
            num_reg = regOrder(num)
            # 같을 경우 가입순서 비교
            if num_reg > mid_reg:
                right.append(num)
            elif num_reg < mid_reg:
                left.append(num)
            else:
                pivot.append(num)

    return quick(left) + pivot + quick(right)

list = quick(list)

for element in list:
    print(age(element), name(element))
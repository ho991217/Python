import math

arr = []
for i in range(int(input())):
    arr.append([int(i) for i in input().split(' ')])

def judge(arr):
    dist = math.sqrt((arr[3] - arr[0]) ** 2 + (arr[4] - arr[1]) ** 2)

    # 중점이 일치 하는 경우
    if dist == 0:
        # 반지름도 동일
        if arr[2] == arr[5]:
            return -1
        else:
            return 0

    # 중점이 일치 하지 않음
    else:
        if (arr[2] + arr[5] < dist) or (dist + arr[5] < arr[2]) or (dist + arr[2] < arr[5]):
            return 0
        elif (dist == arr[2] + arr[5]) or (dist + arr[5] == arr[2]) or (dist + arr[2] == arr[5]):
            return 1
        elif(dist < arr[2] + arr[5]) or (dist + arr[5] > arr[2]) or (dist + arr[2] > arr[5]):
            return 2


    # if arr[2] > dist or arr[5] > dist
    #
    # if dist == 0:
    #     if arr[2] == arr[5]:
    #         return -1
    #     else:
    #         return 0
    # else:
    #     if dist > radius:
    #         return 0
    #     elif dist == radius:
    #         return 1
    #     elif dist < radius:
    #         return 2


for i in arr:
    print(judge(i))
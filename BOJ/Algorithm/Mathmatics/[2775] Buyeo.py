import sys

def showAPT(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=' ')
        print()

aptIn = [[int(sys.stdin.readline().rstrip()), int(sys.stdin.readline().rstrip())] for _ in range(int(sys.stdin.readline().rstrip()))]


maxf = aptIn[0]
for i in range(1, len(aptIn)):
    if aptIn[i][0] > maxf[0]:
        maxf = aptIn[i]
    elif aptIn[i][0] == maxf[0]:
        if aptIn[i][1] > maxf[1]:
            maxf = aptIn[i]

apt = [[i for i in range(1, maxf[1] + 1)]]

showAPT(apt)
# print(apt)
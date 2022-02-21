import sys

N = int(sys.stdin.readline())
paper = [[int(i) for i in sys.stdin.readline().rstrip().split(' ')] for j in range(N)]
if all(all(i == 0 for i in j) for j in paper):
    print(1)
    print(0)
    exit(0)
elif all(all(i == 1 for i in j) for j in paper):
    print(0)
    print(1)
    exit(0)
blue, white = 0, 0

def isTheSame(arr, length=N // 2):
    global white
    global blue

    if length <= 0:
        return arr

    leftTop, rightTop, leftBot, rightBot = [[] for i in range(length)], [[] for i in range(length)], [[] for i in range(length)], [[] for i in range(length)]

    for i in range(len(arr)):
        if i < length:
            for j in range(len(arr[i])):
                if j < length:
                    leftTop[i].append(arr[i][j])
                else:
                    rightTop[i].append(arr[i][j])
        else:
            for j in range(len(arr[i])):
                if j < length:
                    leftBot[i - length].append(arr[i][j])
                else:
                    rightBot[i - length].append(arr[i][j])

    for array in [leftTop, rightTop, leftBot, rightBot]:
        if all(all(i == 0 for i in j) for j in array):
            white += 1

        elif all(all(i == 1 for i in j) for j in array):
            blue += 1

        else:
            isTheSame(array, length // 2)



isTheSame(paper)
print(white)
print(blue)
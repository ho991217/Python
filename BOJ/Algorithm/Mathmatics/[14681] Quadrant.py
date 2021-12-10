import sys

point = [int(sys.stdin.readline().rstrip()) for i in range(2)]

if point[0] > 0:
    if point[1] > 0:
        print(1)
    else:
        print(4)
else:
    if point[1] > 0:
        print(2)
    else:
        print(3)

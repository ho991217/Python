A, B, V = map(int, input().split())
day = 1
curPos = 0
while True:
    curPos += A
    if curPos >= V:
        print(day)
        exit(0)
    else:
        curPos -= B
        day += 1
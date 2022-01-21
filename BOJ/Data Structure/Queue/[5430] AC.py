import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    arr = deque()

    p = [i for i in sys.stdin.readline().rstrip()]
    n = int(sys.stdin.readline())
    for el in eval(sys.stdin.readline().rstrip()):
        arr.append(el)

    Dcounter = 0
    Rcounter = 0
    for cmd in p:
        if cmd == 'D':
            Dcounter += 1
        elif cmd == 'R':
            Rcounter += 1
    if Dcounter > len(arr):
        print('error')
        continue


    revd = False
    for cmd in p:
        if cmd == "R":
            revd = not revd

        elif cmd == "D":
            if revd:
                arr.pop()
            elif not revd:
                arr.popleft()

    if Rcounter % 2 == 1:
        arr.reverse()


    print(str(list(arr)).replace(" ", ""))
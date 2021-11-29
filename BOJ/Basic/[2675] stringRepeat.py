T = int(input())
for _ in range(T):
    R, P = input().split()
    P = [i for i in P]
    for i in P:
        for j in range(int(R)):
            print(i, end='')
    print()


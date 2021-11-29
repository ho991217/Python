prize2017 = [(5000000, 1), (3000000, 2), (2000000, 3), (500000, 4), (300000, 5), (100000, 6)]
prize2018 = [(5120000, 1), (2560000, 2), (1280000, 4), (640000, 8), (320000, 16)]

n = int(input())

tot = [0 for i in range(n)]

for i in range(n):
    p1, p2 = map(int, input().split(' '))
    tmp = 0

    for j in range(len(prize2017)):
        if p1 == 0:
            break
        tmp += prize2017[j][1]

        if tmp >= p1:
            tot[i] += prize2017[j][0]
            break

    tmp = 0

    for j in range(len(prize2018)):
        if p2 == 0:
            break
        tmp += prize2018[j][1]

        if tmp >= p2:
            tot[i] += prize2018[j][0]
            break

for i in tot:
    print(i)
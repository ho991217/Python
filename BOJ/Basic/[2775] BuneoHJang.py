def peopleSum(apart, floor, ho):
    people = 0

    for i in apart[floor - 1]:
        people += i
        if i == ho:
            break
        


T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [[ho for ho in range(n)] for floor in range(k+1)]

    for floor in range(len(apart)):
        for ho in range(len(apart[floor])):
            if floor != 0:
                person = 0
                for i in range(ho):


def solution(enter, leave):
    answer = []
    meetList = [[] for i in range(len(enter))]

    for entered in range(len(enter)):
        # X 교차 경우
        for left in range(len(leave)):
            if entered < enter.index(leave[left]) and leave.index(enter[entered]) > left:
                meetList[enter[entered] - 1].append(leave[left])
                meetList[leave[left] - 1].append(enter[entered])

        # 교차하지 않고 무조건 접촉하는 경우
    for cMoreThan2 in range(len(meetList)):
        # 두 선이상과 교차
        if len(meetList[cMoreThan2]) >= 2:
            certain = True
            for n in meetList[cMoreThan2]:
                if enter.index(n) > enter.index(cMoreThan2 + 1):
                    certain = False

            if certain:
                for i in meetList[cMoreThan2]:
                    meetList[i - 1].extend(meetList[cMoreThan2])

    for i in meetList:
        if meetList.index(i) + 1 in i:
            i.remove(meetList.index(i) + 1)
        i = i.sort()

    for i in meetList:
        answer.append(len(i))

    return answer





enter = [3, 2, 1]
leave = [1, 3, 2]


# enter = [1, 4, 2, 3]
# leave = [2, 1, 3, 4]

# enter = [1, 4, 2, 3]
# leave = [2, 1, 4, 3]


result = solution(enter, leave)
print(result)
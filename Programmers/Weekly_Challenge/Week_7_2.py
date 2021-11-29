
def solution(enter, leave):
    answer = [0 for i in range(len(enter))]

    contactList = dict()
    # 입장한 사람들을 딕셔너리형태로 정리
    # Key : 사람 번호
    inOutList = dict()
    for i in range(1, len(enter) + 1):
        inOutList[i] = {"입장순서" : enter.index(i) + 1, "퇴장순서" : leave.index(i) + 1}

    # print(inOutList)

    # 교차하는 경우 : Key는 큰데 Value가 작은경우 -> 나중에 들어왔는데 먼저 퇴장
    for i in inOutList:   # i = key, 입장한 사람 / contactList[i] = Value, 퇴장 순번
        for j in inOutList:
            if inOutList[i]["입장순서"] > inOutList[j]["입장순서"] and inOutList[i]["퇴장순서"] < inOutList[j]["퇴장순서"]:
                if i not in contactList: contactList[i] = []
                if j not in contactList: contactList[j] = []
                contactList[i].append(j)
                contactList[j].append(i)

    # contactList = dict(sorted(contactList.items()))

    # 교차하지 않지만 어떤 사람들보다 늦게 온 사람이 모든 어떤 사람들보다 일찍 나가는 경우
    for i in contactList:
        if len(contactList[i]) >= 2:
            certain = True

            for j in contactList[i]:
                if inOutList[j]["입장순서"] > inOutList[i]["입장순서"] or inOutList[j]["퇴장순서"] < inOutList[i]["퇴장순서"]:
                    certain = False

            if certain:
                for j in contactList[i]:
                    contactList[j].extend(list(set(contactList[i]) - set([j])))

    for i in contactList:
        answer[i - 1] = len(contactList[i])

    return answer

# enter = [1,3,2]
# leave = [1,2,3]
# result =[0,1,1]


# enter = [1,4,2,3]
# leave = [2,1,3,4]
# result = [2,2,1,3]

# enter = [3,2,1]
# leave = [2,1,3]
# result = [1,1,2]

# enter = [3,2,1]
# leave = [1,3,2]
# result = [2,2,2]

enter = [1,4,2,3]
leave = [2,1,4,3]
result = [2,2,0,2]


print(solution(enter, leave))
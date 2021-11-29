table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]


languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

# languages = ["JAVA", "JAVASCRIPT"]
# preference = [7, 5]

def solution(table, languages, preference):
    # Table을 dict 배열로 바꿔 점수를 넣어줌
    for i in range(len(table)): table[i] = table[i].split(' ')
    jobTable = [dict() for i in range(len(table))]

    for i in range(len(table)):
        for j in range(len(table[i])):
            jobTable[i][table[i][j]] = int(6 - j)

    jobNames = {}

    for i in range(len(jobTable)):
        tmpName = [k for k, v in jobTable[i].items() if v == 6]       # 추천 직업 이름
        tmpName = "".join(tmpName)
        jobTable[i][tmpName] = 0

        for j in range(len(languages)):
            if languages[j] in jobTable[i]:
                jobTable[i][tmpName] += preference[j] * jobTable[i][languages[j]]

        jobNames[tmpName] = jobTable[i][tmpName]

    tmp = [k for k, v in jobNames.items() if max(jobNames.values()) == v]
    tmp.sort()

    return tmp[0]


print(solution(table, languages, preference))
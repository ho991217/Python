def solution(scores):

    def grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'F'

    grades = []

    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])

        selfScore = tmp[i]

        if selfScore == max(tmp) or selfScore == min(tmp):
            tmp.pop(i)

            if selfScore in tmp:
                tmp.insert(i, selfScore)
        grades.append(grade(float(sum(tmp) / len(tmp))))

    return ''.join(grades)
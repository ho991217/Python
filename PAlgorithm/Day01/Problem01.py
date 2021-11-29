import random
score = []

# 문제 1) score 리스트에 1~100 사이의 랜덤 값 5개를 저장 해 주는 함수
def setVal():
    for i in range(5):
        score.append(random.randrange(1, 100))

# 문제 2) 성적이 60점 이상이면 합격
#        합격생들의 방 번호와 성적을 리턴 해 주는 함수
#        [[인덱스, 성적]]
def PassScore():
    congrates = []
    for i in range(len(score)):
        if score[i] >= 60:
            congrates.append([i, score[i]])
    return congrates

# 문제 3) 1등 학생의 방 번호를 리턴 해 주는 함수
def FirstPlace():
    return score.index(max(score))

setVal()
print(PassScore())
print(FirstPlace())
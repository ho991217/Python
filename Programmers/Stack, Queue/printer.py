"""
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다
"""
# priorities : 문서별 중요도 우선순위
# location : 내가 요청한 문서가 어디 있는지

# 스택을 사용해서 푼다

def solution(priorities, location):
    stack = []
    order = []

    for index in range(len(priorities)):
        push = False
        # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        tmp = priorities[0]     # 중요도 저장
        priorities = priorities[1:]

        # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        for j in priorities:
            if tmp < j:
                stack.append(index)
                push = True
                break
        # 3. 그렇지 않으면 J를 인쇄합니다
        if not push:
            order.append(index)
    order += stack

    return order.index(location) + 1





print(solution([1,2,8,3,4], 4))        # location = 2 이기 때문에, C가 내가 요청한 문서, 2로 가장 높기 때문에 첫째로 인쇄됨
# 기대 출력 : 1
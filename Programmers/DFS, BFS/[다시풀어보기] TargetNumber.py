"""
±a ±b ±c ±d ±e = target >> target ±a ±b ±c ±d ±e = 0
numbers를 슬라이싱하며 하나씩 지워나가다가 빈 리스트가 됨 -> 가장 아래까지 탐색

target에 target + a...e / target - a...e 등을 넣다가
target = 0 이 되면 타겟 넘버를 만족하는 경우 (and not numbers 안해주면 끝까지 탐색 안하고 종료)  -> return 1

target != 0 이면서 종료 -> 만족하는 경우가 아니므로 return 1

최종 return에는 solution( 덧셈하는 경우 ) + solution( 뺄셈하는 경우 )
"""

def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0

    return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])

print(solution([1, 1, 1, 1, 1], 3))
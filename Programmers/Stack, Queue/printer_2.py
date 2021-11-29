def solution(priorities, location):
    supreme = priorities.index(max(priorities))
    if supreme <= location: return (location - supreme) + 1
    else: return (len(priorities[supreme:]) + location) + 1

print(solution([1, 1, 9, 1, 1, 1], 0))
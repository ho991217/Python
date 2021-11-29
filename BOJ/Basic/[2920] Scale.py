def solution(arr):
    cache = []
    for i in range(0, len(arr) - 1):
        cache.append(arr[i] - arr[i + 1])

    if all(diff == -1 for diff in cache):
        return 'ascending'
    elif all(diff == 1 for diff in cache):
        return 'descending'
    else:
        return 'mixed'

arr = [int(i) for i in input().split()]
print(solution(arr))
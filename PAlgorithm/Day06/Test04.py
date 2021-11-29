# 선택 정렬(select sort)
# 작은 값을 찾아내서 첫 인덱스와 교체

# 모든 값 중에서 가장 작은 값 찾고
# 첫번째 값 (index = 0)을 제외하고 남은 값 중에서 가장 작은 값
# ...
# i 번째 부터 n-1 번째가 값 중에 가장 작은 값
# 비교할 대상이 없을 때 정렬

# 공간 내 값들의 위치만 바꾸는 것 O(1)
# 모든 인덱스 접근 O(n)
# 최소값 찾은 후 인덱스 (swap) O(n)
# -> 선택정렬의 시간복잡도 : O(n^2)
# - 성능 저하, 최적화 여지 ↓
# 실전 사용x, 가장 구현하기 쉬운 정렬 알고리즘

# 두개의 반복문


# [ 예제 ]
# 최솟값 구하는 반복문
# O(n^2)
def select_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]     # -> 값 교체
    return arr


print(select_sort([5, 3, 99, 23, 1]))
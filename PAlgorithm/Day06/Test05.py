# Bubble sort
# 선택정렬과 더불어 대표적인 O(n^2) 정렬 알고리즘
# 앞에서부터 정렬 해나가는 구조

# 공간 내의 값들을 위치만 바꾸는 것이 O(1)
# 모든 인덱스 접하기 O(n)
# 비교 하고 교대하기 O(n)
# → 총 시간복잡도 O(n^2)

# 선택 정렬과의 차이점
# 정렬이 되어있는 배열이 들어올 경우 O(n)까지 시간 복잡도 향상
import time


def bubble_sort(arr):
    for i in range (len(arr) - 1, 0, -1):       # 역순
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

start = time.time()
bubble_sort([1, 3, 7, 5, 4, 2, 6, 8])
end = time.time()
print('time took : ', end - start)

# 삽입정렬
# 선택정렬, 거풀정렬처럼 대표적인 O(n^2) 알고리즘
# 정렬범위를 1칸씩 확장 해 나가는 방식

# 삽입정렬은 점점 정렬의 범위가 넓어진다
# 바깥쪽 루프 순방향, 안쪽 루프는 역방향

# 정렬범위 2개로 시작해서 전체로 확장 O(n)
# 새롭게 추가 된 값과 기존의 값 비교 O(n)
# 삽입 정렬 O(n^2)

def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print(arr)

a = [2, 1, 5, 4, 3]
b = [1, 2, 3, 4, 5]
print('a : ')
insert_sort(a)
print('b : ')
insert_sort(b)
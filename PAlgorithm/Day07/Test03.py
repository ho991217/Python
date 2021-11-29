# 퀵정렬은 분할 정복 기법, 재귀 알고리즘을 이용한 정렬 알고리즘

# 가운데 기준으로 동일한 개수의 작은 값들과 큰 값들이 분할되어 O(n log n)
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    s_lst = []
    l_lst = []
    eq = []
    mid = arr[len(arr) // 2]

    for num in arr:
        if num > mid:
            l_lst.append(num)
        elif num < mid:
            s_lst.append(num)
        else:
            eq.append(num)

    return quick_sort(s_lst) + eq + quick_sort(l_lst)

start = time.time()
print(quick_sort([6,5,1,4,7,2,3]))
end = time.time()
print('time took : ', end - start)
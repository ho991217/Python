# 병합정렬
# 시간복잡도 O(nlogn)
import time

def mergeSort(ls):
    if len(ls) > 1:
        mid = len(ls) // 2
        left = ls[:mid]
        right = ls[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ls[k] = left[i]
                i += 1
            else:
                ls[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            ls[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ls[k] = right[j]
            j += 1
            k += 1

    print(ls)

start = time.time()
mergeSort([3, 1, 2, 5, 7, 4, 6, 8])
end = time.time()
print('time took : ', end - start)
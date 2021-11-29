Unsorted_array = [5, 2, 3, 7, 6, 1, 4]

def Quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, mid, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)

    return Quick_sort(left) + mid + Quick_sort(right)

print(Quick_sort(Unsorted_array))
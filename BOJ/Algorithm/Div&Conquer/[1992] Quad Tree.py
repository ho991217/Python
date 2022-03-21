import sys

def check(arr):
    isZero = False
    isOne = False

    if all(1 not in i for i in arr):
        isZero = True
    else:
        isZero = False

    if all(0 not in i for i in arr):
        isOne = True
    else:
        isOne = False

    if isZero:
        return 0
    elif isOne:
        return 1
    else:
        return None

def slice(arr, n):
    tmp = []

    if n == 0:
        for i in range(len(arr) // 2):
            tmp.append(arr[i][:len(arr) // 2])

    elif n == 1:
        for i in range(len(arr) // 2):
            tmp.append(arr[i][len(arr) // 2:])

    elif n == 2:
        for i in range(len(arr) // 2, len(arr)):
            tmp.append(arr[i][:len(arr) // 2])

    elif n == 3:
        for i in range(len(arr) // 2, len(arr)):
            tmp.append(arr[i][len(arr) // 2:])


    return tmp

N = int(sys.stdin.readline())

insert = [[int(i) for i in sys.stdin.readline().rstrip()] for j in range(N)]

ans = []

def cal(arr):
    result = check(arr)
    if result is None:
        ans.append('(')
        cal(slice(arr, 0))
        cal(slice(arr, 1))
        cal(slice(arr, 2))
        cal(slice(arr, 3))
        ans.append(')')

    elif result == 0:
        ans.append('0')

    elif result == 1:
        ans.append('1')

cal(insert)
print(''.join(ans))

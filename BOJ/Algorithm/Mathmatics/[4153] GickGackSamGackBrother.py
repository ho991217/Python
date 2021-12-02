def isGick(a, arr):
    return a**2 == arr[0]**2 + arr[1]**2

while True:
    a, b, c = map(int, input().split(' '))
    tmp = [a, b, c]
    if a == 0 and b == 0 and c == 0: break
    a = max(tmp)
    tmp.remove(a)
    if isGick(a, tmp):
        print('right')
    else:
        print('wrong')
n = int(input())

for i in range(n):
    print('*', end = '')

    if i == 0 or i == n - 1:
        for j in range(n - 2):
            print('*', end = '')
    else:
        for j in range(n - 2):
            print(' ', end='')



    print('*')
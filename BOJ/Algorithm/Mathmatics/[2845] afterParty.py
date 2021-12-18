L, P = map(int, input().split(' '))
print(' '.join(str(i - L * P) for i in [int(i) for i in input().split(' ')]))
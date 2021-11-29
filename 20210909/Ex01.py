from sys import stdin

N = [x.lower() for x in stdin.readline().rstrip()]
alphs = {}
for i in N:
    if i in alphs: alphs[i] += 1
    else: alphs[i] = 1

maxValue = 0
maxKey = ''
for i in alphs:
    if alphs[i] > maxValue:
        maxValue = alphs[i]
        maxKey = i
    elif alphs[i] == maxValue:
        print('?')
        exit(0)

print(maxKey.capitalize())
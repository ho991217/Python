import sys
from collections import deque

def cal(i1, i2):
    queue = deque()
    for i in i1:
        queue.append(i)
    s2 = i2[:]
    password = []

    lngth = len(queue)
    for i in range(lngth):
        word = queue.popleft()

        for j in range(len(s2)):
            if word == s2[j]:
                print('word match: ', s2[j])
                password.append(word)
                s2 = s2[j + 1:]
                break
    return password


i1 = sys.stdin.readline().rstrip()
i2 = sys.stdin.readline().rstrip()

answer1 = cal(i1, i2)
print('end!')
answer2 = cal(i2, i1)

print(answer1, answer2)
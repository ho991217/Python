from collections import deque

q = deque()
for i in range(1, int(input()) + 1):
    q.appendleft(i)

count = 1
while True:
    if len(q) == 1:
        break

    if count % 2 == 1:
        q.pop()
    else:
        q.appendleft(q.pop())
    count += 1

print(q.pop())

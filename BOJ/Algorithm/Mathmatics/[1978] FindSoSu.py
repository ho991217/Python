input()
numbers = map(int, input().split())
answer = 0

for i in numbers:
    sosu = True
    if i == 1: continue

    for j in range(2, i):
        if i % j == 0:
            sosu = False
            break

    if sosu: answer += 1

print(answer)


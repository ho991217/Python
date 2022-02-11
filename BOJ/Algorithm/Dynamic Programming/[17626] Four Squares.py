import math
import sys

# 99 = 9^2 + 4^2 + 1^2 + 1^2

N = int(sys.stdin.readline())

squares = [i**2 for i in range(1, math.ceil(math.sqrt(N)) + 1)]
print('sqaures: ', squares)

index = len(squares) - 1
answer = []
while True:
    answer.append(squares[index])

    if sum(answer) == N:
        print(answer)
        exit(0)
    elif sum(answer) > N:
        answer.remove(squares[index])
        index -= 11
    else:
        pass

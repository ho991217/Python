import math
import sys

number = [i for i in str(math.factorial(int(sys.stdin.readline())))]
count = 0
for i in range(len(number) - 1, 0, -1):
    if number[i] == '0':
        count += 1
    else:
        break

print(count)
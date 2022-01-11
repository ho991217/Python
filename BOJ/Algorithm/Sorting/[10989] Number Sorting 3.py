import sys

number = [0 for _ in range(0, 10001)]

for _ in range(int(sys.stdin.readline())):
    number[int(sys.stdin.readline())] += 1

for i in range(len(number)):
    if number[i] != 0:
        for _ in range(number[i]):
            print(i)

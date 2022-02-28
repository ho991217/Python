import sys

cache = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]

for _ in range(int(sys.stdin.readline())):
    print(cache[int(sys.stdin.readline()) - 1])
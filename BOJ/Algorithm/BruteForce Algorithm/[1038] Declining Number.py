import sys

# N = int(sys.stdin.readline())
cache = []

def isDecline(n):
    number = str(n)
    for i in range(len(number) - 1):
        if int(number[i]) <= int(number[i + 1]):
            return False
    return True

counter = 0
while counter <= 9876543210:
    if isDecline(counter):
        cache.append(counter)
    counter += 1

print(cache)

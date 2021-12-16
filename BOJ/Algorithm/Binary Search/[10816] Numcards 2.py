import sys

_ = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split(' ')))
_ = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))
hashmap = {}

for n in cards:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in nums))
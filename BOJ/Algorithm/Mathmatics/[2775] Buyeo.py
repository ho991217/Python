import sys

testCases = []
maxK, maxN = 0, 0

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = [i for i in range(1, n + 1)]

    for _ in range(k):
        for lower in range(1, n):
            people[lower] += people[lower - 1]
    print(people[len(people) - 1])

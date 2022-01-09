import sys

sys.stdin.readline()
arr = sorted(list(map(int, [i for i in sys.stdin.readline().rstrip().split(' ')])))

answer = 0
for i in range(len(arr)):
    tmp = arr[i]
    arr[i] = tmp + answer
    answer += tmp

print(sum(arr))
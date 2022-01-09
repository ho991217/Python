import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
heard = set(sys.stdin.readline().rstrip() for _ in range(N))
saw = set(sys.stdin.readline().rstrip() for _ in range(M))

result = list(heard - (heard - saw))

print(len(result))
print('\n'.join(sorted(result)))
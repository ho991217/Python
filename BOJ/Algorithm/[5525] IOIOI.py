import sys

N = int(sys.stdin.readline())
# Pn의 길이는 2n + 1
Pn = "IO" * N + "I"
pLength = len(Pn)
M = int(sys.stdin.readline())
S = [i for i in sys.stdin.readline().rstrip()]

counter = 0
for i in range(len(S)):
    if S[i] == "I":
        if ''.join(S[i:i+pLength]) == Pn:
            counter += 1

print(counter)
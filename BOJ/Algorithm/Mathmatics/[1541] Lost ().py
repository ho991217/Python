import sys

eq = [i for i in sys.stdin.readline().rstrip()]

for i in range(len(eq)):
    if eq[i] == '-' and eq[i + 1]:
        eq.insert(i, '(')

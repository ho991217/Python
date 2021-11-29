from sys import stdin
from sys import stdout

T = stdin.readline()
for i in range(int(T)):
    n1, n2 = stdin.readline().split()
    print(int(n1) + int(n2))
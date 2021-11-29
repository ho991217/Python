"""
121
1231
12421
0
"""
while True:
    n = input()
    if n == '0': break
    if n == ''.join(reversed([i for i in n])): print('yes')
    else: print('no')
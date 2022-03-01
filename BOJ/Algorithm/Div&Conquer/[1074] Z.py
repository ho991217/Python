import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())

def find(col, row, N, topCorner = 0):
    if N == 0:
        return topCorner

    half = 2 ** (N - 1)
    if half > col and half <= row:
        topCorner += half ** 2
        row -= half
    elif half <= col and half > row:
        topCorner += 2 * (half ** 2)
        col -= half
    elif half <= col and half <= row:
        topCorner += 3 * (half ** 2)
        col -= half
        row -= half

    return find(col, row, N-1, topCorner)

print(find(r, c, N))
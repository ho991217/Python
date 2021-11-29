# 순열
# 다이나믹

def perm(n, i):
    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            perm(n, i + 1)
            n[i], n[j] = n[j], n[i]


perm([1, 2, 3], 0)
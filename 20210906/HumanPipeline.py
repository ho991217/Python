N, K = input().split()
N, K = int(N), int(K)

vi = [x for x in input().split()]
for i in range(len(vi)):
    vi[i] = int(vi[i])

vi.sort()

minTime = K // min(vi)

for i in range(1, len(vi)):
    teama = [x for x in vi[:i]]
    teamb = [x for x in vi[i:]]
    na = len(teama)
    nb = len(teamb)

    va = min(teama) * na
    vb = min(teamb) * nb
    V = va + vb

    count = 1
    while (V * count < K):
        count += 1

    if (count < minTime): minTime = count


print(minTime)





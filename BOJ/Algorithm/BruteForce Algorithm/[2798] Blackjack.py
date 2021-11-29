N, M = map(int, input().split())
cards = [int(i) for i in input().split()]
poss = []
for i in range(0, len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            cardSum = cards[i] + cards[j] + cards[k]
            if cardSum <= M:
                poss.append(cardSum)
print(max(poss))
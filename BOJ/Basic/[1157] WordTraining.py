word = [i for i in input()]

def solution(word):
    frequency = dict()

    for i in word:
        i = i.upper()
        if i not in frequency: frequency[i] = 1
        else: frequency[i] += 1

    frq = [k for k, v in frequency.items() if v == max(frequency.values())]

    if len(frq) > 1: return '?'

    return frq[0]


print(solution(word))
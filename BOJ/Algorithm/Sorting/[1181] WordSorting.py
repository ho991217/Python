N = int(input())
words = [input() for i in range(N)]
words = list(set(words))

def priorWord(word1, word2):
    if len(word1) != len(word2):
        return word1 if len(word1) < len(word2) else word2
    else:
        for i in range(len(word1)):
            if ord(word1[i]) == ord(word2[i]):
                pass
            elif ord(word1[i]) > ord(word2[i]):
                return word2
            else:
                return word1

for i in range(0, len(words) - 1):
    priorIndex = i
    for j in range(i, len(words)):
        if priorWord(words[priorIndex], words[j]) == words[j]:
            priorIndex = j
    words[i], words[priorIndex] = words[priorIndex], words[i]

for i in words:
    print(i)
alph = [-1 for i in range(26)]
word = [i for i in input()]

for i in range(len(word)):
    index = ord(word[i]) - 97
    if alph[index] == -1:
        alph[index] = i

for i in alph:
    print(i, end=' ')
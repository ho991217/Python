# N = int(input())
# words = [input() for i in range(N)]
# words = list(set(words))
#
# def priorWord(word1, word2):
#     if len(word1) != len(word2):
#         return word1 if len(word1) < len(word2) else word2
#     else:
#         for i in range(len(word1)):
#             if ord(word1[i]) == ord(word2[i]):
#                 pass
#             elif ord(word1[i]) > ord(word2[i]):
#                 return word2
#             else:
#                 return word1
#
# for i in range(0, len(words) - 1):
#     priorIndex = i
#     for j in range(i, len(words)):
#         if priorWord(words[priorIndex], words[j]) == words[j]:
#             priorIndex = j
#     words[i], words[priorIndex] = words[priorIndex], words[i]
#
# for i in words:
#     print(i)
import sys

lines = [sys.stdin.readline().rstrip() for i in range(int(sys.stdin.readline().rstrip()))]
lines = list(set(lines))

def srt(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left, mid, right = [], [], []

    for i in arr:
        if len(i) > len(pivot):
            right.append(i)
        elif len(i) < len(pivot):
            left.append(i)
        else:
            mid.append(i)

    return srt(left) + sorted(mid) + srt(right)

print('\n'.join(srt(lines)))
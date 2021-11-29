# import sys
# from collections import Counter
#
# t = int(sys.stdin.readline())
#
# numbers = []
# for _ in range(t):
#     numbers.append(int(sys.stdin.readline()))
#
# print(int(sum(numbers) / len(numbers)))
# print(sorted(numbers)[len(numbers) // 2])
#
# # retry!
# # if (len(set(numbers)) == len(numbers)):
# #     print(sorted(numbers)[1])
# # else:
# #     tmp = [0 for i in range(max(numbers))]
# #     for i in numbers:
# #         tmp[i - 1] += 1
# #
# #     print(tmp)
# #
# #     num = 0
# #     most = []
# #     for k in tmp:
# #         if k == max(tmp):
# #             num += 1
# #             most.append(tmp.index(k) + 1)
# #
# #     print(most)
# #
# #     if (num == 1):
# #         print('hi')
# #         print(most[0])
# #     else:
# #         most.remove(min(most))
# #         print(min(most))
# #
# #
#
# def mode(nums):
#     mode_dict = Counter(nums)
#     modes = mode_dict.most_common()
#
#     if len(nums) > 1:
#         if modes[0][1] == modes[1][1]:
#             mod = modes[1][0]
#         else:
#             mod = modes[0][0]
#     else:
#         mod = modes[0][0]
#
#     return mod
#
# print(mode(numbers))
# print(max(numbers) - min(numbers))

import sys
from collections import Counter

# main
t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))


def mean(nums):
    return round(sum(nums) / len(nums))


def median(nums):
    nums.sort()
    mid = nums[len(nums) // 2]

    return mid


def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod


def scope(nums):
    return max(nums) - min(nums)


print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))
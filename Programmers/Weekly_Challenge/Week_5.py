from itertools import product

one = ['A', 'E', 'I', 'O', 'U']
two = [i + j for (i, j) in product(one, one)]
three = [i + j + k for (i, j, k) in product(one, one, one)]
four = [i + j + k + l for (i, j, k, l) in product(one, one, one, one)]
five = [i + j + k + l + m for (i, j, k, l, m) in product(one, one, one, one, one)]

dictionary = sorted(one + two + three + four + five)

print(dictionary.index('AAAE'))
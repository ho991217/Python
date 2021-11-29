input()
n = [int(i) for i in input().split()]
minimum, maximum = n[0], n[0]
for i in n:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print(minimum, maximum)
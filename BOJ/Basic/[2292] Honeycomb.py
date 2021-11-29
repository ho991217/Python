n = int(input())

floor = 1
element = 1

while element < n:
    element += 6 * floor
    floor += 1

print(floor)


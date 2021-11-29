

def pyMax(*value):
    maxVal = value[0]
    for i in range(value.__len__()):
        if value[i] > maxVal:
            maxVal = value[i]

    return maxVal


def pyMin(*value):
    minVal = value[0]
    for i in range(value.__len__()):
        if value[i] < minVal:
            minVal = value[i]

    return minVal



print(pyMax(1, 2, 5, 1, 10, 4, 3, 12.2, -77))
print(pyMin(1, 2, 5, 1, 10, 4, 3, 12.2, -77))
arr = [int(input()) for i in range(9)]
maxV = (0, arr[0])
for k, v in enumerate(arr):
    if maxV[1] < v:
        maxV = (k, v)

print(maxV[1])
print(maxV[0] + 1)
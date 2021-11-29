N = int(input())
doomsNumber = 0
count = 0

while count < N:
    doomsNumber += 1
    if '666' in str(doomsNumber):
        count += 1
print(doomsNumber)
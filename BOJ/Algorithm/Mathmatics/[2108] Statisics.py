numbers = [int(input()) for _ in range(int(input()))]

print(int(sum(numbers) / len(numbers)))
print(sorted(numbers)[len(numbers) // 2])


if (len(set(numbers)) == len(numbers)):
    print(sorted(numbers)[1])
else:
    tmp = [0 for i in range(max(numbers))]
    for i in numbers:
        tmp[i - 1] += 1

    num = 0
    most = []
    for k in tmp:
        if k == max(tmp):
            num += 1
            most.append(k)

    if (num == 1):
        print(most[0])
    else:
        most.remove(min(most))
        print(min(most))





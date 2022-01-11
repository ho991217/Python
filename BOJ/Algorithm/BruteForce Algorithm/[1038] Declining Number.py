import sys

N = int(sys.stdin.readline())

counter = -1
number = 0

while True:
    if number > 9876543210:
        number = -1
        break
    string_num = [i for i in str(number)]
    # print('current number: ', string_num)
    isDecliningNumber = True

    for i in range(len(string_num) - 1):
        if int(string_num[i]) <= int(string_num[i + 1]):
            # print('not declining number, i = ', i ,end=' ')

            string_num[i] = str(int(string_num[i]) + 1)
            for j in range(i + 1, len(string_num)):
                string_num[j] = '0'
            # print(string_num)
            isDecliningNumber = False

    number = int(''.join(string_num))
    if isDecliningNumber:
        counter += 1
        if counter == N:
            break
        else:
            number += 1

print(number)
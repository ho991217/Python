digits = [0 for i in range(10)]
for i in str(int(input()) * int(input()) * int(input())): digits[int(i)] += 1
for i in digits: print(i)
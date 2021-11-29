# 어떤 수의 각 자리 숫자 합을 계산하는 재귀함수

#5472

# tot(5472) = 2 + tot(547)
# tot(547) = 7 + tot(54)
# tot(54) = 4 + tot(5)
# tot(5) = 5

# def tot(n):
#     if len(str(n)) == 1:
#         return n
#     else:
#         num = str(n)
#         s_num = int(num[len(num) - 1])
#         r_num = int(num[:-1])
#         return s_num + tot(r_num)

def tot1(n):
    if n == 0:
        return 0
    else:
        return n % 10 + tot1(n // 10)


def tot2(n):
    tot = 0

    while n!=0:
        tot += (n % 10)
        n = n // 10 # / -> 실수 // -> 정수

    return tot

print(tot1(5472))
print(tot2(5472))
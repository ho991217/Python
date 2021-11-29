# O(1) : 상수, 문제를 해결하는데 한단계만 처리
def hello():
    print("Hello")
hello()


# O(n) : 선형, 문제 해결하기 위한 단계 수와 입력값이 1 : 1
def print_n(n):
    for i in n:
        print(i)
print_n([1, 2, 3])


# O(n^2) : 반복문 두번, 문제 해결하기 위한 단계수가 n^2
def print_n1(n):
    for i in n:
        for j in i:
            print([i, j])
print_n1([[1, 2, 3], [4, 5, 6]])


# O(logn), O(nlogn) : 정렬 알고리즘에서 많이 사용
def search(ls, a, first = 0, last = None):
    if not last:
        last = len(ls)
    point = (last - first) // 2 + first

    if ls[point] == a:
        return point
    elif ls[point] > a:
        return search(ls, a, first, point)
    else:
        return search(ls, a, point, last)
# ↑ 정렬 알고리즘
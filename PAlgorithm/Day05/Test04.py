class Info:
    __a = 5     # __private_ 로 속성명을 시작하면 비공개 속성이 된다.
    __private_attr = 10

info = Info()
info.__a = 5
print(info.__a)
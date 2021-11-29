def test(**data):
    for i in data:
        print(i, ':', data[i])


test(이름 = input('이름 = '), 나이 =  input('나이 = '), 주소 = input('주소 = '))

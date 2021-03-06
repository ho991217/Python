#CPP - 디폴트 매개변수, 함수의 오버로드
#Java = 함수의 오버로드
#Python - 디폴트 매개변수

#Python에서는 함수의 오버로드가 불가능..

# 디폴트 매개변수
# - 실제 인자값이 없더라도 매개변수에 기본 저장값으로 초기화 시켜주는 가능
# - 함수의 수를 줄이고 통합적으로 처리하기 위해서 만들어진 문법
# - 매개변수에 대입 연산자를 통하여 기본값을 설정하면 된다.

# 디폴트 매개변수의 주의 사항
# - 인자값은 적은 순서대로 매개변수 왼쪽부터 차례로 들어간다
# - 디폴트 매개변수는 정의할 때 반드시 가장 우측부터 정의해야한다.

def disp(a = 10, b = 20, c = 30):
# def disp(a = 10, b = 20, c) -> 에러남
# def disp(a, b, c = 30) -> 에러 안남
    print(a, b, c)

disp()
disp(1)
disp(1, 2)
disp(1, 2, 3)

# 키워드 인자
# - 매개 변수에 들어갈 데이터를 지정하여 넣는 문법
# - 필요에 따라 매개변수를 지정하여 데이터를 넣어주면된다
# disp(a = 1, 2, 3)


# 가변매개변수
# - 매개변수의 개수를 상황에 따라서 여러 개 만들 수 있도록 하는 문법
# - 매개변수 앞에 *을 붙여서 선언하면 된다.
# - 가번 매개변수를 튜플로 처리한다.

def tot(*data):
    print(type(data))
    print(data.__len__())

    to = 0
    for i in data:
        to += i
        print(to)

tot(1,2,3,4,5,6,7,8,9,10)
tot(1,2,4,8)
tot(3)

# 키워드 가변인자
# - 키워드를 지정하여 인자 값을 넣는데, 인자값의 변수 병을 지정하여 넣는 방식
# - 딕셔너리 타입으로 인자값을 넣는 형태
# - 매개변수 앞에 **을 붙여서 선언

def disp2(**data):
    print(type(data))
    print(data)

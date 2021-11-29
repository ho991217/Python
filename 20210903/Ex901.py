def solution(numbers):
    def priority(n1, n2):
        n1str = [x for x in str(n1)]
        n2str = [x for x in str(n2)]

        print(n1str, n2str)
        while True:
            if len(n1str) == len(n2str):
                for i in range(len(n1str)):
                    if int(n1str[i]) > int(n2str[i]):
                        return n1
                    elif int(n1str[i]) < int(n2str[i]):
                        return n2
                    else:
                        pass



    print(priority(1234, 5678))

    answer = ''
    return answer


print(solution([6, 10, 2]))
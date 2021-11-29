def solution(priorities, location):
    order = 1
    index = [i for i in range(len(priorities))]

    while priorities:
        tmp = priorities[0]

        if tmp == max(priorities):
            # order.append(index[0])
            if index[0] == location:
                return order
            else:
                order += 1
        else:
            priorities.append(tmp)
            index.append(index[0])

        priorities = priorities[1:]
        index = index[1:]

for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = [int(i) for i in input().split()]
    print(solution(priorities, M))
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

"""
최적의 답

def solution(priorities, location):
    order = 0
    queue = [(i, priority) for i, priority in enumerate(priorities)]
    
    while priorities:
        tmp = queue.pop(0)

        if any(tmp[1] < q[1] for q in queue):
            queue.append(tmp)
        else:
            order += 1
            if tmp[0] == location:
                return order

"""



print(solution([1, 1, 9, 1, 1, 1], 0))

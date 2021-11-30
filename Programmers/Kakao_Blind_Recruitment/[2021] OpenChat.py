def solution(record):
    users = dict()
    log = []
    output = []

    for line in record:
        cache = line.split()

        if cache[0] == 'Enter':
            users[cache[1]] = cache[2]
            log.append([0, cache[1]])

        elif cache[0] == 'Leave':
            log.append([1, cache[1]])

        elif cache[0] == 'Change':
            users[cache[1]] = cache[2]


    for line in log:
        if line[0] == 0:
            output.append(users[line[1]] + '님이 들어왔습니다.')
        elif line[0] == 1:
            output.append(users[line[1]] + '님이 나갔습니다.')

    return output
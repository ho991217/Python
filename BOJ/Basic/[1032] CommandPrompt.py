N = int(input())
answer = []
for i in range(N):
    tmp = [x for x in input()]
    if i == 0: cmd = [[] for _ in range(len(tmp))]
    for j in range(len(tmp)): cmd[j].append(tmp[j])

for i in range(len(cmd)):
    if all(word == cmd[i][0] for word in cmd[i]):
        answer.append(cmd[i][0])
    else:
        answer.append('?')
answer = "".join(answer)
print(answer)
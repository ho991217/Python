def solution(a, b):
	tmp = []
	i = 1
	while True:
		if a ** i % 10 == 0:
			return 10
		if a ** i % 10 in tmp:
			break
		else:
			tmp.append(a ** i % 10)
			i += 1
	order = b % len(tmp)
	
	if order == 0:
		return tmp[len(tmp) - 1]
	else:
		return tmp[order - 1]
		
for _ in range(int(input())):
	a, b = map(int, input().split())
	print(solution(a, b))


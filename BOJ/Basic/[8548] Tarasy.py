import sys

n, k = map(int, sys.stdin.readline().split())
heights = [int(sys.stdin.readline()) for _ in range(n)]
count = 1

for i in range(0, n - 1):
	diff = heights[i + 1] - heights[i]
	
	if diff <= 0:
		count += 1
		
	else:
		if diff <= k:
			count += 1
		else:
			break
			
print(count)


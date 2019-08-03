# Set data
prob = list(map(int, input().split()))
p = prob[0] / prob[1]
q = 1 - p
n = int(input())

# Get geometric distribution
res = 0
for i in range(n + 1): 
	if i > 0: 
		res = res + (q ** (i - 1) * p)

print(round(res, 3))
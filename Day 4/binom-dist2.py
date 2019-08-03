# Define functions
def factorial(n): 
	if n == 1 or n == 0:
		return 1
	if n > 1: 
		return factorial(n - 1) * n

def binom(x, n, p): 
	f  = factorial(n) / (factorial(n - x) * factorial(x))
	return (f * p**x * (1.0 - p)**(n - x))

# Set data
val = list(map(float, input().split()))
p = (val[0] / 100)
n = int(val[1])

# No more than 2 rejects
no_more = 0
for i in range(n): 
	if i < 3: 
		no_more = no_more + binom(i, n, p)
print(round(no_more, 3))

# At least 2 rejects
at_least = 0
for i in range(n): 
	if i > 1: 
		at_least = at_least + binom(i, n, p)
print(round(at_least, 3))
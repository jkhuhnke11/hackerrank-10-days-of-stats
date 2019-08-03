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
p = val[0] / (val[0] + val[1])
n = 6

# Get result
result = binom(3, n, p) + binom(4, n, p) + binom(5, n, p) + binom(6, n, p)
print(round(result, 3))
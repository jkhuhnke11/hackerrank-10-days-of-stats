# Define Functions
def factorial(n): 
	if n == 1 or n == 0: 
		return 1
	if n > 1: 
		return factorial(n - 1) * n

# Set Data
mean = float(input())
k = float(input())
e = 2.71828

# Gets Results
result = ((mean ** k) * (e ** -mean))/factorial(k)
print(round(result, 3))
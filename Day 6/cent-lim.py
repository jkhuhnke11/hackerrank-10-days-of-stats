import math

# Define Functions
def cumulative(mean, std, val): 
	return 0.5 * (1 + math.erf((val - mean) / (std * (2 ** 0.5))))

# Set Data
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Print Result
print(round(cumulative(new_mean, new_std, max_weight), 4))
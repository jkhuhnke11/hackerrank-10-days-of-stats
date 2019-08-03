import math

# Define Functions
def cumulative(mean, std, value): 
	return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set Data
init_val = list(map(float, input().split()))
mean = init_val[0]
std = init_val[1]
less_per = float(input())
between_per = list(map(float, input().split()))

# Gets Results
print(round(cumulative(mean, std, less_per), 3))
print(round(cumulative(mean, std, between_per[1]) - cumulative(mean, std, between_per[0]), 3))
import math

# Define Functions
def cumulative(mean, std, value): 
	return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set Data
init_val = list(map(float, input().split()))
mean = init_val[0] 
std = init_val[1]
val_first = float(input())
val_sec = float(input())

# Gets Results
print (round(100 - (cumulative(mean, std, val_first) * 100), 2))
print (round(100 - (cumulative(mean, std, val_sec) * 100), 2))
print (round(cumulative(mean, std, val_sec) * 100, 2))
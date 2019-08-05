import statistics as stat

# Define Function
def corr_coef(n, dt_x, dt_y): 
	mean_x = stat.mean(dt_x)
	mean_y = stat.mean(dt_y)
	std_x = stat.pstdev(dt_x)
	std_y = stat.pstdev(dt_y)
	c = 0
	for i in range(n): 
		c = c + (dt_x[i] - mean_x) * (dt_y[i] - mean_y)
	return c / (n * std_x * std_y)

# Set Data
n = int(float(input()))
data_set_x = list(map(float, input().split()))
data_set_y = list(map(float, input().split()))

# Gets Result
print(round(corr_coef(n, data_set_x, data_set_y), 3))
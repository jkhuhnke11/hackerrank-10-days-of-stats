# Define Function
def rank(dt): 
	rank = {}
	sort = sorted(dt)
	for i in range(len(dt)): 
		for j in range(len(sort)):
			if dt[i] == sort[j]: 
				rank[dt[i]] = j + 1
	return rank

def spearman(x, y, rx, ry, n): 
	diff_rank = 0
	for i in range(n): 
		if rx[x[i]] != ry[y[i]]: 
			diff_rank = diff_rank + ((rx[x[i]] - ry[y[i]]) ** 2)
	return (6 * diff_rank) / (n ** 3 - n)

# Set Data
n = int(float(input()))
data_set_x = list(map(float, input().split()))
data_set_y = list(map(float, input().split()))

# Get Rank
rank_x = rank(data_set_x)
rank_y = rank(data_set_y)

# Result
s = spearman(data_set_x, data_set_y, rank_x, rank_y, n)
print(round(1 - s, 3))
		 	 
	
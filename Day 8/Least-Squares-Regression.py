import statistics as stat

# Set data
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mean_x = stat.mean(x)
mean_y = stat.mean(y)
x_sq = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i] * y[i] for i in range(5)])

# Set B and A
b = (n * xy - sum(x) * sum(y)) / (n * x_sq - (sum(x) ** 2))
a = mean_y - b * mean_x

# Prints Results
print(round(a + 80 * b, 3))
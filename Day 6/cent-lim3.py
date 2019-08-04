import math

# Set Data
n = float(input())
mean = float(input())
std = float(input())
per_ci = float(input())
val_ci = float(input())

# Confidence Interval Formula
ci = val_ci * (std / math.sqrt(n))

# Prints Result
print(round(mean - ci, 2))
print(round(mean + ci, 2))
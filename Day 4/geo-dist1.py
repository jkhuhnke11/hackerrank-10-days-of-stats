# Set data
prob = list(map(int, input().split()))
p = prob[0] / prob[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = q ** (n - 1) * p
print(round(result, 3))
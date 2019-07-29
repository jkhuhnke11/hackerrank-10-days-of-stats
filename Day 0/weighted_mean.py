# Creates a weighed mean function
size = int(input())
num = list(map(int, input().split()))
weighted = list(map(int, input().split()))

sum_items = 0
for i in range(size): 
	sum_items = sum_items + (num[i] * weighted[i])

print(round(sum_items/sum(weighted), 1))
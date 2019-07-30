# Defines functions
def median(size, val):
	if size % 2 == 0:
		median = (val[int(size/2)-1] + val[int(size/2)])/2
	else: 
		median = val[int(size/2)]
	return int(median)

# Set up data
size = int(input())
num = sorted(list(map(int, input().split())))

# Check if there is an even or odd amount of data
if size % 2 == 0: 
	data_low = num[0:int(size/2)]
	data_high = num[int(size/2):size]
else: 
	data_low = num[0:int(size/2)]
	data_high = num[int(size/2)+1:size]

# Print final result
print(median(len(data_low), data_low))
print(median(size,num))
print(median(len(data_high), data_high))
# Import library
import math

# Define functions
def mean(data): 
	return sum(data)/len(data)

def stddev(data,size): 
	sum = 0
	for i in range(size): 
		sum = sum + (data[i] - mean(data)) ** 2
	return math.sqrt(sum/size)

# Set data
size = int(input())
num = list(map(int,input().split()))

# Get standard deviation
print(round(stddev(num, size), 1))
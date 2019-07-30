# Defines functions
def median(size, val):
	if size % 2 == 0:
		median = (val[int(size/2)-1] + val[int(size/2)])/2
	else: 
		median = float(val[int(size/2)])
	return median

# Set the data
size = int(input())
elem = list(map(int, input().split()))
freq = list(map(int, input().split()))

new_data = []
for i in range(len(elem)): 
	for j in range(freq[i]): 
		new_data.append(elem[i])
new_data = sorted(new_data)

# Verify if length of new data is even or odd
size = int(len(new_data))
if size % 2 == 0: 
	data_low = new_data[0:int(size/2)]
	data_high = new_data[int(size/2):size]
else: 
	data_low = new_data[0:int(size/2)]
	data_high = new_data[int(size/2)+1:size]

# Print final results on screen 
low = median(len(data_low), data_low)
high = median(len(data_high), data_high)
print(high - low)
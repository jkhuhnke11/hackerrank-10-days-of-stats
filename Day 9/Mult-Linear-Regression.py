from sklearn import linear_model

# Set data
m, n = map(int, input().split())
X, Y = [], []

# Get Parameters X and Y for determination of a and b
for i in range(n): 
	x = [0]
	elements = list(map(float, input().split()))
	for j in range(len(elements)): 
		if j < m:
			x.append(elements[j])
		else: 
			Y.append(elements[j])
	X.append(x)

# Set the Linear Regression Model
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for Determination of Y
q = int(input())
new_X = []
for i in range(q):
	x = [0]
	elements = list(map(float, input().split()))
	for j in range (len(elements)): 
		x.append(elements[j])
	new_X.append(x)

# Gets the Result
result = model.predict(new_X)
for i in range(len(result)): 
	print(round(result[i], 2))
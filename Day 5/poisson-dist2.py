# Set Data
lamb = list(map(float, input().split()))
lamb_a = lamb[0]
lamb_b = lamb[1]

# Gets Results
print(round(160 + 40 * (lamb_a + lamb_a ** 2), 3))
print(round(128 + 40 * (lamb_b + lamb_b ** 2), 3)) 
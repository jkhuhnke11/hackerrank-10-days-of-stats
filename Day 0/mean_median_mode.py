# Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

size = int(input())
num = list(map(int, input().split()))
print(np.mean(num))
print(np.median(num))
print(int(stats.mode(num)[0]))
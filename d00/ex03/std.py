import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex02")
from variance import variance
import numpy as np

def std(x):
	var = variance(x)
	if var:
		return var**0.5

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print("me :", std(X))
print("np :", np.std(X))

print("me :", std(Y))
print("np :", np.std(Y))

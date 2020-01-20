import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex04")
from dot import dot
import numpy as np

def vec_mse(y, y_hat):
	if y.shape != y_hat.shape or len(y) == 0:
		return None
	return dot((y_hat - y) / len(y), (y_hat - y))

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# print("1 -", vec_mse(X, Y))
# print("2 -", vec_mse(X, X))
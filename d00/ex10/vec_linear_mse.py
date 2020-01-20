import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex04")
from dot import dot
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex05")
from mat_vec_prod import mat_vec_prod
import numpy as np

def vec_linear_mse(x, y, theta):
	y = y.reshape(y.shape[0], 1)
	if x.shape[0] != y.shape[0] or x.shape[1] != theta.shape[0] or len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	return dot(((mat_vec_prod(x, theta) - y) / len(y)), (mat_vec_prod(x, theta) - y))[0]


# X = np.array([
# 	[ -6, -7, -9],
# 	[ 13, -2, 14],
# 	[ -7, 14, -1],
# 	[ -8, -4, 6],
# 	[ -5, -9, 6],
# 	[ 1, -5, 11],
# 	[ 9, -11, 8]])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# Z = np.array([3,0.5,-6])

# print("1 -", vec_linear_mse(X, Y, Z))
# # 2641.0
# W = np.array([0,0,0])
# print("2 -", vec_linear_mse(X, Y, W))
# 130.71428571
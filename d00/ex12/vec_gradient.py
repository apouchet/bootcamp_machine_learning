import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex04")
from dot import dot
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex06")
from mat_mat_prod import mat_mat_prod
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex05")
from mat_vec_prod import mat_vec_prod
import numpy as np

def vec_gradient(x, y, theta):
	y = y.reshape(y.shape[0], 1)
	return dot(x / len(y), (mat_vec_prod(x, theta) - y))
	# print(mat_vec_prod(x, theta) - y)


X = np.array([
	[ -6, -7, -9],
	[ 13, -2, 14],
	[ -7, 14, -1],
	[ -8, -4, 6],
	[ -5, -9, 6],
	[ 1, -5, 11],
	[ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
W = np.array([0,0,0])

print("1 -", vec_gradient(X, Y, Z))
print("2 -", vec_gradient(X, Y, W))
print("3 -", vec_gradient(X, X.dot(Z), Z))

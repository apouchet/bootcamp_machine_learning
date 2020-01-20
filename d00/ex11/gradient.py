import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex04")
from dot import dot
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex06")
from mat_mat_prod import mat_mat_prod
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex05")
from mat_vec_prod import mat_vec_prod
import numpy as np

def gradient(x, y, theta):
	res = 0.0
	for i in range(y.shape[0]):
		tmp = np.zeros(x.shape[1])
		for j in range(x.shape[1]):
			tmp[j] = (dot(theta, x[i]) - y[i]) * x[i][j]
		res += tmp
	return res / len(x)


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

print("1 -", gradient(X, Y, Z))
print("2 -", gradient(X, Y, W))
print("3 -", gradient(X, X.dot(Z), Z))
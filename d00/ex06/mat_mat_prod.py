import numpy as np
import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex05")
from mat_vec_prod import mat_vec_prod

def mat_mat_prod(x, y):
	print(x.shape)
	print(y.shape)
	# if x.shape[1] != y.shape[0] or len(x) == 0 or len(y):
	# 	return None
	y.reshape(y.shape[1], y.shape[0])
	for i in range(y.shape[1]):
		if i == 0:
			tab = mat_vec_prod(x, y[:, i]).reshape(y.shape[1], 1)
		else :
			tab = np.append(tab, mat_vec_prod(x, y[:, i]).reshape(y.shape[1], 1), axis=1)
	return tab

# W = np.array([
# 	[ -8, 8, -6, 14, 14, -9, -4],
# 	[ 2, -11, -2, -11, 14, -2, 14],
# 	[-13, -2, -5, 3, -8, -4, 13],
# 	[ 2, 13, -14, -15, -14, -15, 13],
# 	[ 2, -1, 12, 3, -7, -3, -6]])
# Z = np.array([
# 	[ -6, -1, -8, 7, -8],
# 	[ 7, 4, 0, -10, -10],
# 	[ 7, -13, 2, 2, -11],
# 	[ 3, 14, 7, 7, -4],
# 	[ -1, -3, -8, -4, -14],
# 	[ 9, -14, 9, 12, -7],
# 	[ -9, -4, -10, -3, 6]])

# print("me :\n", mat_mat_prod(W, Z))
# print("np :\n", W.dot(Z))

# print("me :\n", mat_mat_prod(Z, W))
# print("np :\n", Z.dot(W))
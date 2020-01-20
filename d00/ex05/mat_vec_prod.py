import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex04")
from dot import dot
import numpy as np

def mat_vec_prod(x, y):
	# print("x =", x.shape)
	# print("y =", y.shape)
	if y.shape[0] != x.shape[1] or x.shape[0] == 0 or x.shape[1] == 0:
		return None
	tab = []
	for i in range(x.shape[0]):
		tab.append(dot(x[i], y.reshape(1, y.shape[0])[0]))
	return np.array(tab).reshape(x.shape[0], 1)

# W = np.array([
#     [ -8, 8, -6, 14, 14, -9, -4],
#     [ 2, -11, -2, -11, 14, -2, 14],
#     [-13, -2, -5, 3, -8, -4, 13],
#     [ 2, 13, -14, -15, -14, -15, 13],
#     [ 2, -1, 12, 3, -7, -3, -6]])
# X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
# Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
# print("me :", mat_vec_prod(W, X))
# print("np :", W.dot(X))
import numpy as np

def mse(y, y_hat):
	if y.shape != y_hat.shape or len(y) == 0:
		return None
	ret = sum((y - y_hat)**2)
	return ret / len(y)

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# Y = np.array([2, 14, -13, 5, 12, 4, -19])
# # X = np.array([])
# # Y = np.array([])
# print("1 -", mse(X, Y))
# print("2 -", mse(X, X))
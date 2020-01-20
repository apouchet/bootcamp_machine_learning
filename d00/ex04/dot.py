import numpy as np

def dot(x, y):
	if len(x) != 0 and len(x) == len(y):
		return sum(x * y)

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
# print("me :", dot(X, Y))
# print("np :", np.dot(X, Y))

# print("me :", dot(X, X))
# print("np :", np.dot(X, X))

# print("me :", dot(Y, Y))
# print("np :", np.dot(Y, Y))
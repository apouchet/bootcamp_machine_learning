import numpy as np

def mean(x):
	np.seterr(all='raise')
	ret = 0.0
	if len(x) == 0:
		return None
	for i in x:
		ret += i
	return ret / len(x)

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# print(mean(X**2))

import sys
sys.path.append("/Users/apouchet/Desktop/ia/bootcamp_ml/d00/ex01")
from mean import mean
import numpy as np

def variance(x):
	m = mean(x)
	if m:
		ret = 0.0
		for i in x:
			ret += (i - m)**2
		return ret / len(x)

X = np.array([0, 15, -9, 7, 12, 3, -21])
# print("me :", variance(X))
# print("np :", np.var(X))
import numpy as np

def sum_(x, f):
	np.seterr(all='raise')
	ret = 0.0
	try:
		if len(x) == 0:
			return None
		for i in x:
			ret += f(i)
	except :
		return None
	return ret

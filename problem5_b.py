from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la
from problem5_a import newton

def fx(x, b) :
	f1 = x[0] * np.sin(x[1]) * np.cos(x[2]) - b[0]
	f2 = x[0] * np.sin(x[1]) * np.sin(x[2]) - b[1]
	f3 = x[0] * np.cos(x[1]) - b[2]
	ff = np.array([f1,f2,f3])
	return ff

def Jacobian(x) :
	J = np.array([	[np.sin(x[1]) * np.cos(x[2]), x[0] * np.cos(x[1]) * np.cos(x[2]), -x[0] * np.sin(x[1]) * np.sin(x[2])],
					[np.sin(x[1]) * np.sin(x[2]), x[0]*np.cos(x[1])*np.sin(x[2]),x[0] * np.sin(x[1]) * np.cos(x[2])],
					[np.cos(x[1]),	-x[0] * np.sin(x[1]) , 0]
				])
	return J

def solve(xyz):
	x0 = [1,1,1]
	x1 = newton(fx, Jacobian, x0, xyz)
	return x1
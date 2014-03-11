from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

def newton(f, J, x0, b = [0,0,0], tol = 1e-12, maxit = 500):
	err = 1.
	i = 0
	while err > tol:
		f0 = f(x0, b)
		J0 = J(x0)
		s0 = -la.solve(J0,f0)
		x1 = x0 + s0
		err = la.norm(s0)
		x0 = x1
		i = i + 1
		if i > maxit :
			break
	return x0

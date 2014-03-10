from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

def newton(func, guess, tol):
	error = 1
	xk = [guess]
	rel_err = 1.
	i = 0
	while error > tol:
		f,df = func(guess)
		temp = guess - (f/df)
		error = abs(guess - temp)
		xk.append(temp)
		guess = temp
		i += 1

	for j in range(2,i-1):
		err1 = abs(xk[j-2] - xk[-1])
		err2 = abs(xk[j-1] - xk[-1])
		err3 = abs(xk[j] - xk[-1])
		rate = np.log(err3/err2)/np.log(err2/err1)

	return xk, rate

def result(func, guess):
	tol = 1e-16
	xk,rate = newton(func, guess, tol)
	print "computed root:",xk[-1]
	print "rate of convergence:"
	print rate,"\n"

def f1(x):
	f = x**2. - 1.
	df = 2. * x
	return f, df

def f2(x):
	f = (x - 1.)**4.
	df = 4. * (x - 1.)**3
	return f, df

def f3(x):
	f = x - np.cos(x)
	df = 1. + np.sin(x)
	return f, df

print "The result for f(x) = x^2 - 1:"
result(f1, 10**6)

print "The result for (x) = (x - 1)^4:"
result(f2, 10)

print "The result for f(x) = x - cos(x):"
result(f3, 1)
from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

def qr_iteration(A, tol):
	m, n = A.shape
	for i in range(0,n-1):
		corner = A[n-i-1][n-i-1]
		q, r = la.qr(A - corner * np.eye(n))
		A = np.dot(r,q)+corner * np.eye(n)
		if la.norm(A[n-i-2][:n-i-2]) < tol:
			break
	return np.diag(A)


A_1 = np.array([[2,3,2], [10,3,4], [3,6,1]])
A_2 = np.array([[6,2,1], [2,3,1], [1,1,1]])
tol = 10e-16

print "Result for A1"
eigenvalues_1 = qr_iteration(A_1.copy(), tol)
print "Computed eigenvalues: ", eigenvalues_1
print "Actual eigenvalues: ", np.linalg.eigvals(A_1)

print "\nResult for A2"
eigenvalues_2 = qr_iteration(A_2.copy(), tol)
print "Computed eigenvalues: ", eigenvalues_2
print "Actual eigenvalues: ", np.linalg.eigvals(A_2)
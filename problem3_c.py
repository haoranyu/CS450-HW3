from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

from problem3_b import reduce_to_hessenberg
np.random.seed(0)
A = np.random.randn(10,10)
Q, U = reduce_to_hessenberg(np.copy(A))

print "U is:"
print U
print "relative error: %g  " % (la.norm(np.dot(np.dot(Q.T, U), Q) - A) / la.norm(A))
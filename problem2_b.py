from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

def lanczos(b, Amul, k, tol=1E-8):
    q0 = 0
    q1 = b / sqrt(np.inner(b.conjugate(), b))
    alpha = np.empty(k)
    beta = np.empty(k)
    beta[-1] = 0.
    for i in xrange(k):
        z = Amul(q1)
        alpha[i] = np.inner(q1.conjugate(), z)
        z -= alpha[i] * q1
        z -= beta[i-1] * q0
        beta[i] = sqrt(np.inner(z.conjugate(), z)).real
        if beta[i] < tol:
            return alpha[:i+1].copy(), beta[:i].copy()
        z /= beta[i]
        q0, q1 = q1, z
    return alpha, beta[:-1]
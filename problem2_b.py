from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

def lanczos(A):
    m,n = np.shape(A)
    Q = np.zeros((m,n))
    p0 = 0
    x0 = np.random.randn(n)
    Q[:,0] = x0/(la.norm(x0))
    alpha = np.zeros(n)
    U = np.zeros((m,n))
    H = np.zeros((m,n))
    
    for i in range(0,n):
        U[:,i] = np.dot(A,Q[:,i])
        alpha = np.dot(Q[:,i].T,U[:,i])
        U[:,i] = U[:,i]-p0*Q[:,i-1]-alpha*Q[:,i]
        p0 = la.norm(U[:,i])
        H[i,i] = alpha
        if(i+1<n):
            H[i+1,i] = p0
            H[i,i+1] = p0
        if p0 == 0:
            break
        if(i+1<n):
            Q[:,i+1]=U[:,i]/p0

    return Q,H
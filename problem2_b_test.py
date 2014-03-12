from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la
from problem2_b import lanczos

def lanczos(A):
    m,n = np.shape(A)
    Q = np.zeros((m,n))
    beta = 0
    x0 = np.random.randn(n)
    Q[:,0] = x0/(la.norm(x0))
    alpha = np.zeros(n)
    U = np.zeros((m,n))
    H = np.zeros((m,n))
    
    for i in range(0,n):
        U[:,i] = np.dot(A,Q[:,i])
        alpha = np.dot(Q[:,i].T,U[:,i])
        U[:,i] = U[:,i]-beta*Q[:,i-1]-alpha*Q[:,i]
        beta = la.norm(U[:,i])
        H[i,i] = alpha
        if(i+1<n):
          	H[i+1,i] = beta
          	H[i,i+1] = beta
        if beta == 0:
          	break
        if(i+1<n):
          	Q[:,i+1]=U[:,i]/beta

    return Q,H


np.random.seed(0)
B = np.random.randn(10,10)
A = B + B.T

Q, H = lanczos(np.copy(A))

print la.norm(np.dot(Q,Q.T) - np.eye(10))
print la.norm(np.dot(Q.T,A).dot(Q) - H) / la.norm(A)
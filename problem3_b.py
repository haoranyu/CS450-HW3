from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la

def house(x):
    sigma = np.sqrt(np.dot(x.T,x))[0,0]
    
    v = x.copy()
    if x[0] <= 0:
        v[0] -= sigma

    else:
        v[0] += sigma
    
    v = v/v[0]
    beta = 2./np.dot(v.T,v)[0,0]
    
    return v, beta

def house_reflector(A):
    m,n = A.shape
    A = np.copy(A[1:m,0:(n-1)])
    m,n = A.shape
    q = np.eye(m)
    H = np.zeros((m,m))
    H_matrix = []
    for k in range(n):
        v,beta = house(A[k:,k:k+1])
        A[k:,k:] -= beta * np.dot(v, np.dot(v.T,A[k:,k:]))
        H[...] = np.eye(m)
        H[k:,k:] -= beta * np.dot(v,v.T)
        Q = np.eye(m+1)
        Q[1:,1:] = H
        H_matrix.append(np.copy(Q))
        q = np.dot(q,H)

    return H_matrix

def reduce_to_hessenberg(A):
    m, n = A.shape
    U = A
    P_list = []
    
    for i in range(m-1):
        H = house_reflector(np.copy(U))
        P = H[i]
        P_list.append(np.copy(P))
        U = np.dot(np.dot(P,U),P.T)

    Q = np.eye(m)
    for i in range(len(P_list)):
        Q = np.dot(P_list[i], Q)

    return Q, U
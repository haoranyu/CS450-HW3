from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from problem2_b import lanczos

def lanczos_eig(A):
    m,n = np.shape(A)
    Q = np.zeros((m,n))
    beta = 0
    x0 = np.random.randn(n)
    Q[:,0] = x0/(la.norm(x0))
    alpha = np.zeros(n)
    gama = []
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
        gama.append(np.copy(la.eigvals(H).T))

    return gama

def plot_init():
	plt.clf()
	plt.xlabel("k axis")
	plt.ylabel("ri axis")
	plt.title("Plot for Problem2 c)")
	plt.hold(True)
	plt.gca().set_aspect("equal")

np.random.seed(0)
n = 32
B = np.random.randn(n, n)
Q, R = la.qr(B)

D = np.zeros(n)
for i in range(n):
	D[i] = i + 1
Di = np.diag(D)
A = np.dot(Q,Di).dot(Q.T)

eig = lanczos_eig(np.copy(A))

plot_init()
for i in range(n):
	test = np.zeros(n)
	for j in range(n):
		test[j] = eig[j][i]
	plt.scatter(np.copy(D), test, s= 0.5)

plt.savefig("problem5_d.png")
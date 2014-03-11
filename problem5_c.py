from __future__ import division
import scipy as sp
import numpy as np
import numpy.linalg as la
from problem5_b import solve

def print_residual(xyz, rp):
	x_ = rp[0] * np.sin(rp[1]) * np.cos(rp[2])
	y_ = rp[0] * np.sin(rp[1]) * np.sin(rp[2])
	z_ = rp[0] * np.cos(rp[1])
	print "Final relative residual: %g " % (la.norm(np.array([x_, y_, z_]).T - np.array(xyz).T)/la.norm(np.array(xyz).T))

def print_pol_res(xyz, rp):	
	r = np.sqrt(xyz[0] ** 2 + xyz[1] ** 2 + xyz[2] ** 2)
	theta = np.arccos(xyz[2]/r)
	phi = np.arctan2(xyz[1], xyz[0])
	print "Final relative error: %g \n" % (la.norm(np.array([r, theta, phi]).T - np.array(rp).T)/la.norm(np.array([r, theta, phi]).T))

for i in range(0,10):
	np.random.seed(i)
	xyz = np.random.randn(3)
	rthetaphi = solve(xyz)

	print "random x, y, z = "
	print xyz
	print "r, theta, phi = "
	print rthetaphi
	print_residual(xyz, rthetaphi)
	print_pol_res(xyz, rthetaphi)
	
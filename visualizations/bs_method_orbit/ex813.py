'''
date: 08/01/22
exercise: 8.13

desc: solving and visualizing earth's and pluto's orbits about the sun 
using the bulirsch-stoer method with combined modified midpoint/richardson extrapolation 
'''

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

G,M = 6.6738e-11*(3600*24*7*52)**2, 1.9891e30
N = 52 
delta = 1.0*10e3

dw = lambda r: -G*M*r[0]/sqrt(r[0]**2 + r[1]**2)**3
dz = lambda r: -G*M*r[1]/sqrt(r[0]**2 + r[1]**2)**3
f = lambda r: np.array( [r[2],r[3],dw(r),dz(r)] ) 


def bs():
    for t in range(N-1):

        n = 1
        r1 = r[:,t] + 0.5*H*f(r[:,t])
        r2 = r[:,t] + H*f(r1)
        R1 = np.empty((4,1),float)
        R1[:,0] = 0.5*(r1+r2+0.5*H*f(r2))
        error = 2*H*delta
        while error>H*delta:
            n = n + 1
            h = H/n
            
            r1 = r[:,t] + 0.5*h*f(r[:,t])
            r2 = r[:,t] + h*f(r1)
            for i in range(n-1):
                r1 += h*f(r2)
                r2 += h*f(r1)

            R2 = R1[:,:]
            R1 = np.empty((4,n),float)
            R1[:,0] = 0.5*(r1+r2+0.5*h*f(r2))
            for m in range(1,n):
                ep = (R1[:,m-1]-R2[:,m-1])/((n/(n-1))**(2*m)-1)
                R1[:,m] = R1[:,m-1] + ep
            error = abs(np.linalg.norm(ep[0:1]))
            #print(error)
        r[:,t+1] = R1[:,n-1]
    return r

r = np.empty((4,N),float)
t0,tf = 0.0,1.1 # earth times
H = (tf-t0)/N
t_points = np.arange(t0,tf,H)
r[:,0] = [1.471e11,0,0,3.0287e4*(3600*24*7*52)] # earth initial conditions
earth_r = bs()

t0,tf = 0.0,260 # pluto times
H = (tf-t0)/N
t_points = np.arange(t0,tf,H)
r = np.empty((4,N),float)
r[:,0] = [4.4368e12,0,0,6.1218e3*(3600*24*7*52)] # pluto initial conditions 
pluto_r = bs()

fig,ax = plt.subplots(1)
ax.plot(earth_r[0,:],earth_r[1,:],c='blue')
ax.plot(pluto_r[0,:],pluto_r[1,:],c='orange')
ax.set(xlabel='x distance from sun',ylabel='y distance from sun',title="earth and pluto's orbit about the sun")
plt.show()
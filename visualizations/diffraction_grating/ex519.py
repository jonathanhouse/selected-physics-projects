'''
date: 05/17/22
exercise: 5.19

desc: visualize diffraction gratings of different transmission functions (named q0 to q3)
by solving solving the associated integral using gauss-legendre quadrature 
'''

from numpy import polynomial
import numpy as np
import matplotlib.pyplot as plt
from math import sin,sqrt,pi
from cmath import exp

d = 20e-6
wl = 500e-9
f = 1
wg = d*10
wd = 10e-2
N = 700
alpha = pi/d
beta = 0.5*alpha

# transmission functions q(u)

q0 = lambda u: pow(sin(alpha*u),2)

q1 = lambda u: pow(sin(alpha*u),2)*pow(sin(beta*u),2)


# two equally spaced slits with 100% transmission
def q2(u):
    db,da = d,d-1e-6
    if (u <= db and u >= da):
        return 1.0
    if (u >= -(db) and u <= -(da)):
        return 1.0
    return 0.0


# two slits 60 um apart (one of width 10 um and the other 20 um)
def q3(u):
    db,da = d,d-1e-6
    if (u <= 30e-6+10e-6 and u >= 30e-6):
        return 1.0
    if (u >= -(30e-6+20e-6) and u <= -(30e-6)):
        return 1.0
    return 0.0


def I(x):
    N = 500
    b,a = wg/2,-wg/2
    j = complex(0,1)
    ft = lambda u: sqrt(q0(u))*exp((j*2*pi*x*u)/(wl*f))
    u,w = polynomial.legendre.leggauss(N)
    up = 0.5*(b-a)*u + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    s = 0.0
    for i in range(N):
        s += wp[i]*ft(up[i])
    return abs(s)**2.0

x = np.linspace(-wd/2.0,wd/2.0,N)
i0 = np.empty(shape=(N))
i = np.empty(shape=(10,N))
for k in range(N):
    i0[k] = I(x[k])
i = np.tile(i0,(200,1))


plt.imshow(i)
plt.hot()
#plt.plot(x,i0)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

G = 1.0
M = 10.0
L = 2.0
t0,tf = 0.0,10.0
N = 5000
t_points = np.linspace(t0,tf,N)
h = (tf-t0)/N

r = np.empty((4,N),float)
r[:,0] = [1,0,0,1]

def dw(r):
    mag = sqrt(r[0]**2 + r[1]**2)
    return -G*M*r[0]/(sqrt(mag**2+L**2/4)*mag**2)
def dz(r):
    mag = sqrt(r[0]**2 + r[1]**2)
    return -G*M*r[1]/(sqrt(mag**2+L**2/4)*mag**2)
f = lambda r,t: np.array( [r[2],r[3],dw(r),dz(r)] )

def runge_kutta(r,f):
    for t in range(N-1):
        rt = r[:,t]
        tt = t_points[t]
        k1 = h*f(rt,t)
        k2 = h*f(rt+0.5*k1,tt+0.5*h)
        k3 = h*f(rt+0.5*k2,tt+0.5*h)
        k4 = h*f(rt+k3,tt+h)
        r[:,t+1] = rt + (k1 + 2*k2 + 2*k3 + k4)/6.0
    return r

x,y,w,z = runge_kutta(r,f)
fig,ax = plt.subplots(1)
fig.set_figheight(6)
fig.set_figwidth(6)
ax.plot(x,y)
ax.set(xlabel='x',ylabel='y',title='processing orbit')

plt.show()
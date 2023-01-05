'''
date: 07/26/22
exercise: 8.07

desc: solving and visualizing trajectories for a spherical cannonball of different masses using 
fourth-order runge-kutta method. 
'''

import numpy as np
import matplotlib.pyplot as plt
from math import pi,radians,cos,sin,sqrt

R = 0.08 # radius of sphere 
m = 1 # mass of sphere
rho = 1.22 # density of air
C = 0.47 # coeffecient of drag 
g = 9.8 

theta = radians(30)
vx0 = 100*cos(theta)
vy0 = 100*sin(theta)
N = 5000
t0,tf = 0.0,50.0
t_points = np.linspace(t0,tf,N)
h = (tf-t0)/N

r = np.empty((4,N),float)
r[:,0] = [0,0,vx0,vy0]
dw = lambda w,z: (-pi*rho*C*R**2)/(2*m)*w*sqrt(w**2 + z**2)
dz = lambda w,z: -g - (pi*rho*C*R**2)/(2*m)*z*sqrt(w**2 + z**2)
f = lambda r,t: np.array( [r[2],r[3],dw(r[2],r[3]),dz(r[2],r[3])] )

def runge_kutta(r,f):
    for t in range(N-1):
        k1 = h*f(r[:,t],t_points[t])
        k2 = h*f(r[:,t]+0.5*k1,t_points[t]+0.5*h)
        k3 = h*f(r[:,t]+0.5*k2,t_points[t]+0.5*h)
        k4 = h*f(r[:,t]+k3,t_points[t]+h)
        r[:,t+1] = r[:,t] + (k1 + 2*k2 + 2*k3 + k4)/6.0
    return r

r = runge_kutta(r,f)
fig,ax = plt.subplots(1)
ax.set(title='mass trajectories under air resistance')
ax.plot(r[0,:],r[1,:],c='red',label='1 kg')

m = 10
r = runge_kutta(r,f)
ax.plot(r[0,:],r[1,:],c='green',label='10 kg')

m = 100
r = runge_kutta(r,f)
ax.plot(r[0,:],r[1,:],c='orange',label='100 kg')

ax.set(xlabel='x',ylabel='y',ylim=[0,300],xlim=[0,1000])
ax.legend()

plt.show()

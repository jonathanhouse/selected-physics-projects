'''
date: 07/26/22
exercise: 8.09 

desc: solves 1-dimensional vibrational system of N masses using fourth-order runge-kutta and animates the results 
'''

import numpy as np
import matplotlib.pylab as plt
from math import cos
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

m,k,w = 1.0,6.0,2.0
t0,tf = 0.0,20.0
points = 1000
h = (tf-t0)/points
t_points = np.linspace(t0,tf,points)

N = 10
F1 = lambda t: cos(w*t)
r = np.empty((2*N,points),float)
r[:,0] = np.zeros(2*N)

dx1 = lambda rn,t: (1/m)*( k*(rn[1]-rn[0]) + F1(t) ) 
dxi = lambda rn,t: (1/m)*( k*(rn[2]-rn[1]) + k*(rn[0]-rn[1]) + 0)
dxN = lambda rn,t: (1/m)*( k*(rn[0]-rn[1]) + 0 )

def f(r,t):
    s = np.empty(2*N,float)
    s[0:N] = r[N:2*N]
    for n in range(N,2*N):
        if n == 0 + N: s[n] = dx1(r[n-N:n-N+2],t)
        elif n == N-1 + N: s[n] = dxN(r[n-N-1:n-N+1],t)
        else: s[n] = dxi(r[n-N-1:n-N+2],t)
    return s

def runge_kutta(r,f):
    for t in range(points-1):
        rt = r[:,t]
        tt = t_points[t]
        k1 = h*f(rt,tt)
        k2 = h*f(rt+0.5*k1,tt+0.5*h)
        k3 = h*f(rt+0.5*k2,tt+0.5*h)
        k4 = h*f(rt+k3,tt+h)
        r[:,t+1] = rt + (k1+2*k2+2*k3+k4)/6.0
    return r

r = runge_kutta(r,f)

# plots all displacement on one axes 
'''
fig,ax = plt.subplots(1)
for n in range(1):
    ax.plot(t_points,r[n,:])
'''

fig,ax = plt.subplots(1)
balls_x = np.arange(0,N)
balls_y = np.zeros(N)
balls, = ax.plot(balls_x,balls_y,'wo',zorder=N)
displace_x = r
springs = [ax.plot([],[],zorder=n) for n in range(N-1)]

def init():
    balls.set_data([],[])

def animation(t):
    balls_xt = np.arange(0,N) + displace_x[0:N,t]
    balls.set_data(balls_xt,balls_y)
    for n in range(N-1):
        springs[n][0].set_data([balls_xt[n],balls_xt[n+1]],[0,0])


anim = FuncAnimation(fig,animation,frames=points,init_func=init,interval=5)
ax.set(xlim=[-1,10],yticks=[],xlabel='x',title='mass displacement')

plt.show()

'''
date: 07/24/22
exercise: 8.04

desc: solves the undriven, nonlinear pendulum problem using fourth-order runge-kutta, and animates the system 
'''

import matplotlib.pyplot as plt
import numpy as np
from math import sin,radians,cos
from matplotlib.animation import FuncAnimation

g = 9.8
l = 0.1
theta = radians(179.0)
N = 5000
a = 0.0
b = 10.0
h = (b-a)/N

r = np.empty((2,N),float)
f = lambda r,t: np.array( [r[1],(-g/l)*sin(r[0])],float)
r[:,0] = [theta,0]
t_points = np.linspace(a,b,N)

# solves diff eq and plots t vs theta
#for t in range(N-1):
#    k1 = h*f(r[:,t],t_points[t])
#    k2 = h*f(r[:,t]+0.5*k1,t_points[t]+0.5*h)
#    k3 = h*f(r[:,t]+0.5*k2,t_points[t]+0.5*h)
#    k4 = h*f(r[:,t]+k3,t_points[t]+h)
#    r[:,t+1] = r[:,t] + (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)

#fig,ax = plt.subplots(1)
#ax.plot(t_points,r[0,:])
#plt.show()

rad = 0.01
fig,ax = plt.subplots(1,figsize=(6,6))
ax.set(xticks=[],yticks=[])
ax.set_xlim(-0.2,0.2)
ax.set_ylim(-0.2,0.2)

rod = ax.plot([],[],lw=2,c='k',zorder=0)[0]
ball = plt.Circle([0.5,0.5],radius=rad,zorder=1,color='red')
draw_ball = ax.add_patch(ball)

#rod, = ax.plot([],[],lw=2)[0] # this works too

def init():
    ball.set(visible=False)
    rod.set_data([],[])

ball_pos = lambda theta: np.array([l*sin(theta),-l*cos(theta)])
ball_data = np.empty((2,N),float)
ball_data[:,0] = ball_pos(theta)

def animate(t):
    #t = int(i) 
    k1 = h*f(r[:,t],t_points[t])
    k2 = h*f(r[:,t]+0.5*k1,t_points[t]+0.5*h)
    k3 = h*f(r[:,t]+0.5*k2,t_points[t]+0.5*h)
    k4 = h*f(r[:,t]+k3,t_points[t]+h)
    r[:,t+1] = r[:,t] + (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    ball_data[:,t+1] = ball_pos(r[0,t+1])
    ball.set(center=[ball_data[0,t+1],ball_data[1,t+1]],visible=True)
    rod.set_data(np.linspace(0,ball_data[0,t+1],N),(0-ball_data[1,t+1])/(0-ball_data[0,t+1])*np.linspace(0,ball_data[0,t+1],N))

anim = FuncAnimation(fig,animate,frames=N-1,init_func=init,interval=7)
plt.show()
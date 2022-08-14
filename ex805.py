import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos,radians
from matplotlib.animation import FuncAnimation

theta = 0
l = 0.1
C = 2
ohm = 5
# ohm = 10 # resonant freq case
t0 = 0.0
tf = 100.0
N = 5000
h = (tf-t0)/N
g = 9.8
f = lambda r,t: np.array([r[1],(-g/l)*sin(r[0]) + C*cos(r[0])*sin(ohm*t)])

r = np.empty((2,N),float)
r[:,0] = [0,0]
t_points = np.linspace(t0,tf,N)

# solves diff eq and plots t vs theta
'''
for t in range(N-1):
    k1 = h*f(r[:,t],t_points[t])
    k2 = h*f(r[:,t] + 0.5*k1, t_points[t] + 0.5*h)
    k3 = h*f(r[:,t] + 0.5*k2, t_points[t] + 0.5*h)
    k4 = h*f(r[:,t] + k3, t_points[t] + h)
    r[:,t+1] = r[:,t] + (k1 + 2*k2 + 2*k3 + k4)/6.0

fig,ax = plt.subplots(1)
ax.plot(t_points,r[0,:])
ax.set(xlim=[0,10])
plt.show()
'''




rad = 0.01
fig,ax = plt.subplots(1,figsize=(6,6))
ax.set(xticks=[],yticks=[])
ax.set_xlim(-0.2,0.2)
ax.set_ylim(-0.2,0.2)

rod = ax.plot([],[],lw=2,c='k',zorder=0)[0]
ball = plt.Circle([0.5,0.5],radius=rad,zorder=1,color='gray')
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

anim = FuncAnimation(fig,animate,frames=N-1,init_func=init,interval=15)
plt.show()
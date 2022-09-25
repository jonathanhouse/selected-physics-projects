import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

l = 0.4 
m = 1
g = 9.8
t0,tf = 0.0,100.0
N = 10000
h = 1e-3
t_points = np.linspace(t0,tf,N)
r = np.empty((4,N),float)
r[:,0] = [pi/2,pi/2,0,0]

dw1 = lambda r: -( pow(r[2],2)*sin(2*r[0]-2*r[1]) + 2*pow(r[3],2)*sin(r[0]-r[1]) + (g/l)*(sin(r[0]-2*r[1]) + 3*sin(r[0]))  )/( 3 - cos(2*r[0]-2*r[1]) )
dw2 = lambda r: ( 4*pow(r[2],2)*sin(r[0]-r[1]) + pow(r[3],2)*sin(2*r[0]-2*r[1]) + 2*(g/l)*(sin(2*r[0]-r[1]) - sin(r[1]))  )/( 3 - cos(2*r[0]-2*r[1]) )
f = lambda r,t: np.array( [r[2],r[3],dw1(r),dw2(r)] )

for t in range(N-1):
    rt = r[:,t]
    tt = t_points[t]
    k1 = h*f(rt,tt)
    k2 = h*f(rt+0.5*k1,tt+0.5*h)
    k3 = h*f(rt+0.5*k2,tt+0.5*h)
    k4 = h*f(rt+k3,tt+h)
    r[:,t+1] = rt + (k1 + 2*k2 + 2*k3 + k4)/6.0


E = [-m*g*l*(2*cos(2*r[0,t])+cos(r[1,t])) + m*pow(l,2)*(r[2,t]**2 + 0.5*r[3,t]**2 + r[2,t]*r[3,t]*cos(r[0,t]-r[1,t])) for t in range(N)]
plt.plot(t_points,E)
plt.show() 

n = 1000
fig,ax = plt.subplots(1,figsize=(7,6))
pos1 = np.array ( [[ l*sin(r[0,t]) for t in range(N) ],[-l*cos(r[0,t]) for t in range(N)]])
pos2 = np.array([[l*(sin(r[0,t])+sin(r[1,t])) for t in range(N) ],[-l*(cos(r[0,t])+cos(r[1,t])) for t in range(N)]])
pivot, = ax.plot([0],[0],'wo',zorder=2)
m1, = ax.plot(pos1[0,0],pos1[1,0],color='magenta',marker='o',zorder=1)
m2, = ax.plot(pos2[0,0],pos2[1,0],color='magenta',marker='o',zorder=1)
r1, = ax.plot(np.linspace(0,pos1[0,0],n),np.linspace(0,pos1[0,0],n)*pos1[1,0]/pos1[0,0],'w',zorder=0)
m = (pos2[1,0]-pos1[1,0])/(pos2[0,0]-pos1[0,0])
b = pos1[1,0] - m*pos1[0,0]
r2, = ax.plot(np.linspace(pos1[0,0],pos2[0,0],n),m*np.linspace(pos1[0,0],pos2[0,0],n)+b,'w',zorder=0)

def init():
    m1.set_data([],[])
    m2.set_data([],[])
    r1.set_data([],[])
    r2.set_data([],[])

def animate(t):
    m1.set_data(pos1[0,t],pos1[1,t])
    m2.set_data(pos2[0,t],pos2[1,t])
    r1.set_data(np.linspace(0,pos1[0,t],n),np.linspace(0,pos1[0,t],n)*pos1[1,t]/pos1[0,t])
    m = (pos2[1,t]-pos1[1,t])/(pos2[0,t]-pos1[0,t])
    b = pos1[1,t] - m*pos1[0,t]
    r2.set_data(np.linspace(pos1[0,t],pos2[0,t],n),np.linspace(pos1[0,t],pos2[0,t],n)*m+b)

ax.set(xlim=[-1,1],ylim=[-1,0.4],xticks=[],yticks=[],title='double pendulum')
anim = FuncAnimation(fig,animate,frames=N,init_func=init,interval=1)
plt.show()
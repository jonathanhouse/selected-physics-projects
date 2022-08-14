import numpy as np
import matplotlib.pyplot as plt
from random import random,randrange
from math import exp
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

N = 20
J,T,kb = 1,1,1
s = np.empty((N,N),int)
Nt = 100000

def E(s):
    Et = 0.0
    for n in range(N-1):
        Et += -J*np.dot(s[n,:],s[n+1,:]) + -J*np.dot(s[:,n],s[:,n+1])
    return Et

def s_init(s):
    for i in range(N):
        for j in range(N):
            if random()>0.5: s[i,j] = 1
            else: s[i,j] = -1
    return s

def metropolis(s):
    i,j = randrange(N),randrange(N)
    a = random()
    E0 = E(s)
    s[i,j] *= -1
    E1 = E(s)
    dE = E1 - E0

    if a<exp(-dE/T): return s
    s[i,j] *= -1
    return s

def magnetization(s):
    return np.sum(s)

def spin_vect(s):
    up = [[],[]]
    down = [[],[]]
    for i in range(N):
        for j in range(N):    
            if s[i,j] == 1: up[0].append(i); up[1].append(j)
            else: down[0].append(i); down[1].append(j)
    return up,down

s = s_init(s)
fig,ax = plt.subplots(1)
ax.set(xticks=[],yticks=[],title='ising model')

t_points = np.linspace(0,Nt,Nt)
m = []
#ax.plot(t_points,m)

up,down = spin_vect(s)
spin_up, = ax.plot(up[0],up[1],'ro',markersize=10)
spin_down, = ax.plot(down[0],down[1],'bo',markersize=10)


def init():
    spin_up.set_data([],[])
    spin_down.set_data([],[])

def animate(t):
    s[:,:] = metropolis(s)[:,:]
    #m.append(magnetization(s))
    up,down = spin_vect(s)
    spin_up.set_data(up[0],up[1])
    spin_down.set_data(down[0],down[1])


anim = FuncAnimation(fig,animate,frames=Nt,interval=1,init_func=init)

plt.show()
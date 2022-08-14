from random import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

L = 101
i,j = L//2,L//2
Nt = int(10e6)

fig,ax = plt.subplots(1)
ax.set(xlim=[0,L],ylim=[0,L],xticks=[],yticks=[],title='brownian motion')
r = np.array( [i,j],int )
p = [i],[j]
path, = ax.plot(p[0],p[0],color='cornflowerblue')
#walk, = ax.plot(r[0],r[1],'mo',markersize=5)

def random_walk(r):
    i,j = r[0],r[1]
    while True:
        z = random()
        if z<0.25 and i+1<L: return np.array( [1,0] )
        elif z>=0.25 and z<0.5 and i-1>=0: return np.array( [-1,0] )
        elif z>=0.5 and z<0.75 and j+1<L: return np.array( [0,1] )
        elif z>= 0.75 and j-1>=0: return np.array( [0,-1] )

def animate(t):
    r[:] += random_walk(r)
    p[0].append(r[0])
    p[1].append(r[1])
    path.set_data(p[0],p[1])
    #walk.set_data(r[0],r[1])

anim = FuncAnimation(fig,animate,frames=Nt,interval=30)
plt.show()


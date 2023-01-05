'''
date: 08/10/22
exercise: 10.11

desc: solves the dimer covering problem using a temperature to allow annealing, and animates
the process of finding the optimal layout for dimers to maximally occuy the grid 
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
from math import exp
from random import random,randrange

T0,Tf,tau = 100,0.1,50000
T = lambda t: T0*exp(-t/tau)


N = 50
Nt = 500000
lattice = np.zeros((N,N),float)
ep = 1e-10
dt = 1
t = 0.0

def count_dimers(l):
    c = np.unique(l)
    c = [c[i] for i in range(len(c)) if c[i] > 0.0]
    dimers_index = np.transpose(np.nonzero(l))
    return -len(c),dimers_index

Tc = T(t)
fig,ax = plt.subplots(1)

dimers, = ax.plot([],[],'ko')
ax.set(xlim=[-1,50],ylim=[-1,50],xticks=[],yticks=[],title='the dimer covering problem')

def init():
    dimers.set_data([],[])


def animate(t):
    Tc = T(t*dt)
    if Tc<Tf: dimers.set_data(dimers[:,:,0],dimers[:,:,1]); print(c);return
    i,j = randrange(0,N),randrange(0,N)
    ia,ja = -1,-1
    c0,q = count_dimers(lattice)
    while ia<0 and ja<0:
        z = random()
        if z<0.25 and j>0: ia,ja = i,j-1
        elif z>=0.25 and z<0.5 and j<N-1: ia,ja = i,j+1
        elif z<=0.5 and z<0.75 and i>0: ia,ja = i-1,j
        elif z>=0.75 and i<N-1: ia,ja = i+1,j
    i_val = lattice[i,j]
    ia_val = lattice[ia,ja]
    if abs(i_val-ia_val)<ep and i_val==0.0:
        z = random()
        lattice[ia,ja] = z
        lattice[i,j] = z
    elif abs(i_val-ia_val)<ep and i_val>0.0:
        lattice[ia,ja] = 0.0
        lattice[i,j] = 0.0
        cf,q = count_dimers(lattice)
        dc = cf-c0
        if random()>exp(-dc/Tc): 
            z = random()
            lattice[ia,ja] = z
            lattice[i,j] = z
    c,dimer_indicies = count_dimers(lattice)
    dimers.set_data(dimer_indicies[:,0],dimer_indicies[:,1])
    print(str( (1-Tc/T0) * 100) + '% cooled & ' + str(c*-1) + ' dimers')

anim = FuncAnimation(fig,animate,interval=10,frames=Nt)
plt.show()
'''
# plots count over time 

x = [0]
t_points = [0]
while Tf<Tc:
    if Tc<Tf: break
    i,j = randrange(0,N),randrange(0,N)
    ia,ja = -1,-1
    c0,q = count_dimers(lattice)
    while ia<0 and ja<0:
        z = random()
        if z<0.25 and j>0: ia,ja = i,j-1
        elif z>=0.25 and z<0.5 and j<N-1: ia,ja = i,j+1
        elif z<=0.5 and z<0.75 and i>0: ia,ja = i-1,j
        elif z>=0.75 and i<N-1: ia,ja = i+1,j
    i_val = lattice[i,j]
    ia_val = lattice[ia,ja]
    if abs(i_val-ia_val)<ep and i_val==0.0:
        z = random()
        lattice[ia,ja] = z
        lattice[i,j] = z
    elif abs(i_val-ia_val)<ep and i_val>0.0:
        lattice[ia,ja] = 0.0
        lattice[i,j] = 0.0
        cf,q = count_dimers(lattice)
        dc = cf-c0
        if random()>exp(-dc/Tc): 
            z = random()
            lattice[ia,ja] = z
            lattice[i,j] = z
    c,dimer_indicies = count_dimers(lattice)
    t += dt
    Tc = T(t)
    x.append(-1*c)
    t_points.append(t)

ax.plot(t_points,x,'.')
plt.show()
'''
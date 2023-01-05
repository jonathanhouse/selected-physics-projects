'''
date: 08/17/22
exercise: 9.08

desc: animates and solves the schrödinger wave equation for a particle in an inpenetrable box by creating
a fast banded matrix elimination and using the crank-nicolson method
'''

import numpy as np
import matplotlib.pyplot as plt
from cmath import exp
from matplotlib.animation import FuncAnimation

def banded(A1,v1):
    A = np.copy(A1)
    v = np.copy(v1)
    N = len(v)

    for m in range(N-1): # tridiagonal gaussian elim
        div = A[m,m]
        v[m] /= div
        v[m+1] = v[m+1] - A[m+1,m]*v[m]

        A[m,:] /= div
        A[m+1,:] -= A[m+1,m]*A[m,:]
    
    for m in range(N-2,-1,-1): # backsubstitution 
        v[m] -= v[m+1]*A[m,m+1]
    return v


Nx = 1000
L = 1e-8
a = L/Nx
h = 1e-18
Nt = 2000
j = complex(0,1)

hbar,m = 1.05457e-34,9.109e-31
x0,sigma,k = L/2,1e-10,5e10
psi_init = lambda x: exp( -(x-x0)**2/(2*sigma**2) )*exp(j*k*x)
psi = np.zeros((Nx,Nt),complex)
psi[:,0] = np.array( list(map(psi_init,np.linspace(0.0,L,Nx))) )
psi[0,:] = 0.0
psi[Nx-1,:] = 0.0

a1,a2 = 1+h*j*hbar/(2*m*a**2),-h*j*hbar/(4*m*a**2)
b1,b2 = 1-h*j*hbar/(2*m*a**2), h*j*hbar/(4*m*a**2)
A = np.zeros((Nx-2,Nx-2),complex)

A[0,0:2] = [a1,a2] 
A[Nx-3,Nx-4:Nx-2] = [a2,a1]
for i in range(1,Nx-3):
    A[i,i-1:i+2] = [a2,a1,a2] 

v = np.empty(Nx-2,complex)
for t in range(Nt-1):
    v[:] = b1*psi[1:Nx-1,t] + b2*( psi[2:Nx,t] + psi[0:Nx-2,t] )
    psi[1:Nx-1,t+1] = banded(A,v)

fig,ax = plt.subplots(1)
ax.set(xlim=[0,1e-8],ylim=[-1,1])
wv, = ax.plot([],[])

def init():
    wv.set_data([],[])
def animate(t):
    wv.set_data([np.linspace(0.0,L,Nx)],[abs(psi[:,t])])

anim = FuncAnimation(fig,animate,init_func=init,interval=1,frames=Nt)
plt.show()

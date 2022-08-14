import numpy as np
import matplotlib.pyplot as plt
from cmath import exp
from numpy import real,imag
from scipy.fftpack import dst,idst
from math import pi,cos,sin
from matplotlib.animation import FuncAnimation

Nx = 10000
L = 1e-8
a = L/Nx
h = 1e-18
Nt = 2000
j = complex(0,1)
x_points = np.linspace(0.0,L,Nx)

hbar,m = 1.05457e-34,9.109e-31
x0,sigma,k = L/2,1e-10,5e10
psi_init = lambda x: exp( -(x-x0)**2/(2*sigma**2) )*exp(j*k*x)
psi = np.zeros(Nx,complex)
psi[:] = np.array( list(map(psi_init,np.linspace(0.0,L,Nx))) )
psi[0] = 0.0
psi[Nx-1] = 0.0

psi_real = [ real(psi[k]) for k in range(Nx) ]
psi_imag = [ imag(psi[k]) for k in range(Nx) ]
ck_real = dst(psi_real)
ck_imag = dst(psi_imag)
inv_ck = lambda t: idst( [ ck_real[k]*cos(pi**2*hbar*k**2/(2*m*L**2)*t) - ck_imag[k]*sin(pi**2*hbar*k**2/(2*m*L**2)*t) for k in range(Nx)] )


fig,ax = plt.subplots(1)
#ax.plot(x_points,inv_ck(0))

ax.set(xlim=[0,1e-8],ylim=[-1,1])
wv, = ax.plot([],[])

def init():
    wv.set_data([],[])

def animate(t):
    wv.set_data(x_points,inv_ck(h*t))

anim = FuncAnimation(fig,animate,init_func=init,frames=Nt,interval=10)
plt.show()
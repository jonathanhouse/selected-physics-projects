'''
date: 07/25/22
exercise: 8.06

desc: solve and plot the harmonic and anharmonic oscillator differential equations with different initial conditions, 
and visualize the anharmonic oscillator and van der Pol oscillator phase spaces 
'''
import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 50.0
N = 5000
w = 1

t_points = np.linspace(t0,tf,N)
r0 = np.empty((2,N),float)
r0[:,0] = [1,0]
f = lambda r,t: np.array([r[1],-pow(w,2)*r[0]])

def solve(r,f):
    h = (tf-t0)/N
    for t in range(N-1):
        k1 = h*f(r[:,t],t_points[t])
        k2 = h*f( r[:,t] + 0.5*k1,t_points[t] + 0.5*h )
        k3 = h*f( r[:,t] + 0.5*k2,t_points[t] + 0.5*h )
        k4 = h*f( r[:,t] + k3,t_points[t] + h )
        r[:,t+1] = r[:,t] + (k1 + 2*k2 + 2*k3 + k4)/6.0
    return r


r0 = solve(r0,f)
fig,ax = plt.subplots(4,sharex=True)
plt.subplots_adjust(wspace=0.75)
ax[0].plot(t_points,r0[0,:])

r1 = np.empty((2,N),float)
r1[:,0] = [2,0]
r1 = solve(r1,f)
ax[1].plot(t_points,r0[0,:])

f_mod = lambda r,t: np.array([r[1],-pow(w,3)*pow(r[0],3)])
r2 = np.empty((2,N),float)
r2[:,0] = [1,0]
r2 = solve(r2,f_mod)
ax[2].plot(t_points,r2[0,:])

r22 = np.empty((2,N),float)
r22[:,0] = [2,0]
r22 = solve(r22,f_mod)
ax[3].plot(t_points,r22[0,:])

ax[0].set(title='harmonic & anharmonic oscillators',ylabel='harmonic\n x(0) = 1')
ax[1].set(ylabel='harmonic\n x(0) = 2')
ax[2].set(ylabel='anharmonic\n x(0) = 1')
ax[3].set(ylabel='anharmonic\n x(0) = 2',xlabel='time')

plt.show()

fig,ax = plt.subplots(1)
ax.plot(r2[0,:],r2[1,:])
ax.set(xlabel='x',ylabel='dx/dt',title='anharmonic oscillator phase space')
plt.show()

N = 5000
tf = 20.0
t_points = np.linspace(t0,tf,N)
w = 1
mu = 1
r_vdp0 = np.zeros((2,N),float)
r_vdp0[:,0] = [1,0]

r_vdp1 = np.empty((2,N),float)
r_vdp1[:,0] = [1,0]

r_vdp2 = np.empty((2,N),float)
r_vdp2[:,0] = [1,0]

vdp = lambda r,t: np.array([r[1],mu*(1-r[0]**2)*r[1] - r[0]*w**2],float)

r_vdp = solve(r_vdp0,vdp)

mu = 2
r_vdp1 = solve(r_vdp1,vdp)

mu = 4
r_vdp2 = solve(r_vdp2,vdp)

# 3 subplots plot
'''
fig,ax = plt.subplots(3,sharex=True)
ax[0].plot(r_vdp0[0,:],r_vdp0[1,:])
ax[1].plot(r_vdp1[0,:],r_vdp1[1,:])
ax[2].plot(r_vdp2[0,:],r_vdp2[1,:])
ax[0].set(ylabel='dx/dt')
ax[1].set(ylabel='dx/dt')
ax[2].set(ylabel='dx/dt',xlabel='x')
'''

# overlapping plot
fig,ax = plt.subplots()
ax.plot(r_vdp0[0,:],r_vdp0[1,:],c='green')
ax.plot(r_vdp1[0,:],r_vdp1[1,:],c='orange')
ax.plot(r_vdp2[0,:],r_vdp2[1,:],c='blue')
ax.set(xlabel='x',ylabel='dx/dt',title='van der Pol oscillator phase space')

plt.show()
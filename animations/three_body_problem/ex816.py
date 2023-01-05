'''
date: 08/03/22
exercise: 8.16

desc: animates and solves the three-body problem equations using the bulirsh-stoer method to get adaptive step sizes 
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

G = 1
m1,m2,m3 = 150.0,200.0,250.0
t0,tf = 0.0,20.0
N = 50000
H = 3e-4
delta = 1e-3
r = np.empty((6,2,N),float)
dw1 = lambda r: G*m2*(r[1,:]-r[0,:])/np.linalg.norm(r[1,:]-r[0,:])**3 + G*m3*(r[2,:]-r[0,:])/np.linalg.norm(r[2,:]-r[0,:])**3
dw2 = lambda r: G*m1*(r[0,:]-r[1,:])/np.linalg.norm(r[0,:]-r[1,:])**3 + G*m3*(r[2,:]-r[1,:])/np.linalg.norm(r[2,:]-r[1,:])**3
dw3 = lambda r: G*m1*(r[0,:]-r[2,:])/np.linalg.norm(r[0,:]-r[2,:])**3 + G*m2*(r[1,:]-r[2,:])/np.linalg.norm(r[1,:]-r[2,:])**3
f = lambda r: np.array( [r[3,:],r[4,:],r[5,:],dw1(r),dw2(r),dw3(r)] )
r[:,:,0] = [[3,1],[-1,-2],[-1,1],[0,0],[0,0],[0,0]]

def bs():
    for t in range(N-1):
        H = 2e-4
        n = 1
        r1 = r[:,:,t] + 0.5*H*f(r[:,:,t])
        r2 = r[:,:,t] + H*f(r1)
        R1 = np.empty((6,2,1),float)
        R1[:,:,0] = 0.5*(r1+r2+0.5*H*f(r2))
        error = 2*H*delta
        while error>H*delta:
            n = n + 1
            if n>20: 
                n = 2
                H = H/2
            h = H/n
            r1 = r[:,:,t] + 0.5*h*f(r[:,:,t])
            r2 = r[:,:,t] + h*f(r1)
            for i in range(n-1):
                r1 += h*f(r2)
                r2 += h*f(r1)

            R2 = R1[:,:,:]
            R1 = np.empty((6,2,n),float)
            R1[:,:,0] = 0.5*(r1+r2+0.5*h*f(r2))
            for m in range(1,n):
                ep = (R1[:,:,m-1]-R2[:,:,m-1])/((n/(n-1))**(2*m)-1)
                R1[:,:,m] = R1[:,:,m-1] + ep
            error = [np.linalg.norm(ep[i,:]) for i in range(3)]
            max = error[0]
            for i in range(len(error)):
                if error[i]>max: max = error[i]
            error = max
            #print(n)
        r[:,:,t+1] = R1[:,:,n-1]
    return r

r = bs()

fig,ax = plt.subplots(1)
#stars, = ax.plot(r[0:3,0,0],r[0:3,1,0],color='orange',marker='o',linestyle='') # easier but can't change star colors
star1, = ax.plot(r[0,0,0],r[0,1,0],color='cornflowerblue',marker='o',linestyle='',zorder=1) 
star2, = ax.plot(r[1,0,0],r[1,1,0],color='magenta',marker='o',linestyle='',zorder=1) 
star3, = ax.plot(r[2,0,0],r[2,1,0],color='pink',marker='o',linestyle='',zorder=1) 

path1, = ax.plot(r[0,0,0],r[0,1,0],color='cornflowerblue',zorder=0) 
path2, = ax.plot(r[1,0,0],r[1,1,0],color='magenta',zorder=0) 
path3, = ax.plot(r[2,0,0],r[2,1,0],color='pink',zorder=0) 

ax.set(xlim=[-5,5],ylim=[-5,5],xticks=[],yticks=[],title='the three body problem')
npoints = 100
def init():
    #stars.set_data([],[]) # for one star vector object
    star1.set_data([],[])
    star2.set_data([],[])
    star3.set_data([],[])

    path1.set_data([],[])
    path2.set_data([],[])
    path3.set_data([],[])

def animate(t):
    #stars.set_data(r[0:3,0,t],r[0:3,1,t]) # for one star vector object
    star1.set_data(r[0,0,t],r[0,1,t])
    star2.set_data(r[1,0,t],r[1,1,t])
    star3.set_data(r[2,0,t],r[2,1,t])

    if t>50:
        path1.set_data(r[0,0,t-50:t],r[0,1,t-50:t])
        path2.set_data(r[1,0,t-50:t],r[1,1,t-50:t])
        path3.set_data(r[2,0,t-50:t],r[2,1,t-50:t])
    
anim = FuncAnimation(fig,animate,frames=N,init_func=init,interval=1)
plt.show()
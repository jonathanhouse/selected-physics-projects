import numpy as np
import matplotlib.pyplot as plt

sig = 10
r_const = 28
b = 8.0/3.0

t0 = 0.0
tf = 50.0 
N = 5000
h = (tf-t0)/N

t_points = np.linspace(t0,tf,N)
r = np.empty((3,N),float)
r[:,0] = [0,1,0]

f0 = lambda x,y,z: sig*(y-x)
f1 = lambda x,y,z: r_const*x - y - x*z
f2 = lambda x,y,z: x*y - b*z
f = lambda r,t: np.array([f0(r[0],r[1],r[2]),f1(r[0],r[1],r[2]),f2(r[0],r[1],r[2])])

for t in range(N-1):
    k1 = h*f(r[:,t],t_points[t])
    k2 = h*f(r[:,t]+0.5*k1,t_points[t]+0.5*h)
    k3 = h*f(r[:,t]+0.5*k2,t_points[t]+0.5*h)
    k4 = h*f(r[:,t]+k3,t_points[t]+h)
    r[:,t+1] = r[:,t] + (1/6.0)*(k1+2*k2+2*k3+k4)

print(r[1,:])
fig,ax = plt.subplots(2)
ax[0].plot(t_points,r[1,:])
ax[0].axes.xaxis.set_ticks([])
ax[0].axes.yaxis.set_ticks([])

ax[1].plot(r[2,:],r[0,:])
ax[1].axes.xaxis.set_ticks([])
ax[1].axes.yaxis.set_ticks([])
plt.show()
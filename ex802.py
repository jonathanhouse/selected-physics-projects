import matplotlib.pyplot as plt
import numpy as np

a = 0.0
b = 30.0
alpha = 1
beta = 0.5
sigma = 2.0
gamma = 0.5
N = 500
h = (b-a)/N

f0 = lambda x,y: alpha*x - beta*x*y
f1 = lambda x,y: gamma*x*y - sigma*y
t_points = np.linspace(a,b,N)

r = np.empty((2,N),float)
r[:,0] = [2,2]

f = lambda r,t: np.array([f0(r[0],r[1]) , f1(r[0],r[1])])
for t in range(N-1):
    k1 = h*f(r[:,t],t_points[t])
    k2 = h*f(r[:,t]+0.5*k1,t_points[t]+0.5*h)
    k3 = h*f(r[:,t]+0.5*k2,t_points[t]+0.5*h)
    k4 = h*f(r[:,t]+k3,t_points[t]+h)
    r[:,t+1] = r[:,t] + (1.0/6)*(k1+2*k2+2*k3+k4)

fig,ax = plt.subplots(2)
ax[0].plot(t_points,r[0,:])
ax[1].plot(t_points,r[1,:])
plt.show()


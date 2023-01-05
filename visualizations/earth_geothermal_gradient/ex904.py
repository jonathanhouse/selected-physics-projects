'''
date: 08/06/22
exercise: 9.04

desc: solving thermal diffusion through earth's crust given a model surface temperature equation and visualizing the profile at 
three month intervals after ten years 
'''

import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi

D = 0.1
A,B = 10.0,12.0
tao = 365
surface_T = lambda t: A + B*sin(2*pi*t/tao)
N = 40
d0,df = 0.0,20.0
a = (df-d0)/N
d = np.linspace(d0,df,N)
T = np.zeros(N,float)
T[0] = surface_T(0)
T[N-1] = 11.0
T[1:N-1] = 10.0
 
h = 1.0
t0,tf = 0.0,365*11
Nt = int((tf-t0)/h)

fig,ax = plt.subplots(1)

for t in range(1,Nt-1):
    T[1:N-1] = T[1:N-1] + h*(D/a**2)*(T[2:N]+T[0:N-2]-2*T[1:N-1])   
    T[0] = surface_T(t)
    if t==3740 or t==3830 or t==3920 or t==4010: ax.plot(d,T,label=str(t) + ' days')

ax.set(xlabel="distance from Earth's surface (m)",ylabel='temperature (C)',title="Earth's crust temperature profile after 10 years every 3 months")
ax.legend()
plt.show()
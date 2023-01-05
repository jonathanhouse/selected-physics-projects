'''
date: 07/23/22
exercise: 8.01

desc: solve and visualize the differential equation for a low-pass filter circuit using fourth-order
runge-kutta method
'''

import numpy as np
import matplotlib.pyplot as plt
from math import floor

def v_in(t):
    if floor(2*t) % 2 == 0:
        return 1.0
    else: return -1.0

N = 500
a = 0.0
b = 10.0
h = (b-a)/N
t_points = np.linspace(a,b,N)

def v_out(tau):
    f = lambda v_out,t: (v_in(t) - v_out)/tau
    v_out = np.empty(N,float)
    v_out[0] = 0

    for t in range(len(t_points)-1):
        k1 = h*f(v_out[t],t_points[t])
        k2 = h*f(v_out[t]+0.5*k1,t_points[t]+0.5*h)
        k3 = h*f(v_out[t]+0.5*k2,t_points[t]+0.5*h)
        k4 = h*f(v_out[t]+k3,t_points[t]+h)
        v_out[t+1] = v_out[t] + (1.0/6)*(k1+2*k2+2*k3+k4)
    return v_out


fig,axes = plt.subplots(3)
axes[0].plot(t_points,v_out(0.01))
axes[1].plot(t_points,v_out(0.1))
axes[2].plot(t_points,v_out(1.0))

axes[0].set_title("voltage across capacitor")
axes[0].set_ylabel('RC = 0.01')
axes[1].set_ylabel('RC = 0.01')
axes[2].set_ylabel('RC = 0.01')

plt.show()
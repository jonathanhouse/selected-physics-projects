'''
date: 08/09/22
exercise: 10.02

desc: calculates and visualizes the number of atoms in the bismuth-213 radioactive decay chain 
(may take about 30s to load)
'''

from random import random
import numpy as np
import matplotlib.pyplot as plt

N0Bi = 10000
NPb = 0
NTl = 0
NfBi = 0

tauBi,tauPb,tauTl = 46*60,3.3*60,2.2*60
p = lambda t,tau: 1 - 2**(-t/tau)
t_max = 20000
t_points = np.linspace(0,t_max,t_max)
fig,ax = plt.subplots(1)

for nt in range(len(t_points)):
    t = t_points[nt]
    for i in range(NPb): 
        if random()<p(t,tauPb): NfBi += 1; NPb -= 1
    for i in range(NTl):
        if random()<p(t,tauTl): NPb += 1; NTl -= 1
    for i in range(N0Bi):
        if random()<p(t,tauBi): 
            N0Bi -= 1
            if random()<0.9791: NPb += 1
            else: NTl += 1
    ax.plot(t,N0Bi,color='black',marker='o',markersize=1)
    ax.plot(t,NPb,color='red',marker='o',markersize=1)
    ax.plot(t,NTl,color='blue',marker='o',markersize=1)
    ax.plot(t,NfBi,color='magenta',marker='o',markersize=1)

ax.plot([],[],color='k',label='213-Bi')
ax.plot([],[],color='r',label='209-Pb')
ax.plot([],[],color='b',label='209-Tl')
ax.plot([],[],color='m',label='209-Bi')

ax.set(xlim=[0,1000],xlabel='t',ylabel='number of atoms',title='radioactive decay of Bi-213')
ax.legend()
plt.show()
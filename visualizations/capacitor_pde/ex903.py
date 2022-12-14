'''
date: 09/25/22
exercise: 9.03

desc: solving and visualizing the electrostatic potential around two flat metal plates 
enclosed in a square metal box 
'''

import numpy as np
import matplotlib.pyplot as plt

N = 101
delta = 1e-6
r0,rf = 0.0,10e-2
w = 0.9
r = np.array( [np.linspace(r0,rf,N),np.linspace(r0,rf,N)] )
phi = np.zeros( (N+1,N+1),float )

acc = 1.0
while acc>delta:
    acc = 0.0
    for i in range(1,N):
        for j in range(1,N):
            x,y = r[0,i],r[1,j]
            if x == 0.02 and y >= 0.02 and y <= 0.08: 
                phi[i,j] = 1.0
                continue
            if x == 0.08 and y >= 0.02 and y <= 0.08: 
                phi[i,j] = -1.0
                continue
            curr_phi = phi[i,j]
            phi[i,j] = (1+w)*(phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])/4.0 - w*phi[i,j]
            if abs(curr_phi-phi[i,j]) > acc: acc = abs(curr_phi-phi[i,j])

fig,ax = plt.subplots(1)
im = ax.imshow(phi)
ax.set(xticks=[],yticks=[],title='capacitor electric charge')
fig.colorbar(im)
plt.show()

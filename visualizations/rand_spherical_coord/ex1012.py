'''
date: 08/11/22
exercise: 10.12

desc: transform random points to spherical coordinates, and visualize the generated points
'''

import numpy as np
import matplotlib.pyplot as plt
from math import acos,pi,sin,cos
from random import random
from mpl_toolkits import mplot3d

N = 2000
r = 1

polar_vars = np.empty((2,N),float)
cart_vars = np.empty((3,N),float)

for n in range(N):
    phi = 2*pi*random()
    theta = acos(1-2*random())  

    '''
    polar_vars[0,n] = phi
    polar_vars[1,n] = theta
    '''

    cart_vars[:,n] = r*sin(phi)*cos(theta),r*sin(phi)*sin(theta),r*cos(phi)

fig = plt.figure(figsize=(6,6))
ax = plt.axes(projection='3d')
ax.scatter3D(cart_vars[0,:],cart_vars[1,:],cart_vars[2,:])

plt.show()
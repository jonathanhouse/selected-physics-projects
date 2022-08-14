import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos,sqrt,pi
from matplotlib import cm

alt_x_dim = 512
alt_y_dim = 1024
altitude_data = open('altitude.txt').read().split()
altitude_data = np.array(altitude_data,float).reshape(alt_x_dim,alt_y_dim)

I = lambda phi,dwx,dwy: (cos(phi)*dwx + sin(phi)*dwy)/sqrt(dwx**2 + dwy**2 + 1)

def diff(data,x,y,h,x_dim,y_dim):
    deriv = np.empty(shape=(2))
    if(x == 0): deriv[0] = (data[x+1,y] - data[x,y])/h
    elif(y == 0): deriv[1] = (data[x,y+1] - data[x,y])/h
    elif(x == x_dim-1): deriv[0] = (data[x,y] - data[x-1,y])/h
    elif(y == y_dim-1): deriv[1] = (data[x,y] - data[x,y-1])/h
    else: 
        deriv[0] = (data[x+1,y] - data[x-1,y])/2*h
        deriv[1] = (data[x,y+1] - data[x,y-1])/2*h
    return deriv

def altitude_intensity():
    intensity = np.empty(shape=(alt_x_dim,alt_y_dim))
    for i in range(alt_y_dim):
        for j in range(alt_x_dim):
            deriv = diff(altitude_data,j,i,30000,alt_x_dim,alt_y_dim)
            intensity[j,i] = I(pi/4,deriv[0],deriv[1])
    return intensity

def display_altitude():
    data = altitude_intensity()
    cmap = cm.get_cmap('gist_earth')
    #data = np.ma.masked_where(data == 0, data)
    #cmap.set_bad(color='blue')
    im = plt.imshow(data,cmap=cmap)
    plt.show()

stm_x_dim = 442
stm_y_dim = 1014
stm_data = np.array(open('stm.txt').read().split(),float).reshape(stm_x_dim,stm_y_dim)
def stm_intensity():
    intensity = np.empty(shape=(stm_x_dim,stm_y_dim))
    for i in range(stm_y_dim):
        for j in range(stm_x_dim):
            deriv = diff(stm_data,j,i,2.5,stm_x_dim,stm_y_dim)
            intensity[j,i] = I(pi/4,deriv[0],deriv[1])
    return intensity

def display_stm():
    im = plt.imshow(stm_intensity())
    plt.show()

display_altitude()
display_stm()
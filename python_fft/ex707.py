import numpy as np
import  matplotlib.pylab as plt
from math import pi,log2
from cmath import exp
from numpy.fft import rfft

# build a fft 

pitch = open("pitch.txt","r")
pitch = [float(x) for x in pitch]


def fft(y): # least memory effcient fft - log2N+1 * N array
    N = len(y)
    i = complex(0,1)
    levels = int(log2(N))
    E = np.empty((levels+1,N),complex)
    E[levels,:] = y[:]
    for m in range(levels-1,-1,-1):
        for j in range(pow(2,m)):
            for k in range(int(N/pow(2,m))):
                s = k
                if k > int(N/pow(2,m+1))-1: s -= int(N/pow(2,m+1))
                E[m,j+pow(2,m)*k] = E[m+1,j+pow(2,m+1)*s] + exp(-i*2*pi*pow(2,m)*k/N)*E[m+1,j+pow(2,m+1)*s+pow(2,m)]
    return E[0,:]

def fft2(y): # more memory effcient fft - two N arrays
    N = len(y)
    i = complex(0,1)
    levels = int(log2(N))
    E_current = np.empty(N,complex)
    E_prev = np.empty(N,complex)
    E_prev[:] = y[:]
    print(E_prev)
    for m in range(levels-1,-1,-1):
        for j in range(pow(2,m)):
            for k in range(int(N/pow(2,m))):
                s = k
                if k > int(N/pow(2,m+1))-1: s -= int(N/pow(2,m+1))
                E_current[j+pow(2,m)*k] = E_prev[j+pow(2,m+1)*s] + exp(-i*2*pi*pow(2,m)*k/N)*E_prev[j+pow(2,m+1)*s+pow(2,m)]
        E_prev[:] = E_current[:] 
    return E_current

np_c = abs(rfft(pitch)) # numpy fft coefficents
my_c = abs(fft2(pitch))  # my fft coefficents
fig,axes = plt.subplots(2)
axes[0].plot(np.arange(len(np_c)),np_c)
axes[1].plot(np.arange(len(my_c)/2),my_c[0:int(len(my_c)/2)])
plt.show()
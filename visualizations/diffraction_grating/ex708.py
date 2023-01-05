'''
date: 07/04/22
exercise: 7.08

desc: visualize diffraction grating intensity by approximating the associated integral 
using fourier transforms, and compare results to ex. 5.19
'''

from cmath import exp 
from math import sin,pi,sqrt
import numpy as np
from numpy.fft import rfft
import matplotlib.pyplot as plt

a = pi/20e-6
q = lambda u: pow(sin(a*u),2)
w = 200e-6
W = 10*w
wv = 500e-9
f = 1
N = 1000
d = .1

u = lambda n: w*(n/N-1/2)
y = [sqrt(q(u(n))) for n in range(N)] + [0 for i in range(9*N)] # 10*N to compensate for using W
c = rfft(y)

x = [wv*f/W*k for k in range(N)]
I = [pow(W,2)/pow(N,2)*abs(c[k])**2 for k in range(N)]

x_final = list(-1*np.array(x[::-1])) + x[:]
I_final = I[::-1] + I
#print(x_final)
plt.plot(x_final,I_final)
plt.xlim(-.05,.05)
plt.show()

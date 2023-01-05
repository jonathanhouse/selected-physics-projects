'''
date: 05/16/22
exercise: 5/13

desc: calculates and visualizes the hermite polynomials associated with the wavefunction for a quantum
harmonic oscillator of order 0,1,2,3 & 30, and calculates the positional uncertainity for a particle using gaussian 
quadrature 
'''

from numpy import polynomial
import numpy as np
import matplotlib.pyplot as plt
from math import pi,exp,factorial,sqrt,sin,fabs,tan,cos
from scipy import integrate

N = 1000

def H(n,x):
    h = np.empty(shape=(n+1))
    if n == 0: return 1
    if n == 1: return 2*x
    h[0] = 1
    h[1] = 2*x
    for i in range(1,n):
        h[i+1] = 2*x*h[i] - 2*i*h[i-1]
    return h[n]
    
def phi(n,x):
    return  1/sqrt( pow(2,n)*factorial(n)*sqrt(pi) )*exp( pow(x,2)/-2 )*H(n,x)

def uncertainity(n):
    N = 100
    b = pi/2
    a = -pi/2
    f = lambda z: pow(phi(n,tan(z)),2)*(pow(tan(z),2)/pow(cos(z),2))
    z,w = polynomial.legendre.leggauss(N)
    zp = 0.5*(b-a)*z + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    s = 0.0
    for i in range(N):
        s += wp[i]*f(zp[i])
    return sqrt(s)

colors = {0:'k-',1:'r-',2:'b-',3:'g-'}

print('\nquantum uncertainity for particle at 5th level of quantum harmonic oscillator:\n<x^2> ~ ' + str(uncertainity(5)))

n = np.arange(0,4)
x = np.linspace(-4,4,N)
p = np.empty(shape=(len(x)))
for i in range(len(n)):
    for k in range(len(x)):
        p[k] = phi(n[i],x[k])
    plt.plot(x,p,colors[n[i]],label='n =' + str(n[i]))
    p = np.empty(shape=(len(x)))

plt.title('n-th order Hermite polynomial \nwavefunction of quantum harmonic oscillator')
plt.legend()
plt.show()

x = np.linspace(-10,10,N)
p = np.empty(shape=(len(x)))
for i in range(len(x)):
    p[i] = phi(30,x[i])

plt.title('order-30 Hermite polynomial wavefunction')
plt.plot(x,p)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from math import sqrt,log10

N = 1000
iterations = 1000
def mandelbrot(c,iterations):
    z = 0
    for i in range(1,iterations+1):
        z = pow(z,2) + c
        if( sqrt( pow(z.real,2) + pow(z.imag,2) ) > 2): return log10(i)
    return log10(iterations)


values = np.empty((N,N),int)
x = np.linspace(-2,2,N)
y = np.linspace(-2,2,N)

for i in range(N): 
    for j in range(N): 
        values[j,i] = mandelbrot(complex(x[i],y[j]),iterations)

plt.figure(figsize=(16,6),facecolor="gray")
plt.jet()
plt.imshow(values)
plt.xlim(0,700)
plt.ylim(150,850)
plt.show()

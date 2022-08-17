import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("millikan.txt",float)

x = data[:,0]
y = data[:,1]
N = len(data[:,0])
ex = np.dot(x,np.full(N,1))*(1/N)
ey = np.dot(y,np.full(N,1))*(1/N)
exx = np.dot(x,x)*(1/N)
exy = np.dot(x,y)*(1/N)

m = (exy-ex*ey)/(exx-pow(ex,2))
c = (exx*ey-ex*exy)/(exx-pow(ex,2))

least_squares = m*x + c

print("planck constant: " + str(m*1.602*pow(10,-19)))

plt.figure(figsize=(16,6),facecolor='gray')
plt.plot(x,y,'ko')
plt.plot(x,least_squares)
plt.show()

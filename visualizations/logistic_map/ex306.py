
import matplotlib.pyplot as plt
import numpy as np

N = 1000
x0 = 0.5
x_final = []
r_final = []

def logistic(r):
    x = [x0]
    for i in range(1, N-1):
        x.append(r * x[i-1] * (1- x[i-1]))
    return x[N-150:]

def logistic_plot(x0,r,n):
    x = [x0]
    for i in range(1,n+1):
        x.append(r*x[i-1]*(1-x[i-1]))
    iterations = np.arange(0,len(x),1)
    plt.figure(figsize=(16,6),facecolor='gray')
    plt.style.use('seaborn-darkgrid')
    plt.title("x=" + str(x0) + " & r=" + str(r))
    plt.xlabel("iterations")
    plt.ylabel("x value")
    plt.plot(iterations,x,'k-')
    plt.show()


r = np.linspace(2.0,4.0,1000,dtype=float)

for r0 in r:
    xs = np.array(logistic(r0))
    x_final.append(xs)
    r_final.append(np.full(len(xs),r0))

x_final = np.array(x_final).ravel()
r_final = np.array(r_final).ravel()

#logistic_plot(0.501,3.64,N)

plt.figure(figsize=(10,5),facecolor='gray')
#plt.style.use('seaborn')
plt.scatter(r_final,x_final,s=0.1)
plt.show()

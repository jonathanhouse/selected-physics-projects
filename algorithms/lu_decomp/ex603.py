'''
date: 05/22/22
exercise: 6.03

desc: performs an LU decomposition to solve the matrix equation of the form ax = v, and compares the results to those
from numpy's linalg solver 
'''

import numpy as np

def lu(a,v):

    U = a.copy()
    vp = v.copy()
    N = len(a[0])
    L = np.zeros(shape=(N,N))
    y = np.empty(shape=(N))
    x = np.empty(shape=(N))

    # gaussian elimination
    for m in range(N):

        for k in range(m,N):
            L[k,m] = U[k,m]

        vp[m] /= U[m,m]
        U[m,:] /= U[m,m]

        for i in range(m+1,N):
            vp[i] -= U[i,m]*vp[m]
            U[i,:] -= U[i,m]*U[m,:]

    #print(L @ U) # identical to np.matmul(L,U)

    vp = v.copy()
    for i in range(N):
        y[i] = vp[i]
        for j in range(0,i):
            y[i] -= y[j]*L[i,j]
        y[i] /= L[i,i]
   
    for m in range(N-1,-1,-1):
        x[m] = y[m]
        for n in range(m+1,N):
            x[m] -= x[n]*U[m,n]       
        x[m] /= U[m,m]
    
    return x

    

a = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],float)
v = np.array([5,0,5,0],float)
#print(np.matmul(lu(a,v)[1],lu(a,v)[0])) # A = L*U 
#print(elim(a,v)[1] @ elim(a,v)[0]) # @ is equivalent to matmul 
print("my lu decomp:\t\t" + str(lu(a,v)))
print("numpy's linalg solver:\t" + str(np.linalg.solve(a,v)))






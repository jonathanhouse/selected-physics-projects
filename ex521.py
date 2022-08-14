from math import pi,sqrt,atan,sin,cos
from numpy import polynomial
import numpy as np
import matplotlib.pyplot as plt

# parts a & b - two point charges
e0 = 8.85e-12
def pot(pos,q,x,y):
    test = [x,y]
    return q/(4*pi*e0*sqrt(pow(test[0]-pos[0],2) + pow(test[1]-pos[1],2)))

def pot_sum(pos_list,q_list,x,y):
    return pot(pos_list[0],q_list[0],x,y) + pot(pos_list[1],q_list[1],x,y)
    
def field(pos_list,q_list,test):
    h = 1e-5
    vals = np.empty(shape=(2))
    vals[0] = -(pot_sum(pos_list,q_list,test[0]+h,test[1]) - pot_sum(pos_list,q_list,test[0],test[1]))/h
    vals[1] = -(pot_sum(pos_list,q_list,test[0],test[1]+h) - pot_sum(pos_list,q_list,test[0],test[1]))/h
    return vals

def field_arrows(pos_list,q_list,sample_x,sample_y):
    arrow_len = 1e-2
    for j in range(len(sample_y)):
        for i in range(len(sample_x)):
            test = [sample_x[j],sample_y[i]]
            theta = atan( field(pos_list,q_list,test)[1] / field(pos_list,q_list,test)[0] )
            plt.arrow(test[0],test[1],arrow_len*cos(theta),arrow_len*sin(theta))

def graph_pot():
    N = 500
    x_points = np.linspace(-0.5,0.5,N)
    y_points = np.linspace(-0.5,0.5,N)
    q_list = [-1.0,1.0]
    pos_list = [(-5e-2,0.0),(5e-2,0.0)]
    tst = [0.0,0]

    pot_grid = np.empty(shape=(N,N))
    e_field = np.empty(shape=(N,N))
    for i in range(N):
        for j in range(N):
            test = [x_points[j],y_points[i]]
            pot_grid[i,j] = pot_sum(pos_list,q_list,test[0],test[1])
            #e_field[i,j] = sqrt( field(pos_list,q_list,test)[0]**2 + field(pos_list,q_list,test)[1]**2 ) # magnitude
            e_field[i,j] = atan( field(pos_list,q_list,test)[1] / field(pos_list,q_list,test)[0] ) # direction
            
    #plt.imshow(pot_grid,extent=(-1,1,-1,1))
    plt.imshow(e_field,extent=[-0.5,0.5,-0.5,0.5])
    field_arrows(pos_list,q_list,np.linspace(-0.45,0.45,25),np.linspace(-0.45,0.45,25))
    plt.hsv()
    plt.show()


# part c - continous charge distribution
L = 10e-2
q0 = 100
sig = lambda x,y,xr,yr: q0*sin(2*pi*x/L)*sin(2*pi*y/L)/(4*pi*e0*sqrt( pow(xr-x,2) + pow(yr-y,2) ))
def fx(x,xr,yr):
    N = 20
    b,a = L/2, -L/2
    y,w = polynomial.legendre.leggauss(N)
    yp = 0.5*(b-a)*y + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    s = 0.0
    for i in range(N):
        s += sig(x,yp[i],xr,yr)*wp[i]
    return s
def continous_pot(xr,yr):
    N = 20
    b,a = L/2,-L/2
    x,w = polynomial.legendre.leggauss(N)
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    s = 0.0
    for i in range(N):
        s += fx(xp[i],xr,yr)*wp[i]
    return s
def continuous_field(xr,yr):
    h = 1e-5
    vals = np.empty(shape=(2))
    vals[0] = -(continous_pot(xr+h,yr) - continous_pot(xr,yr))/h
    vals[1] = -(continous_pot(xr,yr+h) - continous_pot(xr,yr))/h
    return vals

def graph_continuous_field():
    N = 50
    x_points = np.linspace(-0.5,0.5,N)
    y_points = np.linspace(-0.5,0.5,N)
    e_field = np.empty(shape=(N,N))

    for y in range(N):
        for x in range(N):
            e_field[x,y] = atan( continuous_field(x_points[x],y_points[y])[1] / continuous_field(x_points[x],y_points[y])[0] )
    plt.imshow(e_field,extent=[-0.5,0.5,-0.5,0.5])
    plt.hsv()
    plt.show()

def continuous_field_arrows(sample_x,sample_y):
    arrow_len = 1e-2
    for y in range(len(sample_y)):
        for x in range(len(sample_x)):
            test = [sample_x[x],sample_y[y]]
            theta = atan( continuous_field(test[0],test[1])[1] / continuous_field(test[0],test[1])[0] )
            plt.arrow(test[0],test[1],arrow_len*cos(theta),arrow_len*sin(theta))

def continous_plot():
    continuous_field_arrows(np.linspace(-.45,.45,10),np.linspace(-.45,.45,10))
    graph_continuous_field()

graph_pot()
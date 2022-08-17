from random import random,seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import pi,sin,cos,sqrt
plt.style.use('dark_background')
import matplotlib as mpl
seed(3112)
# textbook exercise dla
'''
N = 201
Nt = N*N

fig,ax = plt.subplots(1)
ax.set(xlim=[-2,N+1],ylim=[-2,N+1],title='diffusion-limited aggregation',xticks=[],yticks=[])
head, = ax.plot([],[],color='magenta',marker='s',linestyle='',alpha=1,zorder=1)

heads = np.zeros((Nt,2),int)

def dla(t):
    r = np.empty(2,int)
    r[:] = [N//2,N//2]
    unstuck = True
    while(unstuck):
        z = random()
        collision = False
        i,j = r[0],r[1]
        if z<0.25: r[0]+=1
        elif z>=0.25 and z<0.5: r[0]-=1
        elif z>=0.5 and z<0.75: r[1]+=1
        elif z>=0.75: r[1]-=1

        ia,ja = r[0],r[1]
        collision = [ 1 for k in range(t) if (ia == heads[k,0] and ja == heads[k,1])]
        if ia<0 or ia>N-1 or ja<0 or ja>N-1 or collision: 
            heads[t,0] = i
            heads[t,1] = j
            unstuck = False

def animate(t):
    dla(t)
    head.set_data(heads[0:t,0],heads[0:t,1])
    print(t)

anim = FuncAnimation(fig,animate,interval=1,frames=Nt)
plt.show()
'''

# original dla program
N = 201 # size of grid - N = 501 is about 10 minutes 
Nt = N*N # number of head points - overestimates heads for the entire N*N grid 

heads = np.tile([N//2,N//2],(2,Nt)) # sets all heads initially as center of grid 
r = 0 # running maximum head distance from grid center 

# mpl initialization
fig,ax = plt.subplots(1,figsize=(7,6))
ax.set(xlim=[-1,N+1],ylim=[-1,N+1],xticks=[],yticks=[],title='diffusion-limited aggregation')
heads_plot, = ax.plot([],[],'ws',markersize=0.5)

# grid initialization - for age-color plot, grid values are the age of heads 
grid = np.zeros((N,N),int)
grid[N//2,N//2] = 1

# function for checking grid neighbor occupany of heads [i,j]
def neighbor(i,j):
    if i+1>N-1 or j+1>N-1 or i-1<0 or j-1<0: return True
    if grid[i+1,j] >= 1: return True
    elif grid[i-1,j] >= 1: return True
    elif grid[i,j+1] >= 1: return True
    elif grid[i,j-1] >= 1: return True
    return False

age_max = 0
for t in range(Nt): # overestimates running for each potential head 
    curr = np.empty(2,int) # declare current test head
    z = random()*2*pi # random angle 0-2*pi
    curr[:] = [N//2+(r+1)*cos(z),N//2+(r+1)*sin(z)] # init current test head on a circle w/ radius r around grid center 
    age = 0 # init age
    while(True):
        z = random() # random variable for move 
        collision = False # init collision bool
        i,j = curr[0],curr[1] # save location of test head before move
        # move point in random direction
        if z<0.25: curr[0]+=1
        elif z>=0.25 and z<0.5: curr[0]-=1
        elif z>=0.5 and z<0.75: curr[1]+=1
        elif z>=0.75: curr[1]-=1
        
        ia,ja = curr[0],curr[1] # save new location of test head
        if ia>N-1 or ja>N-1 or ia<0 or ja<0: # if test head goes off grid, start new test point
            z = random()*2*pi
            curr[:] = [N//2+(r+1)*cos(z),N//2+(r+1)*sin(z)]
            break
        if neighbor(i,j): # if test point before move has a neighbor
                if grid[ia,ja] >= 1: # and if that neighbor is a previous head
                    collision = True # a collision has occured
        if collision: 
            heads[:,t] = [i,j] # add head point before collision to heads list
            head_distance = sqrt(np.dot(np.array([i,j])-np.array([N//2,N//2]),np.array([i,j])-np.array([N//2,N//2]))) # find head distance from center
            if head_distance>r: r = head_distance 
            if age>age_max: age_max = age
            print(str(round(r/(N//2)*100,2)) + '% ' + "complete") # print completion percent
            grid[i,j] = age
            break
        if 2*r<np.linalg.norm(np.array([ia,ja])-np.array([N//2,N//2])): # if head test point distance from center exceeds twice the max recorded distance, start new test point
            z = random()*2*pi
            curr[:] = [N//2+(r+1)*cos(z),N//2+(r+1)*sin(z)]
        age += 1 # iterate age 
    if r>N//2: t_max = t; break # if max head distance from center overcomes half the grid length - stop loop and record num of heads

cool = mpl.cm.get_cmap('cool',8)
def animate(t):
    # singularly plots heads w/ colors depending on age - significantly slower
    #ax.plot(heads[0,t],heads[1,t],color=cool(grid[heads[0,t],heads[1,t]]/age_max),marker='s',markersize=0.1)

    # reveals heads over time w/ singular color 
    heads_plot.set_data(heads[0,0:t],heads[1,0:t])

anim = FuncAnimation(fig,animate,interval=1,frames=len(heads[0,0:t_max])) # frames only extend to num of heads - not overestimate Nt
plt.show()

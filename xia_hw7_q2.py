# author: Shufan Xia
# date: Mar.31st,2020

import numpy as np
import matplotlib.pyplot as plt


plt.rc('font',family ='serif')
plt.rc('text',usetex =True)

# define some constants
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

x0 = 2
y0 = 2

# define the systems of DEQs of two variables
def f(r,t):
    x = r[0]
    y = r[1]
    
    dx = alpha*x-beta*x*y
    dy = gamma*x*y-delta*y

    return np.array([dx,dy],float)
    
def RK_Solve(f,t0,tf,x0,y0,N):
    
    h = (tf-t0)/N
    tpoints = np.arange(t0,tf,h)
    xpoints = []
    ypoints = []

    r = np.array([x0,y0],float)
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += 1/6*(k1+2*k2+2*k3+k4)
        
    # rabbits population
    plt.plot(tpoints,xpoints,label="rabbit population")
    # foxes population
    plt.plot(tpoints,ypoints,label="foxe population")
    plt.xlabel("time")
    plt.ylabel("population")
    plt.title("Population of rabbits and foxes over a time per")
    plt.legend()
    plt.savefig("predatorPrey.pdf")
    plt.show()
    


RK_Solve(f,0,30,2,2,1000) # call the function to solve and plot from t=0 to 30
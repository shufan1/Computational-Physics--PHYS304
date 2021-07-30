# author: Shufan Xia
# date: Mar.31st,2020

from vpython import *
from math import cos,sin,pi
import numpy as np


# import numpy and matplot library
import matplotlib.pyplot as plt

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# define some constant
l = 0.1 #m
g = 9.81 #kg.m/s^2

# convert the second order DEQ to a systems of DEQs of two variables
def f(r,t):
    
    theta = r[0] 
    omega = r[1]
    dfth = omega
    dfo = -(g/l)*np.sin(theta)
    
    return np.array([dfth,dfo],float)



def RK_Solve(f,a,b,x0,y0,N):
    
    h = (b-a)/N
    tpoints = np.arange(a,b,h)
    opoints = []
    thpoints = []
    dth = []
    domega = []

    r = np.array([x0,y0],float)

    for t in tpoints:
        thpoints.append(r[0])
        opoints.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        delta = (k1+2*k2+2*k3+k4)/6
        r += delta
        dth = delta[0]
        do = delta[1]
    
#     plt.plot(thpoints,opoints)
#     plt.show()

    return thpoints,opoints,dth,do

# define parameters 
a = 0.0
b = 100
N = 10000  # small number of steps has big computational error 
h = (b-a)/N 
theta0 = np.radians(179)

# Solve the DEQs
theta, omega, dtheta, domega = RK_Solve(f,a,b,theta0,0,N)

tpoints = np.arange(a,b,h)

# plot the solution theta(t)
plt.plot(tpoints, theta)
plt.ylabel("$\Theta$(t)")
plt.xlabel("t(s)")
plt.title("Solution to Underiven Penudlum using 10000 step size")
plt.savefig("undriven_1.pdf")
plt.show()

N2 = 1000 # small number of steps has big computational error 
h2 = (b-a)/N2
tpoints1 = np.arange(a,b,h2)
# Solve the DEQs using 1000 steps
theta1, omega1, dtheta1, domega1 = RK_Solve(f,a,b,theta0,0,N2)

# plot the solution theta(t)
plt.plot(tpoints1, theta1)
plt.ylabel("$\Theta$(t)")
plt.xlabel("t(s)")
plt.title("Solution to Underiven Penudlum using 1000 step size")
plt.savefig("undriven_2.pdf")
plt.show()


### Driven pendulum

## define some constants
l = 0.1 # m
C = 2 #s^-2
D = 5 #s^-1

def fdriven(r,t):
    
    theta = r[0]
    omega = r[1]
    dfth = omega
    dfo = -g/l*np.sin(theta)+C*np.cos(theta)*np.sin(D*t)
    
    return np.array([dfth,dfo],float)

# define parameters 
a = 0.0
b = 100
theta0 = 0 
v0 = 0
N = 10000

tpoints = np.arange(a,b,h)

# Solve the DEQs
theta2, omega2, dtheta2, domega2 = RK_Solve(fdriven,a,b,theta0,v0,N)
# plot the solution theta(t)
plt.plot(tpoints, theta2)
plt.ylabel("$\Theta$(t)")
plt.xlabel("t(s)")
plt.title(r'$\frac{d^2 t}{dt^2} = -\frac{g}{l}sin \theta+C cos \theta sin\Omega t, \Omega = 5$')
plt.savefig("driven_1.pdf")
plt.show()

## driven with the resonant frequency
# omeage resronate = sqrt(g/l) =9.900
D = np.sqrt(g/l)

# Solve the DEQs
theta3, omega3, dtheta3, domega3 = RK_Solve(fdriven,a,b,theta0,v0,N)

# plot the solution theta(t)
plt.plot(tpoints, theta3)
plt.ylabel("$\Theta$(t)")
plt.xlabel("t(s)")
plt.title(r'$\frac{d^2 t}{dt^2} = -\frac{g}{l}sin \theta+C cos \theta sin\Omega t, \Omega = \sqrt{g/l}$')
plt.savefig("driven_2.pdf")
plt.show()

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

# undriven case
# define some constant
l = 0.1 #m
g = 9.8 #kg.m/s^2

def f(r,t):
    
    theta = r[0]
    omega = r[1]
    dfth = omega
    dfo = -(g/l)*np.sin(theta)
    
    return np.array([dfth,dfo],float)

# resonant driven case

## define some constants
l = 0.1 # m
C = 2 #s^-2
D = np.sqrt(g/l)

def fdriven(r,t):
    
    theta = r[0]
    omega = r[1]
    dfth = omega
    dfo = -g/l*np.sin(theta)+C*np.cos(theta)*np.sin(D*t)
    
    return np.array([dfth,dfo],float)


# 4th order Runge-Kutta to solve the DEQs
def RK4_Solve(f,a,b,x0,y0,N):
    
    h = (b-a)/N
    tpoints = np.arange(a,b,h)
    opoints = []
    thpoints = []
    dth = [0]
    domega = [0]

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
        dth.append(delta[0])
        domega.append(delta[1])
    
    return thpoints,opoints,dth,domega

mode = input("selecte undriven or driven:")

if mode == "undriven":

	# #define parameters for undriven pendulum
	a = 0.0
#			 b = 18*np.pi/np.sqrt(9.8)#100s
	b = 100#100s
	N = 10000
	theta0 = np.radians(179)
	theta, omega, dtheta, domega = RK4_Solve(f,a,b,theta0,0,N)

else:
	# # define parameters for driven pendulum 
	a = 0.0
	b = 100 #100s
	N = 10000
	theta0 = 0
	theta, omega, dtheta, domega = RK4_Solve(fdriven,a,b,theta0,0,N)

# make Animation
d = canvas(background = color.white)

# initial position for the sphere
x0 = l*cos(theta0-np.pi/2)
y0 = l*sin(theta0-np.pi/2)

# make a sphere
s = sphere(pos=vector(x0,y0,0),radius=0.01,make_trail=True, trail_type="points",interval=10)
# make a vector
v = curve(vector(0,0,0), vector(x0,y0,0))


for i in range(len(theta)):
	rate(60)
	th = theta[i]
	dth = dtheta[i]

	x = l*cos(th-np.pi/2)
	y = l*sin(th-np.pi/2)

	# update the position of the vector
	v.rotate(dth,axis=vector(0,0,1),origin=vector(0,0,0))
	# update the position of the shphere
	s.pos=vector(x,y,0)










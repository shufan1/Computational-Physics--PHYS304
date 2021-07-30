import numpy as np
from math import factorial 
import matplotlib.pyplot as plt
from gaussxw import gaussxw
import matplotlib.gridspec as gridspe

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

k = 8.99E9 #Coloumb constant

def V(x,y): # expression of V due to two point charge at a given x,y in cm position
	return (k/np.sqrt(x**2 + y**2)-k/np.sqrt((x-10)**2 + y**2))*100 #use point chage potential equation

# a grid of 1cm squares from x,y =-50cm to 50 cm
x,y = np.meshgrid(np.arange(-50, 50, 1),
                  np.arange(-50,50, 1))
## evaluate V at each point on the grid
V_data=V(x,y)
V_data[50][60] = -8E11

# !!!!!!V_data[50][60] corresponds to (10,0) cm the coordiante of the negative charge, 
#division by zero occurs, replace with a large negative number

#plot the potential as 2D density plot
plt.imshow(V_data,cmap='hot',extent=[-50,50,-50,50])
plt.title("Electric potential due to two point charges (V)")
plt.ylabel("$y(cm)$")
plt.xlabel("$x(cm)$")
plt.colorbar()
plt.savefig("potential.pdf")
plt.show()

#  E=-dV, central differnece method to find the partial derivative of x and y 
# # partial derivative using central difference method:
#return the x and y component of the E field at a given point
def Efield(f,x,y,h):

	def dEx(f,x,y,h):
		s = f(x+h,y)-f(x-h,y)
		return -s/(2*h)

	def dEy(f,x,y,h):
		s = f(x,y+h)-f(x,y-h)
		return -s/(2*h)

	return dEx(f,x,y,h),dEy(f,x,y,h)
# a grid of 1cm squares from x,y =-50cm to 50 cm
x,y = np.meshgrid(np.arange(-50, 50, 1),
                  np.arange(-50, 50, 1))
# evaluate Ex and Ey
u, v = Efield(V, x,y,0.001) #h=0.1cm
length = np.sqrt(u**2 + v**2)


#plot the magnitude of the E field as a density plot
plt.imshow(length, vmax=10.E9, cmap='hot',extent=[-50,50,-50,50])
clb = plt.colorbar()
clb.set_label('Magnitude of Electric field ')
plt.title("Electric field due to two point charges (N/C)")
plt.ylabel("$y(cm)$")
plt.xlabel("$x(cm)$")
# streamplot to plot direction of E fields
plt.streamplot(x,y,u,v)
plt.savefig("Efield.pdf")
plt.show()


## part c, continuous charge distribution

#define double intgral method by using the Gauss–Legendre product formula
def double_int(f,x1,x2,y1,y2,N):

	x,wx = gaussxw(N)
	# x and y have the same sample points and weights

	# rescale weight and x/y values
	xp = 0.5*(x2-x1)*x + 0.5*(x2+x1)
	wxp = 0.5*(x2-x1)*wx

	s =0	
	for j in range(N):
		for i in range(N):
			s += wxp[j]*wxp[i]*f(xp[i],xp[j])   
	return s

L = 0.1  #L=10cm
q0= 100 #in unit of C m^-2

# surface charge per unit as a function of x and y
def surfaceCharge(x,y):
	sigma=q0*np.sin(2*np.pi*x/L)*np.sin(2*np.pi*y/L)
	return sigma


# define V at (a,b)
def V(a,b):
	def dV(x,y):
		sigma=surfaceCharge(x,y) # find urface charge per unit at (x,y)
		dV = k*sigma/(np.sqrt((x-a)**2+(y-b)**2)) #dV due a point charge sigma dx dy
		return dV
	Vab = double_int(dV,-L/2,L/2,-L/2,L/2,100) #double integral using Gaussian 
	return Vab

# a grid of 1cm squares from x,y =-50cm to 50 cm
a,b = np.meshgrid(np.arange(-0.5,0.5,0.01),
                  np.arange(-0.5,0.5,0.01))

V_data=V(a,b) 

plt.imshow(V_data,cmap='hot',extent=[-50,50,-50,50])
plt.title("Electric potential (V)")
plt.ylabel("$y(cm)$")
plt.xlabel("$x(cm)$")
clb = plt.colorbar()
clb.set_label('Electric potential (V)')
plt.savefig("potentialc.pdf")
plt.show()



# a grid of 1cm squares from x,y =-50cm to 50 cm
# a,b = np.meshgrid(np.arange(-0.5,0.5,0.01),
#                   np.arange(-0.5,0.5,0.01))

# evaluate Ex and Ey using Efield() from part b)
u, v = Efield(V,a,b,0.001) #h=0.001m
length = np.sqrt(u**2 + v**2) #magnitude of Efield



# #plot the magnitude of the E field as a density plot
plt.imshow(length, vmax=6.E12, cmap='hot',extent=[-50,50,-50,50])
clb = plt.colorbar()
clb.set_label('Magnitude of Electric field (N/C)')
plt.title("Electric field (N/C)")
plt.ylabel("$y(cm)$")
plt.xlabel("$x(cm)$")

# streamplot to plot direction of E fields
plt.streamplot(x,y,u,v)
plt.savefig("Efieldc.pdf")
plt.show()

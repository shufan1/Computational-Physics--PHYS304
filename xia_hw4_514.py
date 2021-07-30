import numpy as np
from math import factorial 
import matplotlib.pyplot as plt
import integration as itg
from gaussxw import gaussxw

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# supress division by zero warning
np.seterr(divide='ignore', invalid='ignore')

#define double intgral method by using the Gauss–Legendre product formula
def double_int(f,x1,x2,y1,y2,N):

	x,wx = gaussxw(N)
	# x and y have the same sample points and weights
	# rescale weight and x values
	xp = 0.5*(x2-x1)*x + 0.5*(x2+x1)
	wxp = 0.5*(x2-x1)*wx

	s =0	
	for j in range(N):
		for i in range(N):
			s += wxp[j]*wxp[i]*f(xp[i],xp[j])   
	return s

#define integrand as a function of z
def f(z):
	def integrand(x,y):
		return 1/np.power((x**2+y**2+z**2),1.5)
	return integrand	


def Fz(z, L):
	#define boundaries and constant
	x1=-L/2
	x2=L/2
	y1=-L/2
	y2=L/2
	G = 6.674E-11
	sigma=10*1000/(L*L)
	
	#evaluate double integral
	Fz = sigma*G*z*double_int(f(z),x1,x2,y1,y2,100)
	return Fz


L = 10

#plot function Fz
z_list = np.linspace(0.0,10,101)#0 to 10m, 100 sample points
Fz = list(map(lambda z: Fz(z,10), z_list)) #evaluate Fz at each z
plt.plot(z_list,Fz)
plt.title("Gravitational force $F_z(z)$")
plt.xlabel("z")
plt.ylabel("$F_z(z)$")
plt.savefig("gravitational.pdf")
plt.show()

#smoothen the dip by plotting more smaple points for 0<=x<=1.5
z_list = np.linspace(0.0,1.5,1001)
Fz = list(map(lambda z: Fz(z,10), z_list))
plt.plot(z_list,Fz)
# plt.yscale("log")
plt.title("Gravitational force $F_z(z)$")
plt.xlabel("z")
plt.ylabel("$F_z(z)$")
plt.savefig("gravitational2.pdf")
plt.show()


import numpy as np 

def aphelion():
	# take user input for perhelion distance and velocity: accept scientific notation
	l1=float(input("enter the distance to the Sun at perihelion in m:"))
	v1=float(input("enter the velocity at perihelion in m/s:")) 
	
	# define constant G and M
	M = 1.989E+30  # Mass of sun in kg
	G = 6.6738E-11 # gravitationla constant in km3kg-1s-2)

	v2= (2*G*M/(v1*l1)-v1)#smaller root from the quadratic equation from energy conservation

	print("velocity at aphelion v2 is %1.4Em/s" % v2)
	l2 = v1*l1/v2 
	print ("distance of aphelion l2 is %1.4E m" % l2)

	# use l2 and l1 to calculate coefficents a and b 
	a = 1/2*(l1+l2)
	b = np.sqrt(l1*l2)
	T = 2*np.pi*a*b/(l1*v1) #period in second
	T_year = T/(365*24*60*60) #convert unit from second to year
	print ("Orbital period P is %1.4E year" % T_year)
	e = (l2-l1)/(l2+l1)
	print ("Orbital eccentricity e is %1.4E" % e)

aphelion()

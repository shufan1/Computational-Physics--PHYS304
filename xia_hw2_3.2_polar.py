# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

#deltoid
# a list of theta value
theta = np.linspace(0,np.pi*24,1000)
# definiton of deltoid function to calculate x and y
x= 2*np.cos(theta)+np.cos(2*theta)
y= 2*np.sin(theta)+np.sin(2*theta)

plt.plot(x,y,label="deltoid")
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.title("deltoid",fontsize=20)
plt.legend(loc=1)
plt.savefig("deltoid.pdf")
plt.show()
plt.close()

# Galiean spiral
#find r for each theta
r=theta**2
#coordinate conversion
x_galiean = r*np.cos(theta)
y_galiean = r*np.sin(theta)

plt.plot(x_galiean,y_galiean,label="galiean spiral")
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.title("Galiean spiral",fontsize=20)
plt.legend(loc=1)
plt.savefig("spiral.pdf")

plt.show()
plt.close()

#Fey's function
# calcualte fey's function with a given theta
def fey(theta):
	r = np.exp(np.cos(theta))-2*np.cos(4*theta)+np.power(np.sin(theta/12),5)
	return r
#find r for each theta
r = list(map(fey,theta))
#coordinate conversion
x_fey = r*np.cos(theta)
y_fey = r*np.sin(theta)

plt.plot(x_fey,y_fey,label="fey's function")
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.title("Fey's funciton",fontsize=20)
plt.legend(loc=1)
plt.savefig("fey.pdf")
plt.show()
plt.close()

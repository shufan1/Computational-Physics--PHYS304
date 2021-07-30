import numpy as np
from math import factorial 
import matplotlib.pyplot as plt
import integration as itg

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# def H(n,x):
# 	if n == 0:
# 		return 1
# 	elif n==1:
# 		return 2*x
# 	else:
# 		return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)

def H(n,x):
	Hns=[]
	for i in range(n+1):
		if i ==0 : #base case 1
			Hns.append(1)
		elif i==1: #base case 2
			Hns.append(2*x)
		else: 
			Hn=2*x*Hns[i-1]-2*(i-1)*Hns[i-2] #recursive definition
			Hns.append(Hn)
	return Hns[n]


def phi(n,x):
	c = 1/(np.sqrt(2**n*factorial(n)*np.sqrt(np.pi)))*np.exp(-x**2/2)
	return c*H(n,x)

# plot H(n,x) for n=0,1,2,3 from x = -4 to 4
for n in [0,1,2,3]:
	x_list=np.linspace(-4,4,41,endpoint=True)
	phin=list(map(lambda x: phi(n,x), x_list)) #evaluate phi n over the range of x
	plt.plot(x_list,phin,label=("$\phi_%d(x)$"%n))

plt.title("$\phi_n, n=0,1,2,3$")
plt.legend()
plt.xlabel("x")
plt.ylabel("$\phi_n$")
plt.grid()
plt.savefig("wavefunction.pdf")
plt.show()


# plot phi30(x)
x_list2=np.linspace(-10,10,101,endpoint=True)
#evaluate Phi 30 over the range of x
P30=list(map(lambda x: phi(30,x), x_list2))
plt.plot(x_list2,P30,label=("$\phi_{30}(x)$"))
plt.title("$\phi_{30}(x)$")
plt.legend()
plt.xlabel("x")
plt.ylabel("$\phi_{30}$")
plt.savefig("phi30.pdf")
plt.show()



# part c

#substitue variable: x= z/1-z^2

def integrand(z):
	x = z/(1-z**2)
	dz = (1+z**2)/(1-z**2)**2
	return dz*x**2*phi(5,x)**2

I = itg.gaussion(integrand,-1,1,100) #use gaussion quadrature integration

print("The uncertanity is ", np.sqrt(I))
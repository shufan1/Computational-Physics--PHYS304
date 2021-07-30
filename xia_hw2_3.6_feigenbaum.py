import numpy as np
import matplotlib.pyplot as plt

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

def logistic_x(r,x):
	xlist = []
	x_prime = x  # starting value of x

	for i in range(0,1000): #iterate 1000 times and record the value of each x prime
		x = r*x*(1-x)
		xlist.append(x)
	#  settle down to a fixed point or limit cycle? .
	if np.abs(xlist[-1]-xlist[-2]) > 0.05:#limit cycle if the last two points differ a lot, I mean 0.1
		# return both of the last two numbers as a list
		return [xlist[-1], xlist[-2]]
	else: #fixed point, return the last float number
		return xlist[-1]

#this function add the result of logistic_x() to the list of data for plotting
def add_data(x, r_data, x_data):
	if isinstance(x, list): # limit cycle after 1000 iterations, 
		#we have two elements in a list, plot both (r,x') 
				r_data.append(r)
				r_data.append(r)
				x_data.append(x[0])
				x_data.append(x[1])

	else: # fixed point after 1000 iterations
		r_data.append(r)
		x_data.append(x)

# create a list of r values
r_value = np.linspace(1,4,301)
r_data = []
x_data = []

for r in r_value:
	x_prime = logistic_x(r,1/2)  #calucluate x' after 1000 iteration starting from x=1/2

	if isinstance(x_prime, list): #limit cycle, 
		#then we need to do another 1000 iterations on both x's
		for x_value in x_prime:
			x = logistic_x(r,x_value) #iterate another 1000 times
			add_data(x,r_data,x_data)
	else: # lfixed point
		x = logistic_x(r,x_prime) #iterate another 1000 times
		add_data(x,r_data,x_data)

# plot r vs x as scatter plot
plt.plot(r_data,x_data, label="Feigenbaum",ls = '', marker = '.', markersize=4)	
plt.xlabel('r',fontsize=20)
plt.ylabel('x',fontsize=20)
plt.title('Feigenbaum Plot',fontsize=20)
plt.legend(loc=1)
plt.savefig("feigenbaum.pdf")
plt.show()
plt.close()
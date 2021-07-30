# author: Shufan Xia
# date: Mar.27th, 2020

import numpy as np
import matplotlib.pyplot as plt


#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# define all constants

G = 6.674E-11 # m^3kg^-1s^-2
M = 5.974E24 # kg
m = 7.348E22 # kg
R = 3.844E8 # m 
omega = 2.662E-6 #s^-1

# define the fucntion f(r):
def f(r):
    a = G*M/(r**2)-G*m/((R-r)**2)-omega**2*r
    return a

# define the dereivative of the fucntion f(r):
def df(r):
    a = -2*G*M/(r**3)-2*G*m/((R-r)**3)-omega**2
    return a

r_range = np.linspace(0.05*R,2*R,101)
f_r = list(map(lambda r: f(r), r_range))
plt.plot(r_range, f_r, label="$f(r)$")
plt.title("plot f(r) to guess the solution")
plt.xlabel("r(m)")
plt.ylim(top=0.06)  # adjust the top leaving bottom unchanged
plt.ylim(bottom=-0.04)
plt.axhline(color='k')
plt.legend()
plt.savefig("L1guess.pdf")
plt.show()

# use Netwon Rapshon method

# define maximum number of iterations, 
imax = 500
# set iterations counter to 0
i = 0
# set the tolerance
tol = 1.E-4
# f(0.0001
# x_appros-xreal/xreal = 0.0001
# x1this-x1last/xthis = 0.0001
roots = []

guesses = [3.4E8] # Make a guess as to what the root
xi = [3.4E8]
for x0 in guesses:
    # iterating loop of Netown_search method
    while i<imax:
        x1 = x0-f(x0)/df(x0) # find the next guess for x
        xi.append(x1)
        if np.abs(xi[i+1]-xi[i]) < tol: # if f(x1)<tol, we find the root
            roots.append(x1) # append the solution and exit the loop for guessing
            break
        else:
            x0 = x1 #update the old guess with the new guess
            i+=1 # increment the loop 

print("r = %.4e"% roots[0])
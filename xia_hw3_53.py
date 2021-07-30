
import numpy as np
import integration as itg
import matplotlib.pyplot as plt
import math
#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

## define integrand
def f(t):
    value = np.exp(-1*t**2)
    return value

## Following section deal with the question what number of steps should I use??
def threeD_f(t):
    value = 12*f(t)*t-8*f(t)*t**3
    return value
 
 ## error of simpson integration as a function of N, step number   
def error_simpson(a,b,N):
    h = (a-b)/N
    threeD_a = threeD_f(a)
    threeD_b = threeD_f(b)
    return 1/90*h**4*(f(a)-f(b))


# use simpson integration method to find the integral of e^-x^2 from 0 to x for each x value
step = np.linspace(1,6000,501)

In = list(map(lambda n: itg.simpson(f,0,3,n),step)) #find the result of the integral ny taking n steps

error = list(map(lambda n,I: np.abs(error_simpson(0,3,n))/I,step,In)) #compute fractional error 

#plot fractional error
plt.plot(step,error,label="Fractional error")
plt.yscale('log') ## plot in log scale
plt.xlabel("Number of bins $N$")
plt.ylabel("log(Fractional error of $J_n(x))$")
plt.title("Fractional error of $E(x)=\int_0^x e^{-t^2} dx$ " )
plt.legend()
plt.savefig('erfError.pdf')
plt.show()

# a list of x values from 0 to 3, step = 0.1
x_values = np.linspace(0,3,31)

# use simpson integration method to find the integral of e^-x^2 from 0 to x for each x value
Ex1 = list(map(lambda x: itg.simpson(f,0,x,5000),x_values))
plt.subplot(121)
plt.plot(x_values, Ex1,label="$E(x)$")#, color='orange',linewidth=6)
plt.title("a) $E(x)=\int_0^x e^{-t^2} dx$")
plt.xlabel("$x$")
plt.ylabel("$E(x)$")
plt.legend()


### compare with math.erf()

## compute the integral using erf(x), multiply by some constant
def E(x):
    I = 0.5*math.erf(x)*math.sqrt(math.pi)
    return I

   
x_values = np.linspace(0,3,31)
Ex2 = list(map(lambda x: E(x), x_values)) # a list of E(x) evaluated at different x values.

## plot E(x) by integration and amth.Erf side by side
plt.subplot(122)
plt.plot(x_values,Ex2,color='b',label=r'$\frac{\sqrt{\pi}}{2}$ Erf(x)')
plt.title(r'$\frac{\sqrt{\pi}}{2}$ Erf(x)')
plt.xlabel("$x$")
plt.ylabel(r'$\frac{\sqrt{\pi}}{2}$ Erf(x)')
plt.legend()
plt.savefig("erf.pdf")
plt.show()
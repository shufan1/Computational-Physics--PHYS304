### 5.10 Period of an anharmonic oscillator
import numpy as np
import integration as itg
import matplotlib.pyplot as plt

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# supress division by zero warning
np.seterr(divide='ignore', invalid='ignore')

# define the potential well
def V(x):
    return x**4

## define the integrand, a function of x with a specific input value of a
def f(a): # a, amplitude
    def fx(x):
        f = 1/np.sqrt(V(a)-V(x))
        return f
    return fx

# mass of the oscillator
m = 1


a_value = np.linspace(0,2,51)

c = np.sqrt(8*m) # constant term of the integrand

T = list(map(lambda a: c*itg.gaussion(f(a),0,a,20),a_value)) # Calculate Period T of each a value by gaussion integration using 20 points

#plot period vs a.
plt.plot(a_value,T,label="Period $T(a)$")
plt.title("Period as a function of a $T(a)$ ")
plt.xlabel("$x(m)$")
plt.ylabel("$T(s)$")
plt.legend()
plt.savefig("period.pdf")
plt.show()
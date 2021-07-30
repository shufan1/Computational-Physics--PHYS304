## 5.4
import numpy as np
import integration as itg
import matplotlib.pyplot as plt

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

## define the integrand
## input:m and x
## output the integrand as a fucntion of x with specific m abd x value
def f_mx (m,x):
    def f(theta):
        return np.cos(m*theta-x*np.sin(theta))
    return f

## define Jm as a funciton of m and x   
def Jm(m,x):
    ## what is the integrand with m and x
    f=f_mx(m,x)
    ## integrate from 0 to pi, using Simpson's rule with N = 1000
    I = itg.simpson(f,0,np.pi,1000)
    return (1/np.pi)*I


m = [0,1,2]

x_values = np.linspace(0,20,201)

## evaluate J_m(x) from x =0 to 20
J0 = list(map(lambda x: Jm(0,x), x_values ))
J1 = list(map(lambda x: Jm(1,x), x_values ))
J2 = list(map(lambda x: Jm(2,x), x_values ))

# plot Jn
plt.plot(x_values, J0, label="$J_0$")
plt.plot(x_values, J1, label="$J_1$")
plt.plot(x_values, J2, label="$J_2$")
plt.title("Bessel function $J_m(x)$ for $m=0,1,2$")
plt.xlabel("$x$")
plt.ylabel("$J_m(x)$")
plt.legend()
plt.savefig("Bessel_function.pdf")
plt.show()

#5.4 part b

# a function to compute and plot diffraction pattern
## input: wavelength 
## ouput: a 2D plot for diffracton pattern
def diffraction(wavelength):
    import numpy as np

    k = 2* np.pi/wavelength # wavenumber
    
   # a function compute I, intenisty at a given distance
    def I_r(r):
        J1=Jm(1,k*r)
        I = (J1/k/r)**2 
        return I

    ## a gird of x and y axis covers 1miu m from the origin 
    x_axis = np.linspace(-1.E-6,1.E-6,101)
    y_axis = np.linspace(-1.E-6,1.E-6,101)

    I = np.zeros((101,101)) # a 2D array to hold the results of I


    n_x=0 ## track column number in the 2D data array
    for x in x_axis:
        n_y=0  # track row number in the 2D data array
        for y in y_axis:
            r = np.sqrt(x**2 + y**2) #compute the distance to origin
            if (r!=0):
                In=I_r(r) # compute I
                I[n_x][n_y]=In #update I
            
            ## I(r) is not defined at r=0, use approximation instead
            else:
                I[n_x][n_y] =0.5**2  # approximation of I(r) when r =0
            n_y+=1 # go on to the next row
        n_x+=1 # to the next column
   
   # plot 2D diffractio result 
    plt.imshow(I, origin="lower", vmax=1.0E-2,extent=[-1,1,-1,1])  ## vmax =1.0E-2 for adjustment to show the pattern 
   
    plt.title("Density Plot of Intensity")
    plt.ylabel("$y(\mu m)$")
    plt.xlabel("$x(\mu m)$")
    plt.hot()
    plt.savefig("diffraction.pdf")
    plt.show()
    
diffraction(500E-9)  # diffractio pattern for wave of 500miu m 


### additional part

### ignore division by zero warning
np.seterr(divide='ignore', invalid='ignore')

def Jn(n,x):
    ## base case n=0 and 1
    if n == 0:
        return Jm(0,x)
    elif n==1:
        return Jm(1,x)
    ## recusive call
    else:
        J_n = 2*(n-1)/x*Jn(n-1,x)-Jn(n-2,x)
        return J_n
    
for n in [2,3,4]:
    x_list = np.linspace(0,20,201)
    Jnx=[]
    Jnx = list(map(lambda x: Jn(n,x),x_list)) # compute Jn at all x values by recursion
    integral_J = list(map(lambda x: Jm(n,x), x_list )) #Jm(n,x) compute the value of J2,3,4 at speceific x by integration

    # plt.plot(x_list,Jnx,label=("J%d"%n))

# plt.title("Bessel function by recusion")
# plt.legend()
# plt.savefig("recursion.pdf")
# plt.show()


#compute fractional error (J by recursion - J by integration)/J by recursion for each n
    error = np.abs(np.array(integral_J)-np.array(Jnx))/np.array(Jnx)
    plt.plot(x_list,error,'.',label="fractional error J%d"%n)
   
# format the plot 
plt.yscale('log')
plt.title("fractional error between $J_n(x)$ using integration and recursion method")
plt.xlabel("$x$")
plt.ylabel("fractional error of $J_n(x)$")
plt.legend()
plt.savefig("error.pdf")
plt.show()

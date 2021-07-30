import numpy as np
import matplotlib.pyplot as plt
import integration as itg # integration is my own integration library

# define constant
a = 10 #eV
a = a*1.60218e-19 #J, convert eV to J
L = 5e-10 #5 Angstrom
hbar = 1.0545718e-34 #m2 kg 
M = 9.1094e-31 #kg


@np.vectorize  # vectorize the function Hmn(m,n)

# this function computes matrix element Hmn at mth row and nth value based on equation 31 in write-up.
def Hmn(m,n):
    if m != n:
        if (m%2!=0 and n%2!=0) or (m%2==0 and n%2==0): # m neq n and both are even or odd
            return 0
        else:
            return -8*m*n*a/(np.power(np.pi*(m**2-n**2),2)) # m neq n, one is even and one is odd
    else:
        return np.power((hbar*n*np.pi),2)/(2*M*L**2)+a/2 # m=n
  

#this function returns an m*m matrix, each entry is Hmn
def matrixH(m):
    # a grid of n and m values for m*m matix
    # n for column indices, m for row indicies. Both starts from 1
    n,m = np.meshgrid(np.arange(1, m+1, 1),
                  np.arange(1, m+1, 1))
   
    H = Hmn(m,n)
    return H

##use a 10*10 H matirx
H=matrixH(10)
E10,Psi10 = np.linalg.eigh(H) #solve for eigen values and vectors. #eigen values are sorted from the lowest to the highest and with corresponsing egien vectors
E10 = E10/(1.60218E-19) # convert from J to eV
print("H is 10 by 10")  
print("Ground state energy:", E10[0])  # ground state energy
print(Psi10[:,0]) #ground state eigen vector

##use a 100*100 H matirx
H=matrixH(100)
E100,Psi100 = np.linalg.eigh(H) #solve for eigen values and vectors. #eigen values are sorted from the lowest to the highest and with corresponsing egien vectors
E100 = E100/(1.60218E-19) # convert from J to eV
print("H is 100 by 100")
print("Ground state energy:", E100[0]) # ground state energy
# print(Psi100[:,0]) #ground state eigen vector


## part d)

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)


## define the integrand psi^2(x) to find the normalization constant
def psi_n_square(n):
    Cn = Psi10[:,n-1] # the coefficent of nth state. It is (n-1)th column of the Psi10 2D array becasue n starts from 1 (ground state) and correspond to 0 index in python array
    def density(x):
        psi = 0 
        for i in range(len(Cn)):
            psi += Cn[i] *np.sin((i+1)*np.pi*x/L)   ##linear combination of eigen functions sin(npix/L)
        return psi**2 #probability density function is square of wave function
    return density

# this function returns the factor to normalize a probability denisty function
def normalize(f):
    I = itg.gaussion(f,0,L,100)
    C= 1/I # compute normalization factor
    return C 

# compute normalization factor for n=1,2,3 probability density function
normalizer = []
for i in range(3):
    normalizer.append(normalize(psi_n_square(i+1))) #i is [0,1,2] 




def normalized_density_n(n,x):
    Cn = Psi10[:,n-1] # the normalization coefficent of nth state. It is (n-1)th column of the Psi10 2D array becasue n starts from 1 (ground state) and correspond to 0 index in python array
    psi = 0 
    for i in range(len(Cn)):
        psi += Cn[i] *np.sin((i+1)*np.pi*x/L) ##linear combination of eigen functions sin(npix/L)
    density = psi**2
    density = density*normalizer[n-1] #normalize using the corresponding normalization factor
    return density


x_values = np.linspace(0,5e-10,101) # plot the probability density functio inside the well from x=0 to L

psi_square_1 = list(map(lambda x: normalized_density_n(1,x), x_values)) # compute density fucntion of the ground state
psi_square_2 = list(map(lambda x: normalized_density_n(2,x), x_values)) # compute density fucntion of the 1st excited state
psi_square_3 = list(map(lambda x: normalized_density_n(3,x), x_values)) # compute density fucntion of the 2nd excited state

# plot the normalized denisty function
plt.plot(x_values,psi_square_1,label = "${|\Psi_1|}^2$")
plt.plot(x_values,psi_square_2,label = "${|\Psi_2|}^2$")
plt.plot(x_values,psi_square_3,label = "${|\Psi_3|}^2$")
plt.xlabel("x(m)")
plt.ylabel("${|\Psi_N|}^2$")
plt.axhline(y=0, color='k') 
plt.axvline(x=0, color='k') # add the boundary of the potential line
plt.axvline(x=5e-10, color='k')
plt.title("Probability Density function ${|\Psi_N|}^2$ for $N=1,2,$ and 3 ")
plt.legend()
plt.savefig("probDens.pdf")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
# import 2D FFT functions
from numpy.fft import rfft2,irfft2,fft2

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# read in the image file
img= np.loadtxt("blur.txt",float)
plt.imshow(img)
plt.gray()
plt.title("Blurred Image")
plt.savefig("Blurred.pdf")

plt.show()


###################################################################################
###################################################################################
# find the dimension of the photo
nrow = len(img)
ncol = len(img[0])
# the dimension of the photo is x = 0 to 1023 and y=0 to 1023

# find the correct transformation on x and y so that the point spread function is periodic as desired
    #in order for x and y come back to 0 and 0 at x=L and y=L
    # a half period of x and y must be 1024, abd x and y have their max at 512, L/2 
y=[]
x = np.linspace(0,2048,2049)
for i in x:
    k = int(i/512)
    if k%2 ==1:
        i =  512*(k+1)-i
    if k%2==0:
        i = i-512*k
        
    y.append(i)

# check if the transformation does make x peak to 512 and drop to 0 every 1024 points
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("trasformation on x for $f(x,y)$ to be periodic")
plt.title("Transformation on x value")
plt.savefig("x.pdf")
plt.show()



#define the point spread function
@np.vectorize  # vectorize the function

def f(x,y):
    sigma = 25
# transform c and y coordinate
    kx = int(x/512)
    if kx%2 ==1:
        x =  512*(kx+1)-x
    else: # kx%2==0:
        x = x-512*kx

    ky = int(y/512)
    if ky%2 ==1:
        y =  512*(ky+1)-y
    else: # ky%2==0:
        y = y-512*ky
        
# calculate the function value at (x,y)        
    fxy= np.exp(-(x**2+y**2)/(2*sigma**2))
    return fxy


# 2D array with the same dimension of the photo
n,m = np.meshgrid(np.arange(0, nrow, 1),
                  np.arange(0, ncol, 1))
# calculate the function value at each (x,y) 
pointSpread = f(n,m)

# plot the 2d point spread function
plt.imshow(pointSpread,origin="lower",vmax=0.4)
plt.gray()
plt.title("$f(x,y)e^{(-(x^2+y^2)/2\sigma ^2)}$")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("gau.pdf")
plt.show()

#################################################################################################
#################################################################################################
# FFT of the orignal blurred photo
bk = rfft2(img)
# FFT of the 2D point spread function
fk = rfft2(pointSpread)

@np.vectorize  # vectorize the function

# define the function to check fk is not too samll in order to avoid error 

@np.vectorize
def f_correct(f):
 	# to avoid division by a very small fk, set a threshold value, 10E-3
    threshold = 10E-3
    if np.real(f) <threshold: 
    # if under the threshold, to leave the coefficient alone in the next step :bl/(fk*l^2), make fk=1
        return 1 
    else: 
    # otherwise, fk is okay
        return f 

fk = f_correct(fk) # correct fk values

ak = bk/(fk*1024*1024) # find the Fourier Transform of the unblurred image
axy = irfft2(ak) #reverse Fourier transform to reconstruct the original brightness function

# plot the image
plt.imshow(axy)
plt.title("Deblurred Image")
plt.savefig("deblurred.pdf")
plt.show()




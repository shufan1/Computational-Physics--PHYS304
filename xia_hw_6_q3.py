# author: Shufan Xia
# date: Mar.27th, 2020

import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np 

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

# read data file
with open('cmb.txt','r') as f:  
    l_full=[]
    yl=[]
    i=0
    for line in f:
        data=line.split()
        l_full.append(float(data[0]))
        yl.append(float(data[1]))     
f.close()

## plot the real data
# plt.plot(l_range,yl,label="power spectrum")
# plt.xlabel("$l$")
# plt.ylabel("$l(l+ 1)C_l^{TT}/(2\pi)$")
# plt.title("CMB temperature power spectrum")
# plt.savefig("spectrum.pdf")
# plt.show()

# cubic interpolation

# use 200 points from the data file as our data for interpolation
l_list = l_full[::11]
spec = yl[::11]

f = interp1d(l_list,spec,kind="cubic")

lnew = l_full[:2190]  #l>2190 is outside the interpolation raneg
ynew=f(lnew) #using the introplated function to find y-axis value

# calcualte fractional error
error = np.abs((ynew-yl[:2190])) # absolute error
frac_error=np.abs((ynew-yl[:2190]))/yl[:2190] 

# plot origional and introplated data
plt.plot(l_full,yl,'-', linewidth="5",label='real data') #original data
plt.plot(lnew,ynew,label="interpolation", marker='o',markersize=1) #introloated data
plt.xlabel("$l$")
plt.ylabel("$l(l+ 1)C_l^{TT}/(2\pi)$")
plt.title("CMB temperature power spectrum")
plt.legend()
plt.savefig("interpolation.pdf")
plt.show()

# plot fractional error
plt.plot(lnew,frac_error, '.' ,markersize=2,label="fractional error")
h = list(map(lambda x: 3/x, l_full)) #plot the comparision value
plt.plot(l_full,h,label="$3/l$")
plt.xlabel("$l$")
plt.legend()
plt.title("Fractional error")
plt.savefig("error.pdf")
plt.show()

# To see fractinal error better, only plot fractional error
plt.plot(l_full[:2190],frac_error, '.',markersize=2,label="fractional error")
plt.xlabel("$l$")
plt.legend()
plt.title("Fractional error")
plt.savefig("Fractional.pdf")
plt.show()
plt.show()

#####################################################################3
#####################################################################
# part b

# central difference method with step size = 2
# define the function : 
#           input: a list of values of a function f(x) evaulated at each x
#           output: a list of values of a f'(x) evaulated at each x
def df(f):
    df = []
    i = 1
    i_max = len(f)-1
    while i<i_max:
        fprime = (f[i+1]-f[i-1])/2 #with step size = 2
        df.append(fprime)
        i += 1
    return df

# find ClTT from CMB data
ClTT = list(map(lambda x,y: 2*np.pi*y/(x*(x+1)),l_full,yl))
# take first order derivative
dClTT = df(ClTT)

plt.plot(l_full[1:-1],dClTT,'.',markersize=2,label = "$dC_l^{TT}$")
plt.xlabel('l')
plt.legend()
plt.title("$dC_l^{TT}$")
plt.savefig('derivative.pdf')
plt.show()


# theoretical expression for spline errors???
# e = h/4! max(f''''(x)) from l_min  to l_max
# where f = the intrpolated function

# first derivative
df1 = df(ynew)

# second derivative
df2 = df(df1) 

# third derivative
df3 = df(df2)

# fourth derivative
df4 = df(df3) 

h = 11 #step size = 11
# theoretical expression for spline errors
e = 11**4*max(df4)/(4*3*2)
# the length of df4 is 2199-8=2191
theo_e = np.full(2190,e)


theo_e_f = np.abs(theo_e)/ynew

# plot fractional error
plt.plot(lnew,theo_e_f,'.',markersize=2,label="theoretical fractional error")
plt.plot(lnew,frac_error,'.',markersize=2,label="fractional error")
plt.legend()
plt.title("Theoretical fractional error ")
plt.savefig('fractionalTheo.pdf')
plt.show()

# plot absolute error
plt.plot(lnew,theo_e,'-',label="theoretical error $\epsilon$")
plt.plot(lnew,error,'.',markersize=2,label="$|residual|$")
plt.legend()
plt.title("Theoretical error ")
plt.savefig('theoretical.pdf')
plt.show()

###################################################################
###################################################################3
# part c
# substiution by variable 

z = list(map(lambda l: l/(1+l), l_full))

# substitution with z=l/(l+1) into l(l+1)ClTT/2pi to find fz=z*ClTT(z)/2pi in terms of z
fz = list(map(lambda y,z: y/(1-z),yl,z))

# use trapezoid method to find the integral of 
N = len(fz)
s = 0

for i in range(N-1):
    a = fz[i]
    b = fz[i+1]
    h = z[i+1]-z[i]
    area = 1/2*h*(a+b)
#     if i== 2197:''
#         print(a,b,h)
    s += area

print(s)

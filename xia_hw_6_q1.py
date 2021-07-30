
# author: Shufan Xia
# date: Mar.26th, 2020

# import packages
import numpy as np
import matplotlib.pyplot as plt

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

me = 9.1094E-31 #kg
V = 20*1.6E-19 #J
omega = 1E-9 #m
hbar = 1.05457E-34; #J*s
 
def y1(E):
    return np.tan(np.sqrt(omega**2*me*E/(2*hbar**2)))

def y2(E):
    return np.sqrt((V-E)/E)

def y3(E):
    return -1*np.sqrt(E/(V-E))

E = np.linspace(0.01*1.6E-19,20*1.6E-19,401)

y1 = list(map(lambda E: y1(E),E))
y2 = list(map(lambda E: y2(E),E))
y3 = list(map(lambda E: y3(E),E))

plt.plot(E,y1,'.',label="y1")
plt.plot(E,y2,label="y2")
plt.plot(E,y3,label="y3")
plt.ylim(top=10)  # adjust the top leaving bottom unchanged
plt.ylim(bottom=-10)  
plt.axhline(color='k')
plt.xlabel("E(J)")
plt.legend()
plt.title("$y1=tan\sqrt{\omega^2 m E /2{\hbar}^2}$, $y2= \sqrt{(V-E)/E}$, and $y3= -\sqrt{E/(V-E)}$")
plt.grid()
plt.savefig("y23.pdf")
plt.show()


# guess of the first sixth
# E1=0.2E-18 J
# E2=0.4E-18 J
# E3=0.8E-18 J
# E4=1.3E-18 J
# E5=1.7E-18 J
# E6=2.4E-18 J


# Binary search method of solving

#decide on the bracketing values that will constrain the root
def bracket(F):
    i = 0
    E = np.linspace(1*1.6E-19,20*1.6E-19,201)
    brackets=[] 
    while i<200:
        if ((F(E[i])>0 and F(E[i+1])<0) or (F(E[i])<0 and F(E[i+1])>0)) and (np.abs(F(E[i])-F(E[i+1])<0.001)):
            brackets.append([E[i],E[i+1]])
        elif (F(E[i])==0):
            brackets.append([E[i]]) 
        i +=1
    return brackets 

########################################################################################

########################################################################################

# bisection to find the solutions
def binary_solve(F,guess_range):
    # define a maximum number of iterations, 
    imax = 100
    # iterations counter to 0
    i = 0
    # tolerance of the accuracy
    tolerance = 0.001E-19
    
    root = []
    for bracket in guess_range:
        if len(bracket)==1: # in case we have magically found the root
            root.append(brakcet[0])
        else:
            #decide on the bracketing values that will constrain the root
            x0 = bracket [0]
            x1 = bracket [1]
            while i <imax: # iterating loop on bisecting
                x2 = (x0+x1)/2
                if (F(x2)*F(x0)>0):
                    x0=x2
                else:
                    x1=x2
                if np.abs(x0-x1)<tolerance:
                    root.append(x1) 
                    break
                i+=1
    return root
# ------------------------------------------------------------------
# define our functions
# for even numbered states
def F1(E):
    c = np.tan(np.sqrt(omega**2*me*E/(2*hbar**2)))+1*np.sqrt(E/(V-E))
    return c

# for odd numbered states
def F2(E):
    c =np.tan(np.sqrt(omega**2*me*E/(2*hbar**2)))-np.sqrt((V-E)/E)
    return c

# find all roots for odd numbered state with E<20eV
binary_range=bracket(F1)
odd_roots=binary_solve(F1,binary_range)  

# find all roots for odd numbered state with E<20eV
binary_range=bracket(F2)
even_roots=binary_solve(F2,binary_range)   

# put all solutions together and sort them in ascending order
roots = odd_roots+even_roots
roots.sort()


# the solution for the first six energy
Bi_sols = roots[:6]
Bi_sols = list(map(lambda x: x/(1.6E-19),Bi_sols)) # convert the result to eV
print(Bi_sols)


########################################################################################

########################################################################################    
# Newtown-Raphson method for solving

# ----------------------------------------------------------------
def df1(E):
    C = omega**2*me/(2*hbar**2)
    a = C*1/(np.cos(np.sqrt(C*E))**2/(2*np.sqrt(C*E))) # sec x =1 /cos x
    b = (1/(V-E)+E/((V-E)**2))/(2*np.sqrt(E/(V-E)))
    return a+b
         
def df2(E):
    C = omega**2*me/(2*hbar**2)
    a = C*1/(np.cos(np.sqrt(C*E))**2/(2*np.sqrt(C*E)))
    b = (-(V-E)/E**2-1/E)/(2*np.sqrt((V-E)/E))
   
    return a+b



def Netwon_Search(f,df,guesses):

    # define a maximum number of iterations, 
    imax = 2000
    # set iterations counter to 0
    i = 0
    # set the tolerance
    tol = 0.001E-19
    
    roots = []
    # multiple roots so multiple guesses
    for x0 in guesses:
        xi = [x0]
        # iterating loop of Netown_search method
        while i<imax:
            x1 = x0-f(x0)/df(x0) # find the next better guess
            xi.append(x1)
            if np.abs(xi[i+1]-xi[i]) < tol: # if f(x1)<tol, we find the root
                roots.append(x1) # append the solution and exit the loop for guessing
                i = 0
                break
            else:
                x0 = x1 #update the old guess with the new guess
                i+=1 # increment the loop 

    return roots

odd_guess = [0.2E-18,0.8E-18,1.7E-18]
odd_sols = Netwon_Search(F1,df1,odd_guess)  

even_guess = [0.4E-18,1.25E-18,2.4E-18]
even_sols = Netwon_Search(F2,df2,even_guess)


Netown_sols = odd_sols+even_sols
Netown_sols.sort()
Netown_sols=list(map(lambda x: x/(1.6E-19),Netown_sols))
print("Solved by Netwon method:", Netown_sols)
print("Solved by binary search method:",Bi_sols)
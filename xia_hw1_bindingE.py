import numpy as np

## part (a)
def binding_Energy(A,Z): # A is mass number, Z stands for atomc number
	#define constant
	a1=15.8
	a2=18.3
	a3=0.714
	a4=23.2
	#check if A is odd or even, and define a5
	if A%2!=0: #A is odd
		a5=0.0
	elif (A%2==0 and Z%2==0): #A is even and Z is even
		a5=12.0
	else : #Z is odd
		a5=-12.0
	binding_Energy = a1*A-a2*np.power(A,2/3)-a3*np.power(Z,2)/np.power(A,1/3)-a4*np.power((A-2*Z),2)/A+a5/np.power(A,(1/2))
	
	return binding_Energy

print("part a:")
print("Binding energy for an atom with A=58 and Z=28 is %1.2f" % (binding_Energy(58,28))) 



## part(b)
def binding_perN(A,Z): # A is mass number, Z stands for atomc number
	bE= binding_Energy(A,Z) # calculate the binding energy with given A and Z
	return bE/A  #return binding energy per nucleon
print("part b:")
print("B/A with A=58 and Z=28 is %1.2f(MeV)" % (binding_perN(58,28)))

##part(c)
def most_stable_A(Z): #  Z stands for atomic number

	energyPerN =[] # create a list to hold binding energy per nucleon for each A from A=Z to A= 3Z
	# for loop from Z to 3Z
	for A in range(Z,3*Z+1):
		binding_Energy = binding_perN(A,Z) # find binding energy per nucleon with given A and Z
		energyPerN.append(binding_Energy) 

	A = energyPerN.index(max(energyPerN))+Z # find A of the maximum B/A

	print("most stable A %d\nB/A max: %1.2f(MeV)" % (A,max(energyPerN))) #print A and max B/A

	return A,max(energyPerN) 

print("part c:")
most_stable_A(28) #call function on Z = 28


#part(d)
def most_stable_allZ():
	B_allZ=[] #a list to hold the hinghest binding energy per nucleon for each atomic number Z
	for z in range(1,101): # foor loop for Z from 1 to 100
		print("Z=",z)
		highest_B=most_stable_A(z)[1] #find the most stable binding energy for each Z 
				#and the function will print the maximum binding energy and the most likely A value

		B_allZ.append(highest_B) # add that maximum value to the list
	
	#search the list to find the maximum binding energy per nucleon 
	# and use the index to find the corresponding Z value
	print("\nZ of max B/A: %d, with %1.2f(MeV)"%(B_allZ.index(max(B_allZ))+1, max(B_allZ)))	
print("part d:")
most_stable_allZ()

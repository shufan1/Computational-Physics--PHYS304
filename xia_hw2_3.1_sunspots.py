# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Use Latex fonts
plt.rc('font', family='serif')
plt.rc('text', usetex=True)

#part a
# read data
data = np.loadtxt("sunspots.txt",float)
month = data[:,0]
sunspots = data[:,1]
# plont sunspots vs month
plt.plot(month,sunspots,'k',label="sunspots",linewidth=0.5)
plt.title('Sunspots observed each month since January 1749',fontsize=20)
plt.xlabel('Month since January 1749',fontsize=20)
plt.ylabel('Number of sunspots',fontsize=20)
plt.legend(loc=1)
plt.savefig('sunspots.pdf')
plt.show()
plt.close()


# part b
# plot the first 1000 data
plt.plot(month[:1000],sunspots[:1000],'k',label="sunspots",linewidth=0.5)
plt.title('Sunspots observed each month since January 1749 ',fontsize=20)
plt.xlabel('Month since January 1749',fontsize=20)
plt.ylabel('Number of sunspots',fontsize=20)
plt.legend(loc=1)
plt.savefig('1000months.pdf')
plt.show()
plt.close()

# claculate running average
running_average = [] # a list holding the running 

for i in range (5,1000):
 #starting from the fifth month since Jan 1749, calculate running avaerage of sunspots for each month

	yk=sunspots[i]
	r =5 
	sum = 0
	# find the sum of sunspots over the 5 months before and after each month
	for m in range (-5,6): #r = -5 t0 5, 
		sum+=sunspots[i+m]
	running_average.append(sum/(2*r+1))


plt.plot(month[:1000],sunspots[:1000],'k',label="sunspots",linewidth=0.5)
plt.plot(month[5:1000], running_average,label="running average"'c')
# skip the first 5 data data of month when plotting running aveage because we only hae 995 data

#axis labels
plt.title('Sunspots observed each month January 1749', fontsize=20)
plt.xlabel('Month since January 1749',fontsize=20)
plt.ylabel('Number of sunspots',fontsize=20)
#put down a legend
plt.legend(loc=1)

plt.savefig('run_average.pdf')
plt.show()
plt.close()
